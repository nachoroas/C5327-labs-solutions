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

