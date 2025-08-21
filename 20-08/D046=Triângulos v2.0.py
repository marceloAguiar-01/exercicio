from cabecalho import exibir_cabecalho

exibir_cabecalho('D046 - Triângulos v2.0 (Equilátero, Isósceles, Escaleno)', '21/08/2025')



# Definindo estilos
reset = '\033[m'      # limpa / padrão
negrito = '\033[1m'
sublinhado = '\033[4m'
inverso = '\033[7m'

# Definindo cores de texto (foreground)
preto = '\033[30m'
vermelho = '\033[31m'
verde = '\033[32m'
amarelo = '\033[33m'
azul = '\033[34m'
magenta = '\033[35m'
ciano = '\033[36m'
branco = '\033[37m'

fundo_vermelho = '\033[41m [m'
fundo_verde = '\033[42m [m'
fundo_roxo = '\033[44m [m'

# Exemplo de uso


a = float(input(f"{verde}Digite o valor da 1ª reta: {reset}"))
b = float(input(f"{verde}Digite o valor da 2ª reta: {reset}"))
c = float(input(f"{verde}Digite o valor da 3ª reta: {reset}"))


if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print(f'{fundo_verde}Os lados são {a}, {b}, {c} e formam um triângulo EQUILÁTERO.{reset}')
    elif a == b or a == c or b == c:
        print(f'{fundo_vermelho}Os lados são {a}, {b}, {c} e formam um triângulo ISÓSCELES.{reset}')
    else:
        print(f'{fundo_roxo}Os lados são {a}, {b}, {c} e formam um triângulo ESCALENO.{reset}')
else:
    print('\033[31m Os valores não formam um triângulo.\033[m')
