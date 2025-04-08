from utils.utils import create_socket, send_message, hex_to_bytes, bytes_to_hex, split_blocks, join_blocks
import re


DESCRYPTOR_ADDR = ("cc5327.hackerlab.cl", 5313)

sock_input_descryptor, sock_output_descryptor = create_socket(DESCRYPTOR_ADDR)

Encyrpt_message = "e2a0bb3fe8a4ff55ca8e8c7048a521fe99865dead7dc6d2712a7701bb36bf78b2f8c2f11d97e5d2c051c8eb56b91fe61f5c81ba7b5ba6439aeff3a83d50c94f93c91a8fabd7f68916fca94d2178577e8746430a186275287fbf15fcf11f4a71b38d754c60009b4693ee6ba68d1eb3a0958f0f71db7813b2cf993fb99cfd32f04"
#"eb39354a1ac9d959dede7632f96c539cf44acec37911167e7c80aebe5e884882df09e469020a039704ae8668ae319b6086923587c78d42e9fca1cd449d99326deddec47df789a8b1ffb649c874e33ec46b95ad3f6ba93f3ec7709a9470fab427e7762f271da8122af899f4281450573f1a1d9468a4f21b4959ea732813575d97"

def descrypt_byte(message,byte_position):
    """
    This function is used to descrypt the last byte of a message.
    :param message: the message to descrypt
    :param byte_position: the position of the byte to descrypt
    :return: the descrypted message
    """
    bytes_array=split_blocks(hex_to_bytes(message),16)
    current_block=bytes_array[len(bytes_array)-1]
    previous_block=bytes_array[len(bytes_array)-2]
    previous_block_mod=bytearray(previous_block)
    for i in range(256):
        print("[Server:5313] Trying byte: {}".format(i))
        previous_block_mod[byte_position]=i
        final_message=join_blocks(bytes_array[:-2]+[previous_block_mod,current_block])
        try:
            descrypt = send_message(sock_input_descryptor,sock_output_descryptor , bytes_to_hex(final_message))
            if "pkcs7:" in descrypt:
                continue
            if "json:" in descrypt:
                print("[Server:5313] Byte found \"{}\"".format(descrypt))
                return (i)
            else:
                print("[Server:5313] Word found \"{}\"".format(descrypt))
        except Exception as e:
            print(e)
        
if __name__ == "__main__":
    
    previous=descrypt_byte(Encyrpt_message,15)
    print("Done")
        