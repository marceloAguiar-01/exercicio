#D006 – Ler um número e mostrar dobro, triplo e raiz quadrada

professor = 'MICHALES CAMURÇA'
data = '08/08/2025'
aluno = 'Marcelo Aguiar de Barros'
atividade = 'D006-📌 Objetivo:D006 – Ler um número e mostrar dobro, triplo e raiz quadrada'


print('CETAM - CENTRO DE EDUCAÇÃO TECNOLÓGICA DO AMAZONAS')
print('CURSO: DESENVOLVIMENTO DE SISTEMA')
print('COMPONENTE: LINGUAGEM DE PROGRAMAÇÃO')
print('DATA: ',data, )
print('PROFESSOR:', professor)
print('ALUNO: ', aluno, )
print('ATIVIDADE: ',atividade, )

#COD1

print('='*20)
n = int(input('Digite um numero: '))
print('='*20)

d = n*2
t = n*3
r = n**0.5

print('O dobro de ',n,' é ',d)
print('O triplo ',n,' é ',t)
print('A raiz quadrada ',n,' é ',r)

#COD2
'''
print('='*20)
n = int(input('Digite um numero: '))
print('='*20)

print(f'O dobro de {n} é {n*2}')
print(f'O triplo de {n} é {n*3}')
print(f'O raiz quadrada de {n} é {n**0.5}')
'''

