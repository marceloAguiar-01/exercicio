#D025: Verifique se um número digitado é positivo, negativo ou zero.

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



n=float(input('Digite um número para saber se ele é positivo, negativo ou zero: '))

if n < 0:
    print('Este número é negativo!')
elif n > 0:
    print('Este número é positivo!')
else :
    print('Este número é zero!')







#print('Carro novo' if (t := int(input('Quantos anos tem seu carro: '))) <= 3 else 'Seu carro é semi novo' if t <= 5 else 'Carro velho')
