# We connect to a (host,port) tuple
from utils.utils import create_socket, send_message, hex_to_bytes, bytes_to_hex, split_blocks, join_blocks


DESCRYPTOR_ADDR = ("cc5327.hackerlab.cl", 5313)

sock_input_descryptor, sock_output_descryptor = create_socket(DESCRYPTOR_ADDR)

Encyrpt_message = "eb39354a1ac9d959dede7632f96c539cf44acec37911167e7c80aebe5e884882df09e469020a039704ae8668ae319b6086923587c78d42e9fca1cd449d99326deddec47df789a8b1ffb649c874e33ec46b95ad3f6ba93f3ec7709a9470fab427e7762f271da8122af899f4281450573f1a1d9468a4f21b4959ea732813575d97"

def descrypt_last_byte(message):
    """
    This function is used to descrypt the last byte of a message.
    :param message: the message to descrypt
    """
    bytes_array=split_blocks(hex_to_bytes(message),16)
    current_block=bytes_array[len(bytes_array)-1]
    previous_block=bytes_array[len(bytes_array)-2]
    previous_block_mod=bytearray(previous_block)
    for i in range(256):
        print("[Server:5313] Trying byte: {}".format(i))
        previous_block_mod[15]=i
        final_message=join_blocks(bytes_array[:-2]+[previous_block_mod,current_block])
        try:
            descrypt = send_message(sock_input_descryptor,sock_output_descryptor , bytes_to_hex(final_message))
            if "pkcs7:" in descrypt:
                continue
            else:
                print("[Server:5313] \"{}\"".format(descrypt))
        except Exception as e:
            print(e)
        
if __name__ == "__main__":
    
    print(descrypt_last_byte(Encyrpt_message))
    print("Done")
            