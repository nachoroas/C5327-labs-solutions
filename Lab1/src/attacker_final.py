from utils.utils import create_socket, send_message, hex_to_bytes, bytes_to_hex, split_blocks, join_blocks
from attacker_e import decrypt_block


DESCRYPTOR_ADDR = ("cc5327.hackerlab.cl", 5312)

sock_A_in, sock_A_out = create_socket(DESCRYPTOR_ADDR)

def extract_key():
    ciphertext = send_message(sock_A_in, sock_A_out, "123456789a")  # Servicio A
    blocks = split_blocks(hex_to_bytes(ciphertext), 16)
    
    full_plaintext = bytearray()
    for i in range(1, len(blocks)):
        block_to_decrypt = join_blocks(blocks[:i + 1])
        decrypted_block = decrypt_block(bytes_to_hex(block_to_decrypt))
        full_plaintext.extend(decrypted_block)
    
    key = full_plaintext[1:].decode('latin-1', errors='ignore')
    return key

print("Key obtenida:", extract_key())