

class Code:
    def __init__(self):
        """
        Se precisar faca uso de variáveis.
        """
        pass

    # TODO
    def dest(self, mnemnonic):
        """
        Retorna o código binário do(s) registrador(es) que vão receber o valor da instrução.
        - in mnemnonic: vetor de mnemônicos "instrução" a ser analisada.
        - return bits: String de 4 bits com código em linguagem de máquina
          que define o endereco da operacao

        """
       

            


        # duas entradas
        com_destino = ['leaw', 'movw', 'addw', 'subw', 'rsubw', 'andw', 'orw']
        
        # uma entrada
        solo = ['leaw', 'movw']

        instrucao = mnemnonic[0] 
        bits = "000"
        if instrucao not in com_destino:
            destino =  mnemnonic[-1]
            if destino == '%D':
                bits = '010'
            elif destino == '%A':
                bits = '001'
            elif destino == '(%A)':
                bits = '100'
        else:
            bits =''
            if instrucao in solo:
                destinos = mnemnonic[2:]
            else:
                destinos = mnemnonic[3:]
            if '(%A)' in destinos:
                bits += '1'
            else:
                bits += '0'
            if '%D' in destinos:
                bits += '1'
            else:
                bits += '0'
            if '%A' in destinos:
                bits += '1'
            else:
                bits += '0'

        return bits

    # TODO
    def comp(self, mnemnonic):
        """
        Retorna o código binário do mnemônico para realizar uma operação de cálculo.
        - in mnemnonic: vetor de mnemônicos "instrução" a ser analisada.
        - return bits:  Opcode (String de 7 bits) com código em linguagem de máquina para a instrução.
        """
        # duas entradas
        duas_entradas = [ 'addw', 'subw', 'rsubw', 'andw', 'orw']
        
        if len(mnemnonic) == 1:
            return '0001100'
            
        instrucao = mnemnonic[0]
        afetado = mnemnonic[1]

        if instrucao not in duas_entradas:  
            # incw
            # decw
            # notw
            # negw
            # movw
            # leaw - nao convem
            if '$' in afetado:
                bits = '0'
                if afetado == '$0':
                    bits += '101010'
                elif afetado == '$1':
                    bits += '111111'
                else:
                    bits += '111010'
            else:
                if afetado == '%D':
                    if instrucao == 'incw': 
                        bits = '00111'
                    else:
                        bits = '00011'
                else: 
                    if afetado == '%A':
                        bits = '0110'
                    else:
                        bits = '1110'
                    if instrucao == 'incw':
                        bits += '1'
                    else:
                        bits += '0'
                if instrucao == 'movw':
                    bits += '00'
                elif instrucao == 'notw':
                    bits += '01'
                elif instrucao == 'negw' or instrucao == 'incw':
                    bits += '11'
                elif instrucao == 'decw':
                    bits += '10'
        else:
            # addw
            # subw
            # rsubw
            # andw
            # orw
            afetados = mnemnonic[1:3]
            if '(%A)' in afetados:
                bits = '10'
            else:
                bits = '00'
            
            if instrucao == 'andw':
                bits += '00000'
            elif instrucao == 'orw':
                bits += '10101'
            else:
                if '$' not in afetados[0] and '$' not in afetados[1]:
                    if instrucao == 'addw' :
                        bits += '00010'
                    elif afetados[0] == '%D' and instrucao!='rsubw':
                        bits += '10011'
                    else:
                        bits += '00111'
                else:
                    if (instrucao == 'addw' and '$1' in afetados) or (instrucao=='subw' and afetados[1] == '$-1') or (instrucao=='rsubw' and afetados[0] == '$-1'):
                        if '%D' in afetados:
                            bits = '0011111'
                        elif '(%A)' in afetados:
                            bits = '1110111'
                        else:
                            bits = '0110111'
                    else:
                        if '%D' in afetados:
                            bits = '0001110'
                        elif '(%A)' in afetados:
                            bits = '1110010'
                        else:
                            bits = '0110010'
                            
        return bits

    # TODO
    def jump(self, mnemnonic):
        """
        Retorna o código binário do mnemônico para realizar uma operação de jump (salto).
        - in mnemnonic: vetor de mnemônicos "instrução" a ser analisada.
        - return bits: (String de 3 bits) com código em linguagem de máquina para a instrução.
        """
        bits = "000"
        for i in mnemnonic:
            if i == "jmp":
                bits = "111"
            elif i == "je":
                bits = "010"
            elif i == "jne":
                bits = "101"
            elif i == "jg":
                bits = "001"
            elif i == "jge":
                bits = "011"
            elif i == "jl":
                bits = "100"
            elif i == "jle":
                bits = "110"
            else:
                bits = "000"
        return bits

    # DONE
    def toBinary(self, value):
        """
        Converte um valor inteiro para binário 16 bits.
        """
        return f"{int(value):016b}"
