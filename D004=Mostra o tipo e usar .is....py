#D004

professor = 'MICHALES CAMURÇA'
data = '07/08/2025'
aluno = 'Marcelo Aguiar de Barros'
atividade = 'D004-📌 Objetivo: Crie um programa que: Leia qualquer valor do teclado Mostre: \n✅ O tipo primitivo \n✅ As informações obtidas com métodos como .is...'


print('CETAM - CENTRO DE EDUCAÇÃO TECNOLÓGICA DO AMAZONAS')
print('CURSO: DESENVOLVIMENTO DE SISTEMA')
print('COMPONENTE: LINGUAGEM DE PROGRAMAÇÃO')
print('DATA: ',data, )
print('PROFESSOR:', professor)
print('ALUNO: ', aluno, )
print('ATIVIDADE: ',atividade, )

#COD1

print('='*20)
n = input('Digite qualquer coisa: ')
print('='*20)
print(f'Seu tipo primitivo é: {type(n)}')
#verifica usando o metodo .is...
print(f'Só tem espaços? {n.isspace()}')
print(f'É um número? {n.isnumeric()}')
print(f'É alfabético? {n.isalpha()}')
print(f'É alfanumérico? {n.isalnum()}')
print(f'Está em maiúsculas? {n.isupper()}')
print(f'Está em minúsculas? {n.islower()}')
print(f'Está capitalizado? {n.istitle()}\n')


#COD2
'''
print('='*20)
n = 8
input('Verificar numeral: 8')
print('='*20)
print(f'Seu tipo primitivo é: {type(n)}')

#verifica usando o metodo .is...
n = str(n)
print(f'Só tem espaços? {n.isspace()}')
print(f'É um número? {n.isnumeric()}')
print(f'É alfabético? {n.isalpha()}')
print(f'É alfanumérico? {n.isalnum()}')
print(f'Está em maiúsculas? {n.isupper()}')
print(f'Está em minúsculas? {n.islower()}')
print(f'Está capitalizado? {n.istitle()}\n')
'''
