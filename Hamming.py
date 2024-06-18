def hamming_3126_encode(data):
    """
    Codifica uma mensagem de 26 bits utilizando o Código de Hamming (31,26).
    
    Parâmetros:
    data (list): Lista de 26 bits (0 ou 1)
    
    Retorna:
    list: Lista de 31 bits codificados
    """
    if len(data) != 26:
        raise ValueError("A entrada deve ter 26 bits")
    
    d = data
    
    # Bits de paridade
    p1  = d[0] ^ d[1] ^ d[3] ^ d[4] ^ d[6] ^ d[8] ^ d[10] ^ d[11] ^ d[13] ^ d[15] ^ d[17] ^ d[19] ^ d[21] ^ d[23] ^ d[25]
    p2  = d[0] ^ d[2] ^ d[3] ^ d[5] ^ d[6] ^ d[9] ^ d[10] ^ d[12] ^ d[13] ^ d[16] ^ d[17] ^ d[20] ^ d[21] ^ d[24] ^ d[25]
    p4  = d[1] ^ d[2] ^ d[3] ^ d[7] ^ d[8] ^ d[9] ^ d[10] ^ d[14] ^ d[15] ^ d[16] ^ d[17] ^ d[22] ^ d[23] ^ d[24] ^ d[25]
    p8  = d[4] ^ d[5] ^ d[6] ^ d[7] ^ d[8] ^ d[9] ^ d[10] ^ d[18] ^ d[19] ^ d[20] ^ d[21] ^ d[22] ^ d[23] ^ d[24] ^ d[25]
    p16 = d[11] ^ d[12] ^ d[13] ^ d[14] ^ d[15] ^ d[16] ^ d[17] ^ d[18] ^ d[19] ^ d[20] ^ d[21] ^ d[22] ^ d[23] ^ d[24] ^ d[25]
    
    return [p1, p2, d[0], p4, d[1], d[2], d[3], p8, d[4], d[5], d[6], d[7], d[8], d[9], d[10], p16, d[11], d[12], d[13], d[14], d[15], d[16], d[17], d[18], d[19], d[20], d[21], d[22], d[23], d[24], d[25]]

def hamming_3126_decode(data):
    """
    Decodifica uma mensagem de 31 bits utilizando o Código de Hamming (31,26) e corrige um único erro, se presente.
    
    Parâmetros:
    data (list): Lista de 31 bits (0 ou 1)
    
    Retorna:
    list: Lista de 26 bits decodificados e corrigidos
    """
    if len(data) != 31:
        raise ValueError("A entrada deve ter 31 bits")
    
    p1, p2, d0, p4, d1, d2, d3, p8, d4, d5, d6, d7, d8, d9, d10, p16, d11, d12, d13, d14, d15, d16, d17, d18, d19, d20, d21, d22, d23, d24, d25 = data
    
    p1_calc  = d0 ^ d1 ^ d3 ^ d4 ^ d6 ^ d8 ^ d10 ^ d11 ^ d13 ^ d15 ^ d17 ^ d19 ^ d21 ^ d23 ^ d25
    p2_calc  = d0 ^ d2 ^ d3 ^ d5 ^ d6 ^ d9 ^ d10 ^ d12 ^ d13 ^ d16 ^ d17 ^ d20 ^ d21 ^ d24 ^ d25
    p4_calc  = d1 ^ d2 ^ d3 ^ d7 ^ d8 ^ d9 ^ d10 ^ d14 ^ d15 ^ d16 ^ d17 ^ d22 ^ d23 ^ d24 ^ d25
    p8_calc  = d4 ^ d5 ^ d6 ^ d7 ^ d8 ^ d9 ^ d10 ^ d18 ^ d19 ^ d20 ^ d21 ^ d22 ^ d23 ^ d24 ^ d25
    p16_calc = d11 ^ d12 ^ d13 ^ d14 ^ d15 ^ d16 ^ d17 ^ d18 ^ d19 ^ d20 ^ d21 ^ d22 ^ d23 ^ d24 ^ d25
    
    error_pos = (p1 != p1_calc) * 1 + (p2 != p2_calc) * 2 + (p4 != p4_calc) * 4 + (p8 != p8_calc) * 8 + (p16 != p16_calc) * 16
    
    if error_pos != 0:
        print(f"Erro detectado na posição {error_pos}, corrigindo...")
        data[error_pos - 1] ^= 1
    
    return [data[2], data[4], data[5], data[6], data[8], data[9], data[10], data[11], data[12], data[13], data[14], data[16], data[17], data[18], data[19], data[20], data[21], data[22], data[23], data[24], data[25], data[26], data[27], data[28], data[29], data[30]]

def main():
    # Solicitar a entrada do usuário
    entrada = input("Digite uma sequência de bits (até 26 bits): ")
    
    # Verificar se a entrada é válida (contém apenas 0s e 1s)
    if not set(entrada).issubset({'0', '1'}):
        print("Entrada inválida. Por favor, digite apenas 0s e 1s.")
        return
    
    # Completar com zeros à esquerda se a entrada tiver menos de 26 bits
    if len(entrada) < 26:
        entrada = entrada.ljust(26, '0')
    
    # Converter a string de entrada em uma lista de inteiros
    mensagem = [int(bit) for bit in entrada]
    
    # Codificar a mensagem
    codificada = hamming_3126_encode(mensagem)
    print("Mensagem codificada:", codificada)
    
    # Simular a recepção de uma mensagem (possivelmente com erro)
    # Aqui, simplesmente copiamos a mensagem codificada, mas você pode introduzir um erro para testar
    recebida = codificada.copy()
    
    # Exemplo de introdução de um erro na posição 3
    # recebida[2] ^= 1  # Descomente para testar a correção de erros
    
    # Decodificar a mensagem recebida
    decodificada = hamming_3126_decode(recebida)
    print("Mensagem decodificada:", decodificada)

if __name__ == "__main__":
    main()
