from ASMsymbolTable import SymbolTable
from ASMcode import Code
from ASMparser import Parser


class ASM:

    # DONE
    def __init__(self, nasm, hack):
        self.hack = hack
        self.symbolTable = SymbolTable()
        self.parser = Parser(nasm)
        self.code = Code()

    # DONE
    def run(self):
        # try:
        self.fillSymbolTable()
        self.generateMachineCode()
        return 0
        # except:
        #     print("--> ERRO AO TRADUZIR: {}".format(self.parser.currentLine))
        #     return -1

    # TODO
    def fillSymbolTable(self):
        """
        primeiro passo para a construção da tabela de símbolos de marcadores (labels)
        varre o código em busca de novos Labels e Endereços de memórias (variáveis)
        e atualiza a tabela de símbolos com os endereços (table).

        Dependencia : Parser, SymbolTable
        """
        while self.parser.advanced():
            if self.parser.commandType() == "L_COMMAND":
                self.symbolTable.addEntry(self.parser.label(), self.parser.currentLine)


        

    # TODO
    def generateMachineCode(self):
        """
        Segundo passo para a geração do código de máquina
        Varre o código em busca de instruções do tipo A, C
        gerando a linguagem de máquina a partir do parse das instruções.

        Dependencias : Parser, Code
        """
        self.parser.lineNumber = 0
        self.parser.currentCommand = ''
        self.parser.file = open('test_assets/factorial.nasm', 'r')

        while self.parser.advanced():

            mnemnonic = self.parser.currentCommand
            print(mnemnonic, 'AAAAAAAAAA')
            if self.parser.commandType() == "C_COMMAND":
                if mnemnonic[0] == 'nop':
                    bin ='100001010100000000'
                elif mnemnonic[0][0] == 'j':
                    print(self.code.jump(mnemnonic))
                    bin = '100000011000000' + self.code.jump(mnemnonic) 
                else:
                    bin = "1000" + self.code.comp(mnemnonic) + "0" + self.code.dest(mnemnonic) + self.code.jump(mnemnonic)
                print(bin)
                self.hack.write(bin + "\n")

            elif self.parser.commandType() == "A_COMMAND":
                x = self.symbolTable.getAddress(self.parser.symbol())
                if x == None:
                    bin = "00" + self.code.toBinary(self.parser.symbol())
                else:
                    bin = "00" + self.code.toBinary(x)
                self.hack.write(bin + "\n")


NASM_IN = 'test_assets/factorial.nasm'
HACK_OUT = 'test_assets/factorial_out.hack'
HACK_REF = 'test_assets/factorial.hack'
fNasm = open(NASM_IN, 'r')
fHack = open(HACK_OUT, 'w')
asm = ASM(fNasm, fHack)
asm.run()
fHack.close()