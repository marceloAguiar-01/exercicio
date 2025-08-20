'''
D042: Comparação entre dois números (maior, menor ou iguais).
 • Leia dois números inteiros e mostre uma das seguintes mensagens:
 • "O primeiro valor é maior"
 • "O segundo valor é maior"
 • "Não existe valor maior, os dois são iguais"
'''

professor = 'MICHALES CAMURÇA'
data = '20/08/2025'
aluno = 'Marcelo Aguiar de Barros'
atividade = 'D002-📅 Desafio 2: Data de Nascimento Formatada'
print('CETAM - CENTRO DE EDUCAÇÃO TECNOLÓGICA DO AMAZONAS')
print('CURSO: DESENVOLVIMENTO DE SISTEMA')
print('COMPONENTE: LINGUAGEM DE PROGRAMAÇÃO')
print('DATA: ',data, )
print('PROFESSOR:', professor)
print('ALUNO: ', aluno, )
print('ATIVIDADE: ',atividade, )


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

print('=='*30)

print('Comparação entre dois números (maior, menor ou iguais)')

print ('==' * 30)

numero = int(input('Digite o primeiro número inteiro: '))
numero2 = int(input('Digite o segundo número inteiro: '))
print('--'*30)
if numero > numero2:
    print(f'{negrito}O primeiro valor ({numero}) é maior que o segundo ({numero2}).{reset}')
elif numero < numero2:
    print(f'{negrito}O segundo valor ({numero2}) é maior que o primeiro ({numero}).{reset}')
else:
    print(f'{negrito}Não existe valor maior, os dois são iguais ({numero}).{reset}')


