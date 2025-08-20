'''
D037: Saudações personalizadas por nome: 
▪ Crie um programa que pergunte o nome do usuário. 
▪ O programa deve ter diferentes saudações dependendo do nome inserido.
▪ Utilize if para um nome específico (ex: “Neymar"),
▪ elif para uma lista de nomes comuns, e else para todos os outros nomes.
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


n = int(input('Digite um número: '))
if n > 0:
    print(f'O número {n} é {verde}POSITIVO{reset}.')
elif n < 0:
    print(f'O número {n} é {vermelho}NEGATIVO{reset}.')
else:
    print(f'O número {n} é {amarelo}ZERO{reset}.')