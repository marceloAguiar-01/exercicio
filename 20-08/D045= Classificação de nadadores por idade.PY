'''
D045: Classificação de nadadores por idade.
 • Leia o ano de nascimento de um atleta e classifique-o em uma 
categoria de natação de acordo com a idade:
 • Até 9 anos: MIRIM
 • Até 14 anos: INFANTIL
 • Até 19 anos: JÚNIOR
 • Até 25 anos: SÊNIOR
 • Acima de 25 anos: MASTER
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
print('Classificação de nadadores por idade.') 
print ('==' * 30)

ano_nascimento = int(input('Digite o ano de nascimento do atleta: '))
idade = 2025 - ano_nascimento
print('--'*30)

print(f'{negrito}Idade do atleta: {idade} anos{reset}')
print('--'*30)
if idade <= 9:
    print(f'{negrito}Categoria: {azul}MIRIM{reset}')
elif idade >= 10 and idade <= 14:
    print(f'{negrito}Categoria: {verde}INFANTIL{reset}')
elif idade >= 15 and idade <= 19:
    print(f'{negrito}Categoria: {amarelo}JÚNIOR{reset}')
elif idade >= 20 and idade <= 25:
    print(f'{negrito}Categoria: {magenta}SÊNIOR{reset}')
else:
    print(f'{negrito}Categoria: {vermelho}MASTER{reset}')
print('--'*30)

print(f'{negrito}{azul}Obrigado por utilizar o programa!{reset}')
print('--'*30)



