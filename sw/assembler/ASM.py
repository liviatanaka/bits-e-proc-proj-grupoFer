from .ASMsymbolTable import SymbolTable
from .ASMcode import Code
from .ASMparser import Parser


class ASM:

    # DONE
    def __init__(self, nasm, hack):
        self.hack = hack
        self.symbolTable = SymbolTable()
        self.parser = Parser(nasm)
        self.code = Code()
        self.numConstant = 0

    # DONE
    def run(self):
        try:
            self.fillSymbolTable()
            self.generateMachineCode()
            return 0
        except:
            print("--> ERRO AO TRADUZIR: {}".format(self.parser.currentLine))
            return -1

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
                self.symbolTable.addEntry(self.parser.label(), self.parser.currentLine - self.numConstant + self.parser.numNop) # para consertar o symboltable
                if self.parser.currentCommand[0] == 'constant':
                    self.symbolTable.addEntry(self.parser.symbol(), self.parser.constant())
                    self.numConstant += 1

                
    # TODO
    def generateMachineCode(self):
        """
        Segundo passo para a geração do código de máquina
        Varre o código em busca de instruções do tipo A, C
        gerando a linguagem de máquina a partir do parse das instruções.

        Dependencias : Parser, Code, fillSymbolTable
        """
        self.parser.lineNumber = 0
        self.parser.currentCommand = ''
        self.parser.file = open('test_assets/factorial.nasm', 'r')
        coloca_nop = False
        while self.parser.advanced():
            

            mnemnonic = self.parser.currentCommand
            if self.parser.commandType() == "C_COMMAND":
                if mnemnonic[0] == 'nop' or coloca_nop:
                    bin ='100001010100000000'
                    coloca_nop = False
                elif mnemnonic[0][0] == 'j':
                    if self.parser.faltanop:
                        coloca_nop = True
                    bin = '100000011000000' + self.code.jump(mnemnonic)
            elif self.parser.commandType() == "A_COMMAND":
                x = self.symbolTable.getAddress(self.parser.symbol())
                # print(x)
                # print(self.symbolTable.table)
                
                if x == None:
                    bin = "00" + self.code.toBinary(self.parser.symbol())
                else:
                    bin = "00" + self.code.toBinary(x)
                self.hack.write(bin + "\n")

