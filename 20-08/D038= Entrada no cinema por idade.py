'''
D038: Entrada no cinema por idade (maior de 18, autorização, não permitido).
 ▪ Desenvolva um programa que simule a verificação de idade para entrar em um  cinema. 
▪ Ele deve pedir a idade do usuário e verificar se ele pode assistir ao filme
 ▪ (maior de 18 anos) ou se precisa de autorização (entre 12 e 18 anos). 
▪ Use else para indicar que ele não pode assistir.
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


idade = int(input('Digite a sua idade: '))

if idade >= 18:
    print(f'{verde}Você pode entrar no cinema.{reset}')
elif 12 <= idade < 18:
    print(f'{amarelo}Você precisa de autorização para entrar no cinema.{reset}')
else:
    print(f'{vermelho}Você não pode entrar no cinema.{reset}')


