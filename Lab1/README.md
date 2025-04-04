# Laboratorio 1 
Martín Bahamonde
Martín Rojas

## Preguntas

### a.-

#### Servicio A:
Se probaron los siguientes mensajes.

1234567890abcdef

123456789

12345678

hasta que se vio disminuida la cadena de texto cifrado, bajo el supuesto de que tenemos un bloque de 16 bytes, entonces la clave debe ser de 7 bytes, puesto cuando se agrega un caracter mas, tendríamos 16 bytes lo que aumentaría la cadena cifrada

#### Servicio B:
Para este caso se uso la respuesta de "12345678", dicha respuesta cifrada, la pasamos a bytes usando la funcion hextobytes para poder modificar el ultimo byte y probar mandarselo al servicio B (nuevamente en hex usando la funcion inversa)


### b.- 
Al enviar al servidor B la respuesta de A obtenemos el mensaje inicial cifrado, lo que nos dice que el servidor B reconoce la clave y puede des encriptar, esto nos dice que podríamos intentar enviar mensajes al servidor B de los bits modificados (cifrado modificado) para ver sus respuestas

### c.- 
Para conocer el largo del cifrador se puede enviar un mensaje de largo L_m al cifrador, este enviará una cadena de largo L_c, luego, hay que iterar sumando un caracter de largo al mensaje (L_m) hasta conseguir que el largo de L_c cambie.

Una vez logrado esto, hay que tener en consideración que el encriptador puede añadir una concatenacion al mensaje antes de cifrar, por ende, una vez haya cambiado, podemos saber que estamos con un bloque de solo padding, ahora, hay que ir sumando nuevamente caracteres a L_m hasta que L_c cambie, el número de caracteres sumados en esta iteración final, es el tamaño del bloque.