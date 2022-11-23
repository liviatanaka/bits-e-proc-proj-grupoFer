#!/usr/bin/env python3
import io
import os
import queue
import uuid


class Code:
    def __init__(self, outFile):
        self.outFile = outFile
        self.counter = 0
        self.vmFileName = None
        self.labelCounter = 0

    # DONE
    def close(self):
        self.outFile.close()

    # DONE
    def updateVmFileName(self, name):
        self.vmFileName = os.path.basename(name).split(".")[0]

    # DONE
    def commandsToFile(self, commands):
        for line in commands:
            self.outFile.write(f"{line}\n")

    # DONE
    def getUniqLabel(self):
        return self.vmFileName + str(self.labelCounter)

    # DONE
    def updateUniqLabel(self):
        self.labelCounter = self.labelCounter + 1

    # DONE
    def writeHead(self, command):
        self.counter = self.counter + 1
        return ";; " + command + " - " + str(self.counter)

    # DONE
    def writeInit(self, bootstrap, isDir):
        commands = []

        if bootstrap or isDir:
            commands.append(self.writeHead("init"))

        if bootstrap:
            commands.append("leaw $256,%A")
            commands.append("movw %A,%D")
            commands.append("leaw $SP,%A")
            commands.append("movw %D,(%A)")

        if isDir:
            commands.append("leaw $Main.main, %A")
            commands.append("jmp")
            commands.append("nop")

        if bootstrap or isDir:
            self.commandsToFile(commands)

# TODO
    def writeLabel(self, label):
        commands = []
        commands.append(self.writeHead("label") + " " + label)
        commands.append(f'{label}:')


        self.commandsToFile(commands)

    # TODO
    def writeGoto(self, label):
        commands = []
        commands.append(self.writeHead("goto") + " " + label)
        
        commands.append(f'leaw ${label}, %A')
        commands.append('jmp')
        commands.append('nop')

    
        self.commandsToFile(commands)

    # TODO
    def writeIf(self, label):
        commands = []
        commands.append(self.writeHead("if") + " " + label)
    
        commands.append("leaw $SP, %A")
        commands.append("movw, (%A), %A")
        commands.append("decw %A")
        commands.append("movw (%A), %D")
        commands.append("leaw $final, %A")
        commands.append("je")
        commands.append("nop")
        
        commands.append('leaw $SP, %A')
        commands.append('movw (%A), %A')
        commands.append('decw %A')
        commands.append('movw %A, %D')
        commands.append('leaw $SP, %A')
        commands.append("movw %D, (%A)")



        commands.append(f'leaw ${label}, %A')
        commands.append('jmp')
        commands.append('nop')
        
        commands.append("final:")
        commands.append('leaw $SP, %A')
        commands.append('movw (%A), %A')
        commands.append('decw %A')
        commands.append('movw %A, %D')
        commands.append('leaw $SP, %A')
        commands.append("movw %D, (%A)")



        # TODO ...
        self.commandsToFile(commands)

    # TODO
    def writeArithmetic(self, command):
        self.updateUniqLabel()
        if len(command) < 2:
            print("instrucão invalida {}".format(command))
        commands = []
        commands.append(self.writeHead(command))

        if command == "add":
            commands.append("leaw $SP, %A")
            commands.append("movw, (%A), %A")
            commands.append("decw %A")
            commands.append("movw (%A), %D")
            commands.append("decw %A")
            commands.append("addw, (%A), %D, %D")
            commands.append("movw %D, (%A)")
            commands.append("incw %A")
            commands.append("movw %A, %D")
            commands.append("leaw $SP, %A")
            commands.append("movw %D, (%A)")

        # TODO
        elif command == "sub": 
            commands.append("leaw $SP, %A")
            commands.append("movw, (%A), %A")
            commands.append("decw %A")
            commands.append("movw (%A), %D")
            commands.append("decw %A")
            commands.append("subw, (%A), %D, %D")
            commands.append("movw %D, (%A)")
            commands.append("incw %A")
            commands.append("movw %A, %D")
            commands.append("leaw $SP, %A")
            commands.append("movw %D, (%A)")
        
        # TODO
        elif command == "or":
            commands.append("leaw $SP, %A")
            commands.append("movw, (%A), %A")
            commands.append("decw %A")
            commands.append("movw (%A), %D")
            commands.append("decw %A")
            commands.append("orw, (%A), %D, %D")
            commands.append("movw %D, (%A)")
            commands.append("incw %A")
            commands.append("movw %A, %D")
            commands.append("leaw $SP, %A")
            commands.append("movw %D, (%A)")
        
        # TODO
        elif command == "and":
            commands.append("leaw $SP, %A")
            commands.append("movw, (%A), %A")
            commands.append("decw %A")
            commands.append("movw (%A), %D")
            commands.append("decw %A")
            commands.append("andw, (%A), %D, %D")
            commands.append("movw %D, (%A)")
            commands.append("incw %A")
            commands.append("movw %A, %D")
            commands.append("leaw $SP, %A")
            commands.append("movw %D, (%A)")
        
        elif command == "not":
            commands.append('leaw $SP, %A')
            commands.append('movw (%A), %A')
            commands.append('decw %A')
            commands.append('movw (%A), %D')
            commands.append('notw %D')
            commands.append('movw %D, (%A)')

        elif command == "neg":
            commands.append('leaw $SP, %A')
            commands.append('movw (%A), %A')
            commands.append('decw %A')
            commands.append('movw (%A), %D')
            commands.append('negw %D')
            commands.append('movw %D, (%A)')
        
        elif command == "eq":
            endereco1 = self.getUniqLabel()
            
            commands.append("leaw $SP, %A")
            commands.append("movw (%A), %D")
            commands.append("decw %D")
            commands.append("decw %D")
            commands.append("movw %D, %A")
            commands.append("movw (%A), %A")
            commands.append("movw %A, %D")
            commands.append("leaw $SP, %A")
            commands.append("movw (%A), %A")
            commands.append("subw %A, $1, %A")
            commands.append("movw (%A), %A")
            commands.append("subw %D, %A, %D")
            commands.append("leaw $" + str(endereco1) + ", %A")
            commands.append("je")
            commands.append("nop")
            commands.append("leaw $SP, %A")
            commands.append("movw, (%A), %D")
            commands.append("decw %D")
            commands.append("decw %D")
            commands.append("movw %D, %A")
            commands.append("movw $0, (%A)")
            commands.append("incw %D")
            commands.append("leaw $SP, %A")
            commands.append("movw %D, (%A)")
            commands.append("leaw $fim, %A")
            commands.append("jmp")
            commands.append("nop")
            
            commands.append(str(endereco1) + ":")
        
            commands.append("leaw $SP, %A")
            commands.append("movw, (%A), %D")
            commands.append("decw %D")
            commands.append("decw %D")
            commands.append("movw %D, %A")
            commands.append("movw $-1, (%A)")
            commands.append("incw %D")
            commands.append("leaw $SP, %A")
            commands.append("movw %D, (%A)")
            commands.append("fim:")
            
            # dica, usar self.getUniqLabel() para obter um label único
        # TODO
        elif command == "gt":
            # dica, usar self.getUniqLabel() para obter um label único
            endereco1 = self.getUniqLabel()
            
            commands.append("leaw $SP, %A")
            commands.append("movw (%A), %D")
            commands.append("decw %D")
            commands.append("decw %D")
            commands.append("movw %D, %A")
            commands.append("movw (%A), %A")
            commands.append("movw %A, %D")
            commands.append("leaw $SP, %A")
            commands.append("movw (%A), %A")
            commands.append("subw %A, $1, %A")
            commands.append("movw (%A), %A")
            commands.append("subw %D, %A, %D")
            commands.append("leaw $" + str(endereco1) + ", %A")
            commands.append("jl")
            commands.append("nop")
            commands.append("leaw $SP, %A")
            commands.append("movw, (%A), %D")
            commands.append("decw %D")
            commands.append("decw %D")
            commands.append("movw %D, %A")
            commands.append("movw $-1, (%A)")
            commands.append("incw %D")
            commands.append("leaw $SP, %A")
            commands.append("movw %D, (%A)")
            commands.append("leaw $fim, %A")
            commands.append("jmp")
            commands.append("nop")

            commands.append(str(endereco1) + ":")
        
            commands.append("leaw $SP, %A")
            commands.append("movw, (%A), %D")
            commands.append("decw %D")
            commands.append("decw %D")
            commands.append("movw %D, %A")
            commands.append("movw $0, (%A)")
            commands.append("incw %D")
            commands.append("leaw $SP, %A")
            commands.append("movw %D, (%A)")
            commands.append("fim:")
        elif command == "lt":
            # dica, usar self.getUniqLabel() para obter um label único
            endereco1 = self.getUniqLabel()
            
            commands.append("leaw $SP, %A")
            commands.append("movw (%A), %D")
            commands.append("decw %D")
            commands.append("decw %D")
            commands.append("movw %D, %A")
            commands.append("movw (%A), %A")
            commands.append("movw %A, %D")
            commands.append("leaw $SP, %A")
            commands.append("movw (%A), %A")
            commands.append("subw %A, $1, %A")
            commands.append("movw (%A), %A")
            commands.append("subw %D, %A, %D")
            commands.append("leaw $" + str(endereco1) + ", %A")
            commands.append("jl")
            commands.append("nop")
            commands.append("leaw $SP, %A")
            commands.append("movw, (%A), %D")
            commands.append("decw %D")
            commands.append("decw %D")
            commands.append("movw %D, %A")
            commands.append("movw $0, (%A)")
            commands.append("incw %D")
            commands.append("leaw $SP, %A")
            commands.append("movw %D, (%A)")
            commands.append("leaw $fim, %A")
            commands.append("jmp")
            commands.append("nop")
            
            commands.append(str(endereco1) + ":")
        
            commands.append("leaw $SP, %A")
            commands.append("movw, (%A), %D")
            commands.append("decw %D")
            commands.append("decw %D")
            commands.append("movw %D, %A")
            commands.append("movw $-1, (%A)")
            commands.append("incw %D")
            commands.append("leaw $SP, %A")
            commands.append("movw %D, (%A)")
            commands.append("fim:")

        self.commandsToFile(commands)

    def writePop(self, command, segment, index):
        self.updateUniqLabel()
        commands = []
        commands.append(self.writeHead(command) + " " + segment + " " + str(index))

        if segment == "" or segment == "constant":
            return False
        # TODO
        elif segment == "local":
            # dica: usar o argumento index (push local 1)
            commands.append(f"leaw ${index}, %A")
            commands.append("movw %A, %D")
            commands.append("leaw $LCL, %A")
            commands.append("movw (%A), %A")
            commands.append("addw %A, %D, %D")
            commands.append("leaw $1, %A")
            commands.append("movw %D, (%A)")

            commands.append("leaw $SP, %A")
            commands.append("movw (%A), %A")
            commands.append("decw %A")
            commands.append("movw (%A), %D")
            commands.append("leaw $LCL, %A")
            commands.append("movw (%A), %A")
            commands.append("movw %D, (%A)")
            
            # atualiza valor de SP
            commands.append("leaw $SP, %A")
            commands.append("movw (%A), %A")
            commands.append("decw %A")
            commands.append("movw %A, %D")
            commands.append("leaw $SP, %A")
            commands.append("movw %D, (%A)")
            
        # TODO
        elif segment == "argument":
            commands.append(f"leaw ${index}, %A")
            commands.append("movw %A, %D")
            commands.append("leaw $ARG, %A")
            commands.append("movw (%A), %A")
            commands.append("addw %A, %D, %D")
            commands.append("leaw $1, %A")
            commands.append("movw %D, (%A)")

            commands.append("leaw $SP, %A")
            commands.append("movw (%A), %A")
            commands.append("decw %A")
            commands.append("movw (%A), %D")
            commands.append("leaw $LCL, %A")
            commands.append("movw (%A), %A")
            commands.append("movw %D, (%A)")
            
            # atualiza valor de SP
            commands.append("leaw $SP, %A")
            commands.append("movw (%A), %A")
            commands.append("decw %A")
            commands.append("movw %A, %D")
            commands.append("leaw $SP, %A")
            commands.append("movw %D, (%A)")

        # TODO
        elif segment == "this":
            commands.append(f"leaw ${index}, %A")
            commands.append("movw %A, %D")
            commands.append("leaw $THIS, %A")
            commands.append("movw (%A), %A")
            commands.append("addw %A, %D, %D")
            commands.append("leaw $1, %A")
            commands.append("movw %D, (%A)")

            commands.append("leaw $SP, %A")
            commands.append("movw (%A), %A")
            commands.append("decw %A")
            commands.append("movw (%A), %D")
            commands.append("leaw $LCL, %A")
            commands.append("movw (%A), %A")
            commands.append("movw %D, (%A)")
            
            # atualiza valor de SP
            commands.append("leaw $SP, %A")
            commands.append("movw (%A), %A")
            commands.append("decw %A")
            commands.append("movw %A, %D")
            commands.append("leaw $SP, %A")
            commands.append("movw %D, (%A)")

        # TODO
        elif segment == "that":
            commands.append(f"leaw ${index}, %A")
            commands.append("movw %A, %D")
            commands.append("leaw $THAT, %A")
            commands.append("movw (%A), %A")
            commands.append("addw %A, %D, %D")
            commands.append("leaw $1, %A")
            commands.append("movw %D, (%A)")

            commands.append("leaw $SP, %A")
            commands.append("movw (%A), %A")
            commands.append("decw %A")
            commands.append("movw (%A), %D")
            commands.append("leaw $LCL, %A")
            commands.append("movw (%A), %A")
            commands.append("movw %D, (%A)")
            
            # atualiza valor de SP
            commands.append("leaw $SP, %A")
            commands.append("movw (%A), %A")
            commands.append("decw %A")
            commands.append("movw %A, %D")
            commands.append("leaw $SP, %A")
            commands.append("movw %D, (%A)")
        
        # TODO
        elif segment == "temp":
            # dica: usar o argumento index (push temp 0)
            commands.append(f"leaw ${index}, %A")
            commands.append("movw %A, %D")
            commands.append("leaw $R5, %A")
            commands.append("addw %A, %D, %D")
            commands.append("movw (%A), %A")
            commands.append("leaw $1, %A")
            commands.append("movw %D, (%A)")

            commands.append("leaw $SP, %A")
            commands.append("movw (%A), %A")
            commands.append("decw %A")
            commands.append("movw (%A), %D")
            commands.append("leaw $LCL, %A")
            commands.append("movw (%A), %A")
            commands.append("movw %D, (%A)")
            
            # atualiza valor de SP
            commands.append("leaw $SP, %A")
            commands.append("movw (%A), %A")
            commands.append("decw %A")
            commands.append("movw %A, %D")
            commands.append("leaw $SP, %A")
            commands.append("movw %D, (%A)")
        
        # TODO
        elif segment == "static":
            commands.append(f"leaw ${index}, %A")
            commands.append("movw %A, %D")
            commands.append("leaw $16, %A")
            commands.append("addw %A, %D, %D")
            commands.append("movw (%A), %A")
            commands.append("leaw $1, %A")
            commands.append("movw %D, (%A)")

            commands.append("leaw $SP, %A")
            commands.append("movw (%A), %A")
            commands.append("decw %A")
            commands.append("movw (%A), %D")
            commands.append("leaw $LCL, %A")
            commands.append("movw (%A), %A")
            commands.append("movw %D, (%A)")
            
            # atualiza valor de SP
            commands.append("leaw $SP, %A")
            commands.append("movw (%A), %A")
            commands.append("decw %A")
            commands.append("movw %A, %D")
            commands.append("leaw $SP, %A")
            commands.append("movw %D, (%A)")

        # TODO    
        elif segment == "pointer":
            commands.append(f"leaw ${index}, %A")
            commands.append("movw %A, %D")
            commands.append("leaw $THIS, %A")
            commands.append("addw %A, %D, %D")
            commands.append("movw (%A), %A")
            commands.append("leaw $1, %A")
            commands.append("movw %D, (%A)")

            commands.append("leaw $SP, %A")
            commands.append("movw (%A), %A")
            commands.append("decw %A")
            commands.append("movw (%A), %D")
            commands.append("leaw $LCL, %A")
            commands.append("movw (%A), %A")
            commands.append("movw %D, (%A)")
            
            # atualiza valor de SP
            commands.append("leaw $SP, %A")
            commands.append("movw (%A), %A")
            commands.append("decw %A")
            commands.append("movw %A, %D")
            commands.append("leaw $SP, %A")
            commands.append("movw %D, (%A)")

        self.commandsToFile(commands)

    def writePush(self, command, segment, index):
        commands = []
        commands.append(self.writeHead(command + " " + segment + " " + str(index)))

        if segment == "constant":
            commands.append(f"leaw ${str(index)}, %A")
            commands.append("movw %A, %D")
            commands.append("leaw $SP, %A")
            commands.append("movw (%A), %A")
            commands.append("movw %D, (%A)")
            commands.append("movw %A, %D")
            commands.append("incw %D")
            commands.append("leaw $SP, %A")
            commands.append("movw %D, (%A)")

            # dica: usar index para saber o valor da consante
            # push constant index
        
        # TODO
        elif segment == "local":
            commands.append(f"leaw ${index}, %A")
            commands.append("movw %A, %D")
            commands.append("leaw $LCL, %A")
            commands.append("movw (%A), %A")
            commands.append("addw %A, %D, %D")
            commands.append("movw %D, %A")
            commands.append("movw (%A), %D")
            commands.append("leaw $SP, %A")
            commands.append("movw (%A), %A")
            commands.append("movw %D, (%A)")
            
            # atualiza valor de SP
            commands.append("incw %A")
            commands.append("movw %A, %D")
            commands.append("leaw $SP, %A")
            commands.append("movw %D, (%A)")
        
        # TODO
        elif segment == "argument":
            commands.append(f"leaw ${index}, %A")
            commands.append("movw %A, %D")
            commands.append("leaw $ARG, %A")
            commands.append("movw (%A), %A")
            commands.append("addw %A, %D, %D")
            commands.append("movw %D, %A")
            commands.append("movw (%A), %D")
            commands.append("leaw $SP, %A")
            commands.append("movw (%A), %A")
            commands.append("movw %D, (%A)")
            
            # atualiza valor de SP
            commands.append("incw %A")
            commands.append("movw %A, %D")
            commands.append("leaw $SP, %A")
            commands.append("movw %D, (%A)")

        # TODO
        elif segment == "this":
            commands.append(f"leaw ${index}, %A")
            commands.append("movw %A, %D")
            commands.append("leaw $THIS, %A")
            commands.append("movw (%A), %A")
            commands.append("addw %A, %D, %D")
            commands.append("movw %D, %A")
            commands.append("movw (%A), %D")
            commands.append("leaw $SP, %A")
            commands.append("movw (%A), %A")
            commands.append("movw %D, (%A)")
            
            # atualiza valor de SP
            commands.append("incw %A")
            commands.append("movw %A, %D")
            commands.append("leaw $SP, %A")
            commands.append("movw %D, (%A)")
        
        # TODO
        elif segment == "that":
            commands.append(f"leaw ${index}, %A")
            commands.append("movw %A, %D")
            commands.append("leaw $THAT, %A")
            commands.append("movw (%A), %A")
            commands.append("addw %A, %D, %D")
            commands.append("movw %D, %A")
            commands.append("movw (%A), %D")
            commands.append("leaw $SP, %A")
            commands.append("movw (%A), %A")
            commands.append("movw %D, (%A)")
            
            # atualiza valor de SP
            commands.append("incw %A")
            commands.append("movw %A, %D")
            commands.append("leaw $SP, %A")
            commands.append("movw %D, (%A)")

        # elif segment == "argument":
        #     pass # TODO

        # TODO
        elif segment == "static":
            commands.append(f"leaw ${index}, %A")
            commands.append("movw %A, %D")
            commands.append("leaw $16, %A")
            commands.append("addw %A, %D, %D")
            commands.append("movw %D, %A")
            commands.append("movw (%A), %D")
            commands.append("leaw $SP, %A")
            commands.append("movw (%A), %A")
            commands.append("movw %D, (%A)")
            
            # atualiza valor de SP
            commands.append("incw %A")
            commands.append("movw %A, %D")
            commands.append("leaw $SP, %A")
            commands.append("movw %D, (%A)")
        
        # TODO
        elif segment == "temp":
            commands.append(f"leaw ${index}, %A")
            commands.append("movw %A, %D")
            commands.append("leaw $R5, %A")
            commands.append("addw %A, %D, %D")
            commands.append("movw %D, %A")
            commands.append("movw (%A), %D")
            commands.append("leaw $SP, %A")
            commands.append("movw (%A), %A")
            commands.append("movw %D, (%A)")
            
            # atualiza valor de SP
            commands.append("incw %A")
            commands.append("movw %A, %D")
            commands.append("leaw $SP, %A")
            commands.append("movw %D, (%A)")
        
        elif segment == "pointer":
            commands.append(f"leaw ${index}, %A")
            commands.append("movw %A, %D")
            commands.append("leaw $THIS, %A")
            commands.append("addw %A, %D, %D")
            commands.append("movw %D, %A")
            commands.append("movw (%A), %D")
            commands.append("leaw $SP, %A")
            commands.append("movw (%A), %A")
            commands.append("movw %D, (%A)")
            
            # atualiza valor de SP
            commands.append("incw %A")
            commands.append("movw %A, %D")
            commands.append("leaw $SP, %A")
            commands.append("movw %D, (%A)")

        self.commandsToFile(commands)

    # TODO
    def writeCall(self, funcName, numArgs):
        commands = []
        commands.append(self.writeHead("call") + " " + funcName + " " + str(numArgs))

        # TODO
        # ...

        # salvando return
        commands.append("leaw $return, %A")
        commands.append("movw %A, %D")
        commands.append("leaw $SP, %A")
        commands.append("movw (%A), %A")
        commands.append("movw %D, (%A)")

        # salvando LCL
        commands.append("leaw $LCL, %A")
        commands.append("movw (%A), %D")
        commands.append("leaw $SP, %A")
        commands.append("movw (%A), %A")
        commands.append("incw %A")
        commands.append("movw %D, (%A)")
        commands.append("movw %A, %D")
        commands.append("leaw $SP, %A")
        commands.append("movw %D, (%A)")

        # salvando ARG
        commands.append("leaw $ARG, %A")
        commands.append("movw (%A), %D")
        commands.append("leaw $SP, %A")
        commands.append("movw (%A), %A")
        commands.append("incw %A")
        commands.append("movw %D, (%A)")
        commands.append("movw %A, %D")
        commands.append("leaw $SP, %A")
        commands.append("movw %D, (%A)")

        # salvando THIS
        commands.append("leaw $THIS, %A")
        commands.append("movw (%A), %D")
        commands.append("leaw $SP, %A")
        commands.append("movw (%A), %A")
        commands.append("incw %A")
        commands.append("movw %D, (%A)")
        commands.append("movw %A, %D")
        commands.append("leaw $SP, %A")
        commands.append("movw %D, (%A)")

        # salvando THAT
        commands.append("leaw $THAT, %A")
        commands.append("movw (%A), %D")
        commands.append("leaw $SP, %A")
        commands.append("movw (%A), %A")
        commands.append("incw %A")
        commands.append("movw %D, (%A)")
        commands.append("movw %A, %D")
        commands.append("leaw $SP, %A")
        commands.append("movw %D, (%A)")

        # salvando LCL - RAM[1]
        commands.append("incw %A")
        commands.append("movw %A, %D")
        commands.append("leaw $LCL, %A")
        commands.append("movw %D, (%A)")
        commands.append("leaw $SP, %A")
        commands.append("movw %D, (%A)")

        # salvando ARG - RAM[2]
        commands.append(f"leaw ${5 +numArgs}, %A")
        commands.append("subw %D, %A, %D")
        commands.append("leaw $ARG, %A")
        commands.append("movw %D, (%A)")

        # chamando a funcao
        commands.append(f"leaw ${funcName}, %A")
        commands.append("jmp")
        commands.append("nop")

        commands.append("return:")


        self.commandsToFile(commands)

    # TODO
    def writeReturn(self):
        commands = []
        commands.append(self.writeHead("return"))

        # TODO
        # ...

        # atualiza o valor: retorno da funcao -> arg0
        commands.append("leaw $SP, %A")
        commands.append("movw (%A), %A")
        commands.append("decw %A")
        commands.append("movw (%A), %D")
        commands.append("leaw $ARG, %A")
        commands.append("movw (%A), %A")
        commands.append("movw %D, (%A)")
        commands.append("addw %A, $1, %D")
        commands.append("leaw $SP, %A") # aumenta o valor do SP
        commands.append("incw, %D")
        commands.append("movw %D, (%A)")


        commands.append("leaw $return, %A")
        commands.append("jmp")
        commands.append("nop")
        
        
        self.commandsToFile(commands)

    # TODO
    def writeFunction(self, funcName, numLocals):
        commands = []
        commands.append(self.writeHead("func") + " " + funcName + " " + str(numLocals))

        # TODO
        # ...
        commands.append(f"{funcName}:")
        commands.append("leaw $LCL, %A")
        commands.append("movw (%A), %A")
        commands.append("movw %A, %D")
        commands.append("leaw $SP, %A")
        commands.append("movw %D, (%A)")
        commands.append(f"leaw ${numLocals}, %A")
        commands.append("addw %A, %D, %D")
        commands.append("leaw $SP, %A")
        commands.append("movw %D, (%A)")

        self.commandsToFile(commands)

# commands.append("")