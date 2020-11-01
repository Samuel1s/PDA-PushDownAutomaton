#*******************************************************************************
#*                      Validar uma palavra dado um APD.                       *
#*-----------------------------------------------------------------------------*
#* @AUTHOR: Samuel Filipe dos Santos.                                          *
#* @TEACHER: Andrei Rimsa.                                                     *
#* @LANGUAGE: Python                                                           *
#* @DISCIPLINE: Autômato de Pilha Determinístico                               *
#* @DATE: 02 de novembro de 2020                                               *
#*******************************************************************************

import json
import sys
import os
 
class AUTOMATO:
    def __init__(self):
        self.stack = []

    def compute(self, parsedData):
        validar = True
        palavra = input('Digite a palavra: ')
        palavra = palavra.rstrip()

        for letra in palavra:
            if letra not in parsedData['ap'][1]:
                validar = False
        
        if (validar == True):
            palavra += '#'
            simboloInicialPilha = parsedData['ap'][2][0]
            self.stack.append(simboloInicialPilha)
            estadosFinais = parsedData['ap'][5]
            estadoInicial = parsedData['ap'][4]
            simbolosPilha = parsedData['ap'][2]
            transicoes = parsedData['ap'][3]

            simboloAtualPilha = simboloInicialPilha
            estadoAtual = estadoInicial
            
            print('Estados\tEntrada\tPilha\tTransições')
            print('{}\t {}\t {}\t ({}, {})'.format(estadoAtual, '_', 'Z', simboloAtualPilha, self.stack))
            for letra in palavra:
                for transicao in transicoes:
                    if ((transicao[0] == estadoAtual) and (transicao[1] == letra) and (transicao[2] == simboloAtualPilha)):
                        estadoAtual = transicao[3]
                        if(len(transicao[4]) == 2):
                            self.stack.append(letra)
                        elif(len(transicao[4]) == 3):
                            self.stack.append(letra)
                            self.stack.append(letra) 
                        elif ((transicao[4] == '#') and (len(self.stack) != 1)):
                            self.stack.pop()
                            break   
                previousStackSymbol = simboloAtualPilha
                simboloAtualPilha = self.stack[len(self.stack)-1]
                print('{}\t {}\t {}\t ({}, {})'.format(estadoAtual, letra, previousStackSymbol, simboloAtualPilha, self.stack))

            if(estadoAtual in estadosFinais):
                print('SIM')
                self.stack = []
            else:
                print('NÃO')
                self.stack = []
        else: 
            print('Palavra digitada não é válida.\n')
def main():
    if os.path.exists(sys.argv[1]):
        f = open(sys.argv[1])
        data = json.load(f)
        f.close
    else:
        print('Arquivo passado por parâmetro não encontrado.\n')
        sys.exit(0)    

    apd = AUTOMATO()

    print('Carregando dados do json passado por parâmetro: ')
    print('--------------------------------------')
    print('Conjunto de estados: ', data['ap'][0])
    print('Alfabeto de símbolos: ', data['ap'][1])
    print('Alfabeto da pilha: ', data['ap'][2])
    print('Lista de Transições:')
    for transicao in data['ap'][3]:
        print('\t', transicao)
    print('Estado inicial: ', data['ap'][4])
    print('Conjunto de estados finais: ', data['ap'][5])
    print('--------------------------------------')
     
    while 1:  
        apd.compute(data)

if __name__ == '__main__':
    try:
        main()
    except (KeyboardInterrupt) as e:
        sys.exit(0)    