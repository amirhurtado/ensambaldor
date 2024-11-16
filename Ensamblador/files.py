
def push_str_bin(file: str, info: list):
    with open(file, "w") as f:
        for binary_str in info:
            # Divide la cadena binaria en bloques de 8 bits
            for i in range(0, len(binary_str), 8):
                byte_chunk = binary_str[i:i+8]
                f.write(byte_chunk + '\n')
                
def push_str_bin_quartus(file: str, info: list):
    j = 0
    with open(file, "w") as f:
        for binary_str in info:
            # Divide la cadena binaria en bloques de 8 bits
            for i in range(0, len(binary_str), 8):
                byte_chunk = binary_str[i:i+8]
                f.write(f"@{j}\n{byte_chunk}\n")
                j += 1
                
def push_str_hex(file: str, info: list):
    with open(file, "w") as f:
        for binary_str in info:
            # Divide la cadena binaria en bloques de 8 bits
            for i in range(0, len(binary_str), 8):
                byte_chunk = binary_str[i:i+8]
                binary = int(byte_chunk, 2)
                hex_chunk = hex(binary)
                f.write(hex_chunk[2:] + '\n')
                
                