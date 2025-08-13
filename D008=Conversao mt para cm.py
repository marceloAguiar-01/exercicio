#D008 – Converter metros em centímetros e milímetros



professor = 'MICHALES CAMURÇA'
data = '08/08/2025'
aluno = 'Marcelo Aguiar de Barros'
atividade = 'D008-📌 Objetivo:D008 – Converter metros em centímetros e milímetros'


print('CETAM - CENTRO DE EDUCAÇÃO TECNOLÓGICA DO AMAZONAS')
print('CURSO: DESENVOLVIMENTO DE SISTEMA')
print('COMPONENTE: LINGUAGEM DE PROGRAMAÇÃO')
print('DATA: ',data, )
print('PROFESSOR:', professor)
print('ALUNO: ', aluno, )
print('ATIVIDADE: ',atividade, )

#COD1

print('=' * 30)
metros = float(input('Digite o valor em metros: '))
print('=' * 30)

centimetros = metros * 100
milimetros = metros * 1000

print(f'{metros} metros equivalem a {centimetros} centímetros e {milimetros} milímetros.')

#COD2
'''
print('=' * 30)
metros = float(input('Digite o valor em metros: '))
print('=' * 30)

print(f"{metros:.2f} m = {metros * 100:.0f} cm = {metros * 1000:.0f} mm")
'''
