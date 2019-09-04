msg_original        = tuple(input("Digite a Mensagem a ser Criptografada: \n"))
qntd_algarismos     = len(msg_original) # Indica a quantidade de algarismos
indicador_algarismo = 0             # Indica a posição do algarismo a ser convertido
complexbility       = int()               # Peso que Adiciona Compexibilidade á mensagem criptografada
msg_criptografada   = ()                      # Mensagem Criptografada

#   Converte o texto de Tuple para String
def converterTuple(text_tuple): 
    str = ''.join(text_tuple)
    return str


#   Específica a quantidade de Algarismos de cada valor e retorna o resultado em Algarismos pré-definidos
def indicador_qntd_algarismos(tamanho_valor):
    if tamanho_valor == 1: indicador_qntd = "A",
    if tamanho_valor == 2: indicador_qntd = "B",
    if tamanho_valor == 3: indicador_qntd = "C",
    if tamanho_valor == 4: indicador_qntd = "D",
    if tamanho_valor == 5: indicador_qntd = "E",
    if tamanho_valor == 6: indicador_qntd = "F",
    if tamanho_valor == 7: indicador_qntd = "G",
    if tamanho_valor == 8: indicador_qntd = "H",
    if tamanho_valor == 9: indicador_qntd = "I",
    return indicador_qntd

#   Peso que Adiciona Compexibilidade á mensagem criptografada

def complexbility(complexidade):
    complexidade = (qntd_algarismos*2)
    return complexidade

def complexbility_2(complexidade): # Desabilitado
    if complexidade == "ABC": complexidade = " ",
    else: complexidade = () 
    return complexidade


#   Tabela de Valores - Pega cada letra/simbolo (algarismo) escrito na msg_original e atribuí um novo valor

def converter_tabela(algarismo):
    if algarismo == "a": crypted_algarismo = 1
    if algarismo == "b": crypted_algarismo = 2
    if algarismo == "c": crypted_algarismo = 3
    if algarismo == "d": crypted_algarismo = 4
    if algarismo == "e": crypted_algarismo = 5
    if algarismo == "f": crypted_algarismo = 6
    if algarismo == "g": crypted_algarismo = 7
    if algarismo == "h": crypted_algarismo = 8
    if algarismo == "i": crypted_algarismo = 9
    if algarismo == "j": crypted_algarismo = 10
    if algarismo == "k": crypted_algarismo = 11
    if algarismo == "l": crypted_algarismo = 12
    if algarismo == "m": crypted_algarismo = 13
    if algarismo == "n": crypted_algarismo = 14
    if algarismo == "o": crypted_algarismo = 15
    if algarismo == "p": crypted_algarismo = 16
    if algarismo == "q": crypted_algarismo = 17
    if algarismo == "r": crypted_algarismo = 18
    if algarismo == "s": crypted_algarismo = 19
    if algarismo == "t": crypted_algarismo = 20
    if algarismo == "u": crypted_algarismo = 21
    if algarismo == "v": crypted_algarismo = 22
    if algarismo == "w": crypted_algarismo = 23
    if algarismo == "x": crypted_algarismo = 24
    if algarismo == "y": crypted_algarismo = 25
    if algarismo == "z": crypted_algarismo = 26
    if algarismo == "A": crypted_algarismo = 27
    if algarismo == "B": crypted_algarismo = 28
    if algarismo == "C": crypted_algarismo = 29
    if algarismo == "D": crypted_algarismo = 30
    if algarismo == "E": crypted_algarismo = 31
    if algarismo == "F": crypted_algarismo = 32
    if algarismo == "G": crypted_algarismo = 33
    if algarismo == "H": crypted_algarismo = 34
    if algarismo == "I": crypted_algarismo = 35
    if algarismo == "J": crypted_algarismo = 36
    if algarismo == "K": crypted_algarismo = 37
    if algarismo == "L": crypted_algarismo = 38
    if algarismo == "M": crypted_algarismo = 39
    if algarismo == "N": crypted_algarismo = 40
    if algarismo == "O": crypted_algarismo = 41
    if algarismo == "P": crypted_algarismo = 42
    if algarismo == "Q": crypted_algarismo = 43
    if algarismo == "R": crypted_algarismo = 44
    if algarismo == "S": crypted_algarismo = 45
    if algarismo == "T": crypted_algarismo = 46
    if algarismo == "U": crypted_algarismo = 47
    if algarismo == "V": crypted_algarismo = 48
    if algarismo == "W": crypted_algarismo = 49
    if algarismo == "X": crypted_algarismo = 50
    if algarismo == "Y": crypted_algarismo = 51
    if algarismo == "Z": crypted_algarismo = 52
    if algarismo == " ": crypted_algarismo = 53
    if algarismo == "-": crypted_algarismo = 54
    if algarismo == "_": crypted_algarismo = 55
    if algarismo == "+": crypted_algarismo = 56
    if algarismo == "=": crypted_algarismo = 57
    if algarismo == ")": crypted_algarismo = 58
    if algarismo == "(": crypted_algarismo = 59
    if algarismo == "*": crypted_algarismo = 60
    if algarismo == "%": crypted_algarismo = 61
    if algarismo == "#": crypted_algarismo = 62
    if algarismo == "@": crypted_algarismo = 63
    if algarismo == "!": crypted_algarismo = 64
    if algarismo == "'": crypted_algarismo = 65
    if algarismo == "[": crypted_algarismo = 66
    if algarismo == "]": crypted_algarismo = 67
    if algarismo == "{": crypted_algarismo = 68
    if algarismo == "}": crypted_algarismo = 69
    if algarismo == "ã": crypted_algarismo = 70
    if algarismo == "Ã": crypted_algarismo = 71
    if algarismo == "ô": crypted_algarismo = 72
    if algarismo == "Ô": crypted_algarismo = 73
    if algarismo == "é": crypted_algarismo = 74
    if algarismo == "É": crypted_algarismo = 75
    if algarismo == "á": crypted_algarismo = 76
    if algarismo == "Á": crypted_algarismo = 77
    if algarismo == "à": crypted_algarismo = 78
    if algarismo == "À": crypted_algarismo = 79
    if algarismo == "ê": crypted_algarismo = 80
    if algarismo == "Ê": crypted_algarismo = 81
    if algarismo == "Ç": crypted_algarismo = 82
    if algarismo == "ç": crypted_algarismo = 83
    if algarismo == "&": crypted_algarismo = 84
    if algarismo == "º": crypted_algarismo = 85
    if algarismo == "|": crypted_algarismo = 86
    if algarismo == ",": crypted_algarismo = 87
    if algarismo == ".": crypted_algarismo = 88
    if algarismo == ";": crypted_algarismo = 89
    if algarismo == ":": crypted_algarismo = 90
    return crypted_algarismo

#   Processo de Conversão
while qntd_algarismos > 0:
    
    valor_convertido    = (str((converter_tabela(msg_original[indicador_algarismo]))+complexbility(0)),)
    msg_criptografada           = msg_criptografada  +  valor_convertido  +  indicador_qntd_algarismos(len(str(valor_convertido[0]))) + complexbility_2(len(msg_criptografada))

    qntd_algarismos     = qntd_algarismos - 1
    indicador_algarismo = indicador_algarismo + 1    

#   FIM
print (converterTuple(msg_criptografada))
