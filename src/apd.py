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

class Validar:
    def validarPilha(self, pilha, palavra, transicoes, estadoAtual, estadosFinais, simboloAtualPilha ):
        for letra in palavra:
            for transicao in transicoes:
                if ((transicao[0] == estadoAtual) and (transicao[1] == letra) and (transicao[2] == simboloAtualPilha)):
                    estadoAtual = transicao[3]
                    if(len(transicao[4]) == 2):
                        pilha.append(letra)
                    elif(len(transicao[4]) == 3):
                        pilha.append(letra)
                        pilha.append(letra) 
                    elif ((transicao[4] == '#') and (len(pilha) != 1)):
                        pilha.pop()
                        break   
                    
            simboloAtualPilha = pilha[len(pilha)-1]

        if(estadoAtual in estadosFinais):
            print('SIM')
            pilha = []
        else:
            print('NÃO')
            pilha = []  
 
class Automato:
    def definir(self, json):
        pilha = [] 
        validarPalavra = True
        palavra = input()

        for letra in palavra:
            if letra not in json['ap'][1]:
                validarPalavra = False
        
        if (validarPalavra == True):
            palavra += '#'
            simboloInicialPilha = json['ap'][2][0]
            pilha.append(simboloInicialPilha)
            estadosFinais = json['ap'][5]
            estadoInicial = json['ap'][4]
            simbolosPilha = json['ap'][2]
            transicoes = json['ap'][3]

            simboloAtualPilha = simboloInicialPilha
            estadoAtual = estadoInicial

            validar_apd = Validar()
            validar_apd.validarPilha(pilha, palavra, transicoes, estadoAtual, estadosFinais, simboloAtualPilha)

        else: 
            print('Palavra digitada não é válida.\n')

try:
    if os.path.exists(sys.argv[1]):
        f = open(sys.argv[1])
        data = json.load(f)
        f.close
    else:
        print('Arquivo passado por parâmetro não encontrado.\n')
        sys.exit(0)    

    apd = Automato()

    while 1:  
        apd.definir(data)

except (KeyboardInterrupt) as e:
    sys.exit(0)    
    