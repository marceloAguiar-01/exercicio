# D028: Compare dois nomes e informe qual vem primeiro na ordem alfabética.
professor = 'MICHALES CAMURÇA'
data = '18/08/2025'
aluno = 'Marcelo Aguiar de Barros'
atividade = 'D002-📅 Desafio 2: Data de Nascimento Formatada'

print('CETAM - CENTRO DE EDUCAÇÃO TECNOLÓGICA DO AMAZONAS')
print('CURSO: DESENVOLVIMENTO DE SISTEMA')
print('COMPONENTE: LINGUAGEM DE PROGRAMAÇÃO')
print('DATA: ',data, )
print('PROFESSOR:', professor)
print('ALUNO: ', aluno, )
print('ATIVIDADE: ',atividade, )

import random

numero_sorteado = random.randint(0, 5)
palpite = int(input('Adivinhe o número que estou pensando (entre 0 e 5): '))

if palpite == numero_sorteado:
    print('Parabéns! Você acertou!')
else:
    print(f'Errado! Eu pensei no número {numero_sorteado}.')
