#D013 – Calcular salário com 15% de aumento



professor = 'MICHALES CAMURÇA'
data = '08/08/2025'
aluno = 'Marcelo Aguiar de Barros'
atividade = 'D0013-📌 Objetivo:D013 – Calcular salário com 15% de aumento'

print('CETAM - CENTRO DE EDUCAÇÃO TECNOLÓGICA DO AMAZONAS')
print('CURSO: DESENVOLVIMENTO DE SISTEMA')
print('COMPONENTE: LINGUAGEM DE PROGRAMAÇÃO')
print('DATA: ',data, )
print('PROFESSOR:', professor)
print('ALUNO: ', aluno, )
print('ATIVIDADE: ',atividade, )

#COD1

print('=' * 30)
salario = float(input('Salário atual: R$ '))
print('=' * 30)

aumento = salario * 0.15
novo_salario = salario + aumento

print(f'Salário atual: R$ {salario:.2f}')
print(f'Aumento de 15%: R$ {aumento:.2f}')
print(f'Novo salário: R$ {novo_salario:.2f}')
