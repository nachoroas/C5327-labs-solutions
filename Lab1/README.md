# Laboratorio 1 
Martín Bahamonde
Martín Rojas

## Soluciones a las preguntas

### Parte a.-

#### Cambiando el largo del mensaje:
Para el largo del mensaje se probaron los siguientes str:
1234567890abcdef
123456789
12345678

Hasta que se vio disminuida la cadena de texto cifrado, como sabemos que el cifrador es aes, los bloques son de 16 bytes, teniendo en consideración aquello notamos que con el largo de 9 el padding cambia, eso significa que hay un bloque entero (16 bytes) de padding, después, obteniendo el texto cifrado, notamos que hay 256 caracteres en texto hexadecimal, por ende, considerando que dos caracteres codifican a un byte, dicho texto tiene 128 bytes.

Entonces, considerando que son 128 bytes y que 16 son de padding y 9 son del mensaje, eso nos deja que quedan 103 bytes de la clave... ahora si es que en el texto cifrado también está IV (típicamente de 16 bytes) entonces la clave son 87 bytes

#### Modificando un character del plaintext:
Por otro lado, al cambiar un caracter, por ejemplo el ultimo, cambia toda la cadena cifrada:
12345678: 
``` 
beb4bd88c570382b0474cc7d231bfe9270ea5306b54104a1b9a314af95e83de53fb00ca028a1747d34ad79c892dd6496f904e61690ccd49d4b9210f3bd1b11d992672e0f2abd6e515ca1a6721f235e6bce7d28d2bc910065a1919524dbd4d52bc2edc61cc2f2e0b5fc7df5760f07291d
```

1234567a: 
```
2bbc171eae04cdb0670f543a048026603b1f9cee4d585f6045157c34cc7442d9a066132103de6bd22785d0a92bb2d8beae2bfd2c3fcf523d8030a67c762f7c51b34e37fa0117952dd0cd6a07583cb1004c160f8978783d190f91635c91f132c2680aac8e3e123a89f1dddbd9350d0be2
```

Estos resultados son esperables del AES

#### Modificando un byte del texto cifrado (no padding):

Para este caso se uso la respuesta de "12345678", dicha respuesta cifrada, la pasamos a un array de bytes usando la funcion hextobytes para poder modificar el ultimo byte y probar mandarselo al servicio B (nuevamente en hex usando la funcion inversa)

El resultado, considerando que modificamos un byte que sabemos no es de padding, es la siguiente

```
"[Server] "json: invalid character '\a' in string literal""
```
Lo que significa que el cambio que hicimos hizo que el padding fuera valido, pero la desencriptación no lo fuese.



#### Modificando un byte del texto cifrado, que es de padding:

Ahora, modificando un byte de padding, el servidor nos devolvió:
 ```
"[Server] "pkcs7: invalid padding (last byte is larger than total length)""
```

Esto es una vulnerabilidad por parte del servidor, puesto nos permite usar el ataque de padding oracle

### Parte b.- 
Al enviar al servidor B la respuesta de A obtenemos el mensaje inicial cifrado, esta función se llama dec

### Parte c.- 
Para conocer el largo del cifrador se puede enviar un mensaje de largo L_m al cifrador, este enviará una cadena de largo L_c, luego, hay que iterar sumando un caracter de largo al mensaje (L_m) hasta conseguir que el largo de L_c cambie.

Una vez logrado esto, hay que tener en consideración que el encriptador puede añadir una concatenacion al mensaje antes de cifrar, por ende, una vez haya cambiado, podemos saber que estamos con un bloque de solo padding, ahora, hay que ir sumando nuevamente caracteres a L_m hasta que L_c cambie, el número de caracteres sumados en esta iteración final, es el tamaño del bloque.

### Parte d.- 
Para decifrar el byte, primero dividimos en bloques de 16 bytes, (pasandolos a byte desde hex), luego, en el penultimo bloque se hace un for cambiando el byte desde 0 a 255 hasta que nos de error, cuando obtenemos un "json:" Se interpreta que la modificación produjo una salida en la que el descifrado resulta en un formato JSON (o al menos, es la señal que se esperaba para indicar que se logró un descifrado "válido"). En este caso, se imprime un mensaje indicando que se encontró el byte correcto y se retorna el valor i.

En lab_solutions.py el caso 4 representa lo dicho con el texto encriptado:
"e2a0bb3fe8a4ff55ca8e8c7048a521fe99865dead7dc6d2712a7701bb36bf78b2f8c2f11d97e5d2c051c8eb56b91fe61f5c81ba7b5ba6439aeff3a83d50c94f93c91a8fabd7f68916fca94d2178577e8746430a186275287fbf15fcf11f4a71b38d754c60009b4693ee6ba68d1eb3a0958f0f71db7813b2cf993fb99cfd32f04"

### Parte e.- 
Acá, se implementa la parte escencial del ataque de padding para decifrar un bloque.
Primero obtenemos los datos en byte usando la función hex to byte, después se dividen en bloques de 16 bytes, donde se guarda el ultimo y penultimo bloque, además se inicializa un vector de 16 bytes para el plaintext:

```python
def decrypt_block(ciphertext_hex):
    ciphertext = hex_to_bytes(ciphertext_hex)
    blocks = split_blocks(ciphertext, 16)    
    last_block = blocks[-1]
    prev_block = bytearray(blocks[-2])  
    plaintext = bytearray(16) 
```
Después, se hace un bucle que  recorre las posiciones de los bytes a descifrar del último byte (15) hasta el primer byte (0). Dentro se hace un bucle interno probando los 256 valores que puede tomar el byte en cada índice,despues se manda al servidor para obtener una respuesta que diferencia entre un padding valido y uno invalido, luego se usa XOR entre valor interno y bloque previo.

