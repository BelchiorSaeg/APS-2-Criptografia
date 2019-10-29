# -*- coding: utf-8 -*-
"""
@author: Belchior

"""

import random

##   Obs: o termo "Célula" é usado neste algoritmo para designar cada valor de uma lista
##   (podendo ser uma letra da mensagem original, ou seu valor resultante).

#################################################################################################################

### *** Funções *** ###

#-----------------------------------------------------------------------------------------------------------------
# Limpa tela

def clean(): print("\n" * 45)
    
#-----------------------------------------------------------------------------------------------------------------
# Impõem uma decisão ao usuário

def escolha(cls_1, msg, cls_2):
    
    if cls_1 == "cls": clean()
    print(msg)
    choice = input(">> ")
    if cls_2 == "cls": clean()
    
    return choice

#-----------------------------------------------------------------------------------------------------------------
# Pede Confirmação ao Usuário

def confirmar(cls_1, msg, cls_2):
    
    confirm = "{:.1}".format(escolha(cls_1, msg, cls_2))
    
    if   confirm == "s": return True
    elif confirm == "n": 
        print("Operação Cancelada! \n\n")
        return False
    
    print("Opção Invalida! \n\n")

#-----------------------------------------------------------------------------------------------------------------
# Lê arquivo de Texto e retorna o conteúdo
    
def ler_arquivo(nome):
    
    nome     = nome.replace(".txt", "")
    arquivo  = open(nome + ".txt", 'r')
    conteudo = ""
    
    conteudo = arquivo.readlines()

    arquivo.close()
    return conteudo

#-----------------------------------------------------------------------------------------------------------------
# Escreve um conteúdo em um arquivo de texto

def escrever_arquivo(nome, conteudo):
    
    nome    = nome.replace(".txt", "")
    arquivo = open(nome + ".txt", 'w')
    
    arquivo.writelines(conteudo)
    arquivo.close()

#-----------------------------------------------------------------------------------------------------------------
# Dicionários contendo os valores que cada celula irá assumir


dicio_encript = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14,
 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26, 'A': 27,
 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36, 'K': 37, 'L': 38, 'M': 39, 'N': 40,
 'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46, 'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52, ' ': 53,
 '-': 54, '_': 55, '+': 56, '=': 57, ')': 58, '(': 59, '*': 60, '%': 61, '#': 62, '@': 63, '!': 64, "'": 65, '[': 66,
 ']': 67, '{': 68, '}': 69, 'ã': 70, 'Ã': 71, 'ô': 72, 'Ô': 73, 'é': 74, 'É': 75, 'á': 76, 'Á': 77, 'à': 78, 'À': 79,
 'ê': 80, 'Ê': 81, 'Ç': 82, 'ç': 83, '&': 84, 'º': 85, '|': 86, ',': 87, '.': 88, ';': 89, ':': 90, 'ó': 91, 'Ó': 92,
 '0': 93, '1': 94, '2': 95, '3': 96, '4': 97, '5': 98, '6': 99, '7': 100, '8': 101, '9': 102, '<': 103, '>': 104,
 '~': 105, '$': 106, '¨': 107, '/': 108, '\\': 109, '"': 110, '?': 111}

dicio_decript = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n',
 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z', 27: 'A',
 28: 'B', 29: 'C', 30: 'D', 31: 'E', 32: 'F', 33: 'G', 34: 'H', 35: 'I', 36: 'J', 37: 'K', 38: 'L', 39: 'M', 40: 'N',
 41: 'O', 42: 'P', 43: 'Q', 44: 'R', 45: 'S', 46: 'T', 47: 'U', 48: 'V', 49: 'W', 50: 'X', 51: 'Y', 52: 'Z', 53: ' ',
 54: '-', 55: '_', 56: '+', 57: '=', 58: ')', 59: '(', 60: '*', 61: '%', 62: '#', 63: '@', 64: '!', 65: "'", 66: '[',
 67: ']', 68: '{', 69: '}', 70: 'ã', 71: 'Ã', 72: 'ô', 73: 'Ô', 74: 'é', 75: 'É', 76: 'á', 77: 'Á', 78: 'à', 79: 'À',
 80: 'ê', 81: 'Ê', 82: 'Ç', 83: 'ç', 84: '&', 85: 'º', 86: '|', 87: ',', 88: '.', 89: ';', 90: ':', 91: 'ó', 92: 'Ó',
 93: '0', 94: '1', 95: '2', 96: '3', 97: '4', 98: '5', 99: '6', 100: '7', 101: '8', 102: '9', 103: '<', 104: '>',
 105: '~', 106: '$', 107: '¨', 108: '/', 109: '\\', 110: '"', 111: '?'}

#-----------------------------------------------------------------------------------------------------------------
# Valor que adiciona a complexidade/encriptação à célula
    
def complexidade(n_celula): return (n_celula)# + int(chave_dec[4])) * int(chave_dec[0]) - int(chave_dec[2]))
    
#-----------------------------------------------------------------------------------------------------------------
#   gera a chave de encriptação, exibi e a retorna

def gerar_chave():
        
    #  Geração da Chave:
    key       = list(input("\n\nDigite uma Frase qualquer, quanto maior, mais segura será sua encriptação: \n\n"))
    
    chave_dec = [random.randint(0,999),random.randint(0,999),random.randint(0,999)]

    if key == []: key = list("Frase Padrão")      
    for x in range(0,len(key)): key[x] = dicio_encript[key[x]]
    
        
    #Algarismo 3---
    posic   = len(key)
    soma    = 0
    
    for numero in key:
        soma  = soma + numero * posic
        posic = posic - 1
    while soma > 900: soma = soma / random.randint(1,5)
    
    chave_dec[2] = int( (soma + chave_dec[2]) / 2 )
    
    #Algarismo 2---
    soma = soma / 2

    for numero in range(0,3): soma = soma + (random.choice(key))
    while soma > 900: soma = soma / random.randint(1,5)

    chave_dec[1] = int( (soma + chave_dec[1]) / 2 )

    #Algarismo 1----
    soma = chave_dec[0] + chave_dec[1] + len(key)
    soma = soma / 3
    soma = soma + (random.randint(0,999)+random.randint(0,999)+random.randint(0,999))
    soma = soma / 3
    
    while soma > 900: soma = soma / random.randint(1,5)
    
    chave_dec[0]   = int( (soma + chave_dec[0]) / 2 )


    # Impressão de Chave
    
    chave_dec.insert(1,"-")
    chave_dec.insert(3,"-")
    for x in chave_dec: chave_dec[chave_dec.index(x)] = str(x)
        
    clean()
    print("\nSua chave de Desencriptação: {}\n\n".format("".join(chave_dec)))
        
    return chave_dec
#-----------------------------------------------------------------------------------------------------------------
# converte a msg original na criptografada
    
def criptografar(msg):
    
    msg      = list(msg)
    n_celula = len(msg)
    
    # Gera um novo valor para célula
    for n in range(0, len(msg)):
        
        msg[n]    = dicio_encript[msg[n]] + complexidade(n_celula)
        msg[n]    = str(msg[n]) + "#"
        n_celula -= 1
        
    return "".join(msg)
        
#-----------------------------------------------------------------------------------------------------------------
# converte a msg criptografada na original novamente
    
def descriptografar(msg):
    
    msg      = msg.split("#")
    msg.remove("")
    n_celula = len(msg)
    
    
    for n in range(0, len(msg)):
        
        msg[n]    = int(msg[n]) - complexidade(n_celula)
        
        if msg[n] in dicio_decript: msg[n] = dicio_decript[msg[n]]
        else: msg[n] = "*"
        
        n_celula -= 1
        
    return "".join(msg)

#-----------------------------------------------------------------------------------------------------------------

def menu():

    while 1 > 0:
        print('*******************************************')
        print("1) Criptografar \n2) Descriptografar \n3) Configurações \n4) Cancelar")
        print('*******************************************\n\n')
        
        opcao = escolha("", "Escolha uma Opção", "cls")
        
        if opcao not in ["1", "2", "3", "4"]: print("Opção Invalida!\n\n")
        else: break
    
    if opcao != "4": processo(opcao)

#-----------------------------------------------------------------------------------------------------------------

def processo(opcao):
    
    global chave_dec
    
    if opcao == "1":
        
        msg       = escolha("cls", "Digite uma mensagem a ser Criptografada: ", "cls")
        chave_dec = gerar_chave()
        msg       = criptografar(msg)
    
        print("Mensagem Criptografada gerada!! \n")
        print("-------------------------------------------\n\n\n")
        
        
        escrever_arquivo("cifra", msg)
        
        
    if opcao == "2":
        
        msg = escolha("cls", "Digite a mensagem a ser Descriptografada: ", "cls")
    
        # Recepção da Chave
        while len(chave_dec) != 3:
            
            chave_dec = list(input("\nDigite a chave de Desencriptação: \n\n"))
            chave_dec = "".join(chave_dec)
            chave_dec = chave_dec.split("-")
            clean()
        
        msg = descriptografar(msg)
        
        print("\nMensagem Descriptografada: \n\n{} \n".format(msg))
        print("-------------------------------------------\n\n\n")
    
    if confirmar("", "Deseja Continuar? ", "cls"): menu()

#-----------------------------------------------------------------------------------------------------------------
  
### *** Fim - Funções *** ###

#################################################################################################################

chave_dec = ""

clean()
menu ()
