import socket

# We connect to a (host,port) tuple
import utils.utils as utils

CONNECTION_ADDR = ("cc5327.hackerlab.cl", 5312)

if __name__ == "__main__":
    # Parte a :
    # Enviar mensajes de distinto tamaño al servidor A
    sock_input, sock_output = utils.create_socket(CONNECTION_ADDR)
    msg1 = "1234567890"
    msg2 = "123456789"
    msg3 = "12345678"
    msg4 = "1"
    try:
        # You need to use encode() method to send a string as bytes.
        for msg in [msg1, msg2, msg3,msg4]:
            print("[Client] \"{}\"".format(msg))
            resp = utils.send_message(sock_input, sock_output, msg)
            print("[Server] \"{}\"".format(resp))
        # Wait for a response and disconnect.
    except Exception as e:
        print(e)
        print("Closing...")
        sock_input.close()
    
    # Notamos que con 12345678 el largo de la cadena cifrada cambia, y con 1, el largo sigue siendo
    # el mismo que el de 12345678, por ende, la llave debe tener un largo de 7 bytes (si suma 16 entonces cambia)



    
