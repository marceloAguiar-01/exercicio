#D026: Peça dois números ao usuário e exiba se são iguais ou diferentes.

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



n1=float(input('Digite o 1º números para saber se ele é  iguais ou diferentes a outro: '))
n2=float(input('Digite o 2º números para saber se ele é  iguais ou diferentes a outro: '))

if n1 == n2:
    print('Estes números são iguais!')
else :
    print('Estes números são diferentes!')
