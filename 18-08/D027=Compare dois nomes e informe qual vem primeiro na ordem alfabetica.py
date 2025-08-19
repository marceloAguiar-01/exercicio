# D027: Compare dois nomes e informe qual vem primeiro na ordem alfabética.
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



n1=input('Digite o 1º nome para saber se ele vem primeiro na ordem alfabética: ')
n2=input('Digite o 1º nome para saber se ele vem primeiro na ordem alfabética: ')

if n1 < n2:
    print(f'O nome que vem primeiro é: {n1}')
else :
    print(f'O nome que vem primeiro é: {n2}')