'''
 D041: Conversor de bases numéricas (binário, octal, hexadecimal)
 • Leia um número inteiro e permita ao usuário escolher a base de 
conversão (binário, octal ou hexadecimal).
 • Converta o número para a base escolhida.
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

print('Conversor de bases numéricas (binário, octal, hexadecimal)')

print ('==' * 30)

print('--'*30)
numero = int(input('Digite um número inteiro: '))
print('Escolha a base de conversão:')
print('1 - Binário')
print('2 - Octal')
print('3 - Hexadecimal')
print('--'*30)

opcao = int(input('Digite a opção (1/2/3): '))
if opcao == 1:
    print(f'{negrito}O número {numero} em binário é: {bin(numero)[2:]}{reset}')
elif opcao == 2:
    print(f'{negrito}O número {numero} em octal é: {oct(numero)[2:]}{reset}')
elif opcao == 3:
    print(f'{negrito}O número {numero} em hexadecimal é: {hex(numero)[2:].upper()}{reset}')
else:
    print(f'{vermelho}Opção inválida!{reset}')




















