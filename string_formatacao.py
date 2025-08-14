frase = 'Curso Python Básico'
print(f"A frase '{frase}' tem {len(frase)} caracteres.")
'''
print(len(frase))             # Traz a quantidade de caracteres da frase. espaço tambem conta.
print(frase[6:11])            # Traz os caracteres entre o indice [6] e o [11].
print(frase[9])               # traz o caractere do indice [9].
print(frase[:19])             # traz o caracteres do indice [0] e o indice [19].
print(frase[6:])              # traz o caractere do indice [6] até o ultimo indice da string.
print(frase[6:19:2])          # traz o indice da posição [6] a [19] pulando de 2 em 2.

print(frase.count('o'))       # traz quantas vezer a letra o aparece na string.
print(f'{frase.count('s')}')

print(frase.count('o',0,10))  # traz quantas vezer a letra o aparece na string di indice [0] ao [10].
print(frase)
print(frase.strip())          # remove os espaços do começo e do fim.


print(frase.find('Básico'))   # localiza i indice da string 'C'
print(frase.find('Java'))     # quando não encontra retorna -1

#palavra = frase.split()      # separa e traz como tupla
#print(f'{palavra}')
#print(' '.join(palavra))     # junta

print('Curso' in frase)       # verifica se a palavra digitada existe na string. retorna True
print('curso' in frase)       # verifica se a palavra digitada existe na string. retorna False

print(frase.replace('Python','Android')) # troca a palavra na string

print(frase.lower())          # converte toda frase para minusculo
print(frase.upper())          # converte toda frase para maiusculo
print(frase.capitalize())     # converte apenas a primeira letra da primeira palavra para maiusculo
print(frase.title())          # converte todas as primeiras letras de cada palavra para maiusculo
print(frase.swapcase())       # inverte maiusculos e minusculos
print(frase.strip())          #  remove espaços do começo e do final da frase
print(frase.rstrip())         #  Remove espaços (ou caracteres específicos) à direita
print(frase.lstrip())         #  Remove espaços em branco da esquerda

'''
#texto='''curso 
#basico 
#de 
#python.'''
'''
print(texto.title())
print(frase.isdigit())
print(frase.isalpha())
print(frase.isspace())
print('abc'.isalpha())
print('abc1234'.isalnum())
print(' '.isspace())
'''

#nome = 'Marcelo'
#idade = 33
#print("Meu nome é {} e tenho {} anos.".format(nome, idade))
#print('Meu nome e %s e tenho %d anos,'% (nome, idade))


#palavra=['Curso', 'Python', 'Básico']
palavra = frase.split()      # separa e traz como tupla
print(f'{palavra}')
print(' '.join(palavra)) 