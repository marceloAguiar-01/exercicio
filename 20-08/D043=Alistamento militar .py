'''
D043: Alistamento militar (ainda vai, na hora ou já passou).
 • Leia o ano de nascimento de um jovem e informe se ele ainda vai se 
alistar, se está na hora de se alistar ou se já passou do tempo.
 • O programa também deve informar quantos anos faltam ou quantos anos 
se passaram do prazo.
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

print('Alistamento militar (ainda vai, na hora ou já passou).')

print ('==' * 30)

ano_nascimento = int(input('Digite o ano de nascimento do jovem: '))
ano_atual = 2025 

idade = ano_atual - ano_nascimento

print('--'*30)

if idade < 18:
    anos_faltando = 18 - idade
    print(f'{negrito}O jovem ainda vai se alistar. Faltam {anos_faltando} anos para o alistamento.{reset}')
elif idade == 18:
    print(f'{negrito}O jovem está na hora de se alistar.{reset}')
else:
    anos_passados = idade - 18
    print(f'{negrito}O jovem já passou do tempo de se alistar. Já se passaram {anos_passados} anos.{reset}')