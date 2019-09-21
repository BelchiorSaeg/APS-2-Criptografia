import random

##  Chave de Desencriptação:
chave_dec = random.randrange(1,99)
chave_dec = chave_dec, random.randrange(1,chave_dec)

##   Obs: o termo "Célula" é usado neste algoritmo para designar cada valor de uma lista.

### ---- Funções ----

##   Converte uma lista em String única
def ListToText(text_list): return ''.join(text_list)


##   Pega a quantidade de celula em cada valor e retorna uma letra correspondente
def separador(sep): return random.choice(list("ABCDEFGHIJKLMNO"))


##   Peso que Adiciona Compexibilidade á mensagem criptografada
def complexidade(qntd_celula): return (qntd_celula * int(chave_dec[0]) - int(chave_dec[1]))


##   Remove a Complexidade
def descomplexar(qntd_celula): return - (qntd_celula * int(chave_dec[0]) - int(chave_dec[1]))


##   Tabela de Valores - Contém o novo valor para cada caractere a ser criptografado
def tabela():
    # |001 = "a" |002 = "b" |003 = "c" |004 = "d" |005 = "e" |006 = "f" |007 = "g" |008 = "h" |009 = "i" |010 = "j" |011 = "k" |012 = "l" |013 = "m" |014 = "n"|
    # |015 = "o" |016 = "p" |017 = "q" |018 = "r" |019 = "s" |020 = "t" |021 = "u" |022 = "v" |023 = "w" |024 = "x" |025 = "y" |026 = "z" |027 = "A" |028 = "B"|
    # |029 = "C" |030 = "D" |031 = "E" |032 = "F" |033 = "G" |034 = "H" |035 = "I" |036 = "J" |037 = "K" |038 = "L" |039 = "M" |040 = "N" |041 = "O" |042 = "P"|
    # |043 = "Q" |044 = "R" |045 = "S" |046 = "T" |047 = "U" |048 = "V" |049 = "W" |050 = "X" |051 = "Y" |052 = "Z" |053 = " " |054 = "-" |055 = "_" |056 = "+"|
    # |057 = "=" |058 = ")" |059 = "(" |060 = "*" |061 = "%" |062 = "#" |063 = "@" |064 = "!" |065 = "'" |066 = "[" |067 = "]" |068 = "{" |069 = "}" |070 = "ã"|
    # |071 = "Ã" |072 = "ô" |073 = "Ô" |074 = "é" |075 = "É" |076 = "á" |077 = "Á" |078 = "à" |079 = "À" |080 = "ê" |081 = "Ê" |082 = "Ç" |083 = "ç" |084 = "&"|
    # |085 = "º" |086 = "|" |087 = "," |088 = "." |089 = ";" |090 = ":" |091 = "ó" |092 = "Ó" |093 = "0" |094 = "1" |095 = "2" |096 = "3" |097 = "4" |098 = "5"|
    # |099 = "6" |100 = "7" |101 = "8" |102 = "9" |103 = "<" |104 = ">" |105 = "~" |106 = "$" |107 = "¨" |108 = "/" |109 = "\" |110 = """ |111 = "?" |

    c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
         31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42,
         43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
         71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82,
         83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107,
         108, 109, 110, 111]
    d = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
         "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
         "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " ", "-", "_", "+", "=", ")", "(", "*", "%", "#",
         "@", "!", "'", "[", "]", "{", "}", "ã", "Ã", "ô", "Ô", "é", "É", "á", "Á", "à", "À", "ê",
         "Ê", "Ç", "ç", "&", "º", "|", ",", ".", ";", ":", "ó", "Ó", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
         "<", ">", "~", "$", "¨", "/", "\\", '"', "?"]

    return c, d


##   Pega cada letra/simbolo (celula) escrito na msg_original e atribuí um novo valor com base na Tabela de Valores
def converter_tabela(celula):
    c, d = tabela()

    if celula in d: return c[d.index(celula)]
    return 0


##   Tabela de Valores - Descriptografa os algarismos
def decrypter(celula):
    c, d = tabela()

    if celula in c: return d[c.index(celula)]
    return ""


##   Processo de Criptografar
def Criptografar(msg):

    # Variáveis
    n_celula    = len(msg)
    msg_crypted = []

    # Processamento
    for x in msg:
        valor_final = str(converter_tabela(x) + complexidade(n_celula))
        msg_crypted.append(valor_final + separador(valor_final))
        n_celula = n_celula - 1

    ##   Separação da mensagem Criptografada em bytes (Processo Independente e meramente estético, se apagado, não alterará a estrutura do script)

    # Váriáveis:
    msg_bytes                   = []
    qntd_algarismo              = 0


    # Processamento
    for x in (list(ListToText(msg_crypted))):

        qntd_algarismo          = qntd_algarismo + 1
    
        if qntd_algarismo > 8:
            qntd_algarismo      = 0
            msg_bytes           = msg_bytes + [" "] + [x]   
        else:     
            msg_bytes           = msg_bytes + [x]
            
    msg_crypted = msg_bytes
    
    ##

    return ListToText(msg_crypted)

    ##  Fim!


##   Processo de Desencriptação da mensagem
def Descriptografar(msg):

    ##  Separa os Algarismos nos valores originais.

    # Váriáveis
    celula_sep  = ""
    msgCryp_sep = []

    # Processo
    for x in msg:

        if x.isalpha():
            msgCryp_sep.append(celula_sep)
            celula_sep = ""

        if x.isnumeric():
            celula_sep = celula_sep + str(x)

    ##   Processo de Desencriptação da mensagem

    # Variáveis
    qntd_celula = len(msgCryp_sep)
    msg_descrypted = []

    # Processamento
    for x in msgCryp_sep:

        if not x.isnumeric(): x = 0

        valor_final = str(int(x) + descomplexar(qntd_celula))
        msg_descrypted.append(decrypter(int(valor_final)))
        qntd_celula = qntd_celula - 1

    ##
        
    return ListToText(msg_descrypted)


### FIM: ---- Funções ----

##  Escolha do Processo
op = input("Digite o numero relativo ao que deseja fazer: \n1 - Criptografar \n2 - Descriptografar \n\n")

while op != "1" and op != "2":
    print("\nOpção Invalida!! \n")
    op = input("Digite novamente: ")

## Gera a mensagem Criptografada
if op == "1":
    
    print("\nMensagem Criptografada: \n\n{} ".format(Criptografar(input("\nDigite uma mensagem a ser Criptografada: \n\n"))))

    # Impressão de Chave
    chave_dec = list(chave_dec)
    chave_dec.insert(int(len(chave_dec)//2),"-")
    for x in chave_dec: chave_dec[chave_dec.index(x)] = str(x)
    print("\nSua chave de Desencriptação: ",ListToText(chave_dec))

## Gera a mensagem Descriptografada
elif op == "2":
    
    msg_c    = input("\nDigite uma mensagem a ser Desciptografada: \n\n")

    # Impressão de Chave
    chave_dec = list(input("\nDigite a chave de Desencriptação: \n\n"))
    chave_dec = "".join(chave_dec)
    chave_dec = chave_dec.split("-")

    print("\nMensagem Descriptografada: \n\n{} ".format( Descriptografar(msg_c)) )

