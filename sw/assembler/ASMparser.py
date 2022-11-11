import sys


class Parser:
    # DONE
    def __init__(self, inputFile):
        self.file = inputFile  # self.openFile()  # arquivo de leitura
        self.lineNumber = 0  # linha atual do arquivo (nao do codigo gerado)
        self.currentCommand = ""  # comando atual
        self.currentLine = 0  # linha de codigo atual
        self.CommandType = {"A": "A_COMMAND", "C": "C_COMMAND", "L": "L_COMMAND"}
        self.numNop = 0
        self.faltanop = False

    # DONE
    def openFile(self):
        try:
            return open(self.inputFile, "r")
        except IOError:
            sys.exit("Erro: inputFile not found: {}".format(self.inputFile))

    # DONE
    def reset(self):
        self.file.seek(0)

    # DONE
    def close(self):
        self.file.close()

    # TODO
    def advanced(self):
        """
        Carrega uma instrução e avança seu apontador interno para o próxima
        linha do arquivo de entrada. Caso não haja mais linhas no arquivo de
        entrada o método retorna "Falso", senão retorna "Verdadeiro".
        @return Verdadeiro se ainda há instruções, Falso se as instruções terminaram.
        """
        
        if self.lineNumber != 0:
            arquivo = self.file
            self.file = arquivo
        else:
            arquivo = self.file.readlines()
            self.file = arquivo

        variavel = -1
        while arquivo[variavel] == "\n": #or ";" in arquivo[variavel]:
            del arquivo[variavel]
            variavel -= 1

        if self.lineNumber >= len(arquivo):
            return False
        
        self.faltanop = False
        jumps = "jmp je jl jg jle jge"
        jump = arquivo[self.lineNumber].split(";")
        a = jump[0].replace(" ", "").replace("\n", "")
        if jump[0] != "\n" and jump[0] != "" and a[:len(a)-2] in jumps :

            proxima_linha = self.lineNumber
           
            while True:
                proxima_linha += 1
                if arquivo[proxima_linha] == "\n":
                    continue
                if arquivo[proxima_linha].split(";")[0] != "":
                    if "nop" in arquivo[proxima_linha].split(";")[0]:
                        break
                    else:
                        self.faltanop = True
                        self.numNop += 1

                       
                        break


        comComentario = False
        linha_arquivo = self.lineNumber
        for linha in range(linha_arquivo, len(arquivo)):

            if arquivo[linha] == "\n":
                self.lineNumber += 1
            elif ";" in arquivo[linha]:
                self.lineNumber += 1

                
                if arquivo[linha].replace(' ','').split(';')[0] != '' :
                    
                    if ':' not in arquivo[linha]:
                        self.currentLine += 1
                        comComentario = True
                        break

            else:
                if ':' not in arquivo[linha]:
                    self.currentLine += 1
                break
        if comComentario:
            self.lineNumber -= 1
            linha_ = arquivo[self.lineNumber].split(';')[0]

        else:
            linha_ = arquivo[self.lineNumber]
        self.currentCommand = linha_.replace(",", "").split()


        if arquivo[self.lineNumber][-1] == "\n":
            self.lineNumber += 1
            return True
        self.lineNumber += 1
        return True


        # você deve varrer self.file (arquivo já aberto) até encontrar: fim de arquivo
        # ou uma nova instrucao
        # self.file


    # TODO
    def commandType(self):
        """
        Retorna o tipo da instrução passada no argumento:
         - self.commandType['A'] para leaw, por exemplo leaw $1,%A
         - self.commandType['L'] para labels, por exemplo Xyz: , onde Xyz é um símbolo.
         - self.commandType['C'] para todos os outros comandos
        @param  self.currentCommand
        @return o tipo da instrução.
        """
        
      
        # analise o self.currentCommand
        if self.currentCommand[0] == "leaw":
            return self.CommandType["A"]
        elif self.currentCommand[0][-1] == ":" or self.currentCommand[0] == 'constant':
            return self.CommandType["L"]
        else:
            return self.CommandType["C"]
    
    def constant(self):
        return self.currentCommand[2]

    def symbol(self):
            """
            Retorna o símbolo ou valor numérico da instrução passada no argumento.
            Deve ser chamado somente quando commandType() é A_COMMAND.
            @param  command instrução a ser analisada.
            @return somente o símbolo ou o valor número da instrução.
            """

            # analise o self.currentCommand
            if self.commandType() == "A_COMMAND":
                return self.currentCommand[1].replace("$", "")
            elif self.currentCommand[0] == 'constant':
                return self.currentCommand[1].replace("$", "")


    # TODO
    def label(self):
        """
        Retorna o símbolo da instrução passada no argumento.
        Deve ser chamado somente quando commandType() é L_COMMAND.
        @param  command instrução a ser analisada.
        @return o símbolo da instrução (sem os dois pontos).
        
        """
        if self.commandType() == "L_COMMAND":
             return self.currentCommand[0].replace(":", "") 

        # analise o self.currentCommand
        pass
    # DONE
    def command(self):
        return self.currentCommand

    # DONE
    def instruction(self):
        return self.currentCommand
