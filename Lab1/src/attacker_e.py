from utils.utils import create_socket, send_message, hex_to_bytes, bytes_to_hex, split_blocks, join_blocks

DESCRYPTOR_ADDR = ("cc5327.hackerlab.cl", 5313)

sock_input_descryptor, sock_output_descryptor = create_socket(DESCRYPTOR_ADDR)

Encyrpt_message ="16aebac760873ad97ab6fb251866f83d8caeb4efe85db9c56971c72327b3d0ca6b4c3fec20ce08fd89cbb35fa1e37f9d49c3956df377b3ea7ff7b851ce7eddbb1537662a11b6ff9be58d61bea8cd918fcd695b04439a5c75a2c62de98c238759aa753a3cce3007b2accd365d00d35cc1e1843c92507bc132e71f6d17bf45c3df"


def decrypt_block(ciphertext_hex):
    ciphertext = hex_to_bytes(ciphertext_hex)
    blocks = split_blocks(ciphertext, 16)    
    last_block = blocks[-1]
    prev_block = bytearray(blocks[-2])  
    plaintext = bytearray(16) 

    for byte_pos in range(15, -1, -1): 
        padding_val = 16 - byte_pos
        found = False

        for guess in range(256):

            modified_prev = bytearray(prev_block)
            

            for i in range(byte_pos + 1, 16):
                modified_prev[i] = plaintext[i] ^ padding_val
            
            modified_prev[byte_pos] = guess
            payload = join_blocks(blocks[:-2] + [modified_prev, last_block])
            response = send_message(sock_input_descryptor, sock_output_descryptor, bytes_to_hex(payload))


            if "json:" in response:
                plaintext[byte_pos] = guess ^ padding_val
                print(f"Byte {byte_pos} descifrado: {hex(plaintext[byte_pos])}")
                found = True
                break


        if not found and byte_pos == 15:
            print("[Caso Borde] Forzando detección del último byte de padding...")
            plaintext[byte_pos] = padding_val
            prev_block[byte_pos] = prev_block[byte_pos] ^ plaintext[byte_pos] ^ padding_val
            print(f"Byte {byte_pos} forzado como padding: {hex(padding_val)}")
        elif not found:
            raise ValueError(f"No se pudo descifrar el byte {byte_pos}")


    plaintext_final = bytearray()
    for i in range(16):
        plaintext_final.append(plaintext[i] ^ blocks[-2][i])  
    
    return plaintext_final

if __name__ == "__main__":
    decrypted = decrypt_block(Encyrpt_message)
    print("Plaintext descifrado:", decrypted.decode('utf-8', errors='ignore'))