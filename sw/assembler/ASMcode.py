

class Code:
    def __init__(self):
        """
        Se precisar faca uso de variáveis.
        """
        self.table = {}
        self.init()

    # TODO
    def dest(self, mnemnonic):
        """
        Retorna o código binário do(s) registrador(es) que vão receber o valor da instrução.
        - in mnemnonic: vetor de mnemônicos "instrução" a ser analisada.
        - return bits: String de 4 bits com código em linguagem de máquina
          que define o endereco da operacao
        """

        bits = "0000"
        return bits

    # TODO
    def comp(self, mnemnonic):
        """
        Retorna o código binário do mnemônico para realizar uma operação de cálculo.
        - in mnemnonic: vetor de mnemônicos "instrução" a ser analisada.
        - return bits:  Opcode (String de 7 bits) com código em linguagem de máquina para a instrução.
        """

        bits = "000000"
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
