import socket
import descryptor
import argparse
import binascii
import attacker
import attacker_e


# We connect to a (host,port) tuple
import utils.utils as utils

CONNECTION_ADDR = ("cc5327.hackerlab.cl", 5312)


def case_1():
    print("Parte a!!")
    print("Enviando mensajes de distinto tamaño al servidor A")
    sock_input, sock_output = utils.create_socket(CONNECTION_ADDR)
    msg1 = "1234567890"
    msg2 = "123456789"
    msg3 = "12345678"
    msg4 = "1"
    try:
        
        for msg in [msg1, msg2, msg3,msg4]:
            print("[Client] \"{}\"".format(msg))
            resp = utils.send_message(sock_input, sock_output, msg)
            print("[Server] \"{}\"".format(resp))
        
    except Exception as e:
        print(e)
        print("Closing...")
        sock_input.close()
    print("Los resultados de esta prueba se detallan en el readme")
    print()
    print("-------------------------------------------------------------------")
    print()
    print("Probando ahora con 12345678 y 1234567a")
    print("Enviando mensaje al servidor A")
    M1a = utils.send_message(sock_input, sock_output, "12345678")
    print("[Server] \"{}\"".format(M1a))
    print()
    M1b = utils.send_message(sock_input, sock_output, "1234567a")
    print("[Server] \"{}\"".format(M1b))
    print()
    print("Los resultados de esta prueba se detallan en el readme parte a")
    print("-------------------------------------------------------------------")
    print()
    print("Cambiando un bit del mensaje cifrado:")
    print("Probando con 12345678")
    print()
    print("Enviando mensaje al servidor A")
    M2 = utils.send_message(sock_input, sock_output, "12345678")
    print("La cadena cifrada es: ", M2)
    print()
    print("Modificando el un byte del mensaje cifrado")
    M2_a = utils.hex_to_bytes(M2)
    M2_a[40] = 0x58
    M2_b = utils.bytes_to_hex(M2_a)
    print("Mensaje modificado: ", M2_b)
    print()
    print("Enviando mensaje al servidor B")
    sock_input, sock_output = utils.create_socket(("cc5327.hackerlab.cl", 5313))
    print("[Client] \"{}\"".format(M2_b))
    respB = utils.send_message(sock_input, sock_output, M2_b)
    print("[Server] \"{}\"".format(respB))
    print()
    print("Nuevamente, los resultados de esta prueba se detallan en el readme")
    print()
    print("-------------------------------------------------------------------")
    print()
    print("Ahora modificando algun byte del ultimo bloque (es decir de padding)")
    print("Primero, el texto cifrado de 12345678 es: ", M2)
    M2_c = utils.hex_to_bytes(M2)
    M2_c[100] = 0x30
    M2_c = utils.bytes_to_hex(M2_c)
    print("El texto cambiado con byte de padding: ", M2_c)
    print()
    print("Enviando mensaje al servidor B")
    print("[Client] \"{}\"".format(M2_c))
    respBc = utils.send_message(sock_input, sock_output, M2_c)
    print("[Server] \"{}\"".format(respBc))
    print()
    print("Los resultados de esta prueba se detallan en el readme parte a")

def case_2():
    print("parte b!!")
    print("Se creo la función dec en el archivo descryptor.py, la cual entrega un mensaje al servidor A y la respuesta al servidor B")
    print()
    descryptor.dec()
    print("Como podemos notar, el mensaje es desencriptado por el servidor B)")


def caso_3():
    print("parte c!!")
    print("Esta parte está explicada en su totalidad en el readme")

def caso_4():
    print("parte d!!")
    print("Esta parte está explicada en el readme, ejecutando la función descrypt_last_byte(Encyrpt_message) de attacker")
    attacker.descrypt_byte("e2a0bb3fe8a4ff55ca8e8c7048a521fe99865dead7dc6d2712a7701bb36bf78b2f8c2f11d97e5d2c051c8eb56b91fe61f5c81ba7b5ba6439aeff3a83d50c94f93c91a8fabd7f68916fca94d2178577e8746430a186275287fbf15fcf11f4a71b38d754c60009b4693ee6ba68d1eb3a0958f0f71db7813b2cf993fb99cfd32f04", 15)

def caso_5():
    print("parte e!!")
    print("En esta parte, se intenta ejecutar con exito la decifración de un bloque completo, con la misma lógica que para la parte anterior")
    print("Pero con un archivo attacker modificado, attacker_e.py")
    print()
    print("Ejecutando la función descrypt_block de attacker_e")
    attacker_e.decrypt_block("e2a0bb3fe8a4ff55ca8e8c7048a521fe99865dead7dc6d2712a7701bb36bf78b2f8c2f11d97e5d2c051c8eb56b91fe61f5c81ba7b5ba6439aeff3a83d50c94f93c91a8fabd7f68916fca94d2178577e8746430a186275287fbf15fcf11f4a71b38d754c60009b4693ee6ba68d1eb3a0958f0f71db7813b2cf993fb99cfd32f04")

    print()
    print()
    print("La explicación de la función se encuentra en el readme")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ejecutar pruebas AES-CBC en terminal")
    parser.add_argument("--case", type=int, help="Número de caso de prueba (1-8)", required=True)
    args = parser.parse_args()

    cases = {
        1: case_1,
        2: case_2,
        3: caso_3,
        4: caso_4,
        5: caso_5,
    }

    if args.case in cases:
        cases[args.case]()
    else:
        print("Opción inválida. Seleccione un número entre 1 y 5.")