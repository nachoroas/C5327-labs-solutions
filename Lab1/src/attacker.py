# We connect to a (host,port) tuple
from utils.utils import create_socket
from utils.utils import send_message
from utils.utils import hex_to_bytes
from utils.utils import bytes_to_hex
from utils.utils import split_blocks
from utils.utils import join_blocks


DESCRYPTOR_ADDR = ("cc5327.hackerlab.cl", 5313)

sock_input_descryptor, sock_output_descryptor = create_socket(DESCRYPTOR_ADDR)

Encyrpt_message = "fab6254277e630565e3e90070648603a235f5e0adb98a402880489d1acd9b3bfa3c5d883edd7d51be9614cbc5242e1dcb65f6d11c1306026b29f544f0b45bfb4a30220d0fefe03e0fb0b37e5efe042d76feb702ae1f8029e3bd51665a0610fea6dcf40d080d73d982e7cf3d5d996e578"

def descrypt_last_byte(message):
    """
    This function is used to descrypt the last byte of a message.
    :param message: the message to descrypt
    """
    bytes_array=split_blocks(hex_to_bytes(message),16)
    for i in range(0,255):
        bytes_array[len(bytes_array)-2][15]=i
        final_message=join_blocks(bytes_array)
        try:
            descrypt = send_message(sock_input_descryptor,sock_output_descryptor , bytes_to_hex(final_message))
            print("[Server:5313] \"{}\"".format(descrypt))
        except Exception as e:
            print(e)
        
if __name__ == "__main__":
    
    print(descrypt_last_byte(Encyrpt_message))
    print("Closing...")
            