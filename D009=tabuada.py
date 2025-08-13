#D009 – Mostrar a tabuada (1 a 10) de um número


professor = 'MICHALES CAMURÇA'
data = '08/08/2025'
aluno = 'Marcelo Aguiar de Barros'
atividade = 'D009-📌 Objetivo:D009 – Mostrar a tabuada (1 a 10) de um número'


print('CETAM - CENTRO DE EDUCAÇÃO TECNOLÓGICA DO AMAZONAS')
print('CURSO: DESENVOLVIMENTO DE SISTEMA')
print('COMPONENTE: LINGUAGEM DE PROGRAMAÇÃO')
print('DATA: ',data, )
print('PROFESSOR:', professor)
print('ALUNO: ', aluno, )
print('ATIVIDADE: ',atividade, )

#COD1

print('=' * 30)
num = int(input('Digite um número para ver sua tabuada: '))
print('=' * 30)

print(f'{num} x 1  = {num * 1}')
print(f'{num} x 2  = {num * 2}')
print(f'{num} x 3  = {num * 3}')
print(f'{num} x 4  = {num * 4}')
print(f'{num} x 5  = {num * 5}')
print(f'{num} x 6  = {num * 6}')
print(f'{num} x 7  = {num * 7}')
print(f'{num} x 8  = {num * 8}')
print(f'{num} x 9  = {num * 9}')
print(f'{num} x 10 = {num * 10}')


#COD2
'''
print('=' * 30)
num = int(input('Digite um número para ver sua tabuada: '))
print('=' * 30)

for i in range(1, 11):
    print(f"{num} x {i:2} = {num * i}")
'''
#COD3

'''
print('=' * 30)
num = int(input('Digite um número para ver sua tabuada: '))
print('=' * 30)

i = 1
while i <= 10:
    print(f'{num} x {i:2} = {num * i}')
    i += 1
'''
