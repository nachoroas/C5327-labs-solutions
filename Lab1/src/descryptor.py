import utils.utils as utils
ENCRYPTOR_ADDR = ("cc5327.hackerlab.cl", 5312)
DESCRYPTOR_ADDR = ("cc5327.hackerlab.cl", 5313)

sock_input_encryptor, sock_output_encryptor= utils.create_socket(ENCRYPTOR_ADDR)

sock_input_descryptor, sock_output_descryptor = utils.create_socket(DESCRYPTOR_ADDR)
def dec():
    try:
        response = input("send a message: ")
        print("[Client] \"{}\"".format(response))
        encrypt = utils.send_message(sock_input_encryptor, sock_output_encryptor, response)
        print("[Server:5312] \"{}\"".format(encrypt))
        print("Changing to descryptor...")
        descrypt = utils.send_message(sock_input_descryptor,sock_output_descryptor , encrypt)
        print("[Server:5313] \"{}\"".format(descrypt))
        print("Closing...")
    except Exception as e:
        print(e)
        print("Closing...")
        input.close()