#D012 – Calcular preço com 5% de desconto



professor = 'MICHALES CAMURÇA'
data = '08/08/2025'
aluno = 'Marcelo Aguiar de Barros'
atividade = 'D0012-📌 Objetivo:D012 – Calcular preço com 5% de desconto'

print('CETAM - CENTRO DE EDUCAÇÃO TECNOLÓGICA DO AMAZONAS')
print('CURSO: DESENVOLVIMENTO DE SISTEMA')
print('COMPONENTE: LINGUAGEM DE PROGRAMAÇÃO')
print('DATA: ',data, )
print('PROFESSOR:', professor)
print('ALUNO: ', aluno, )
print('ATIVIDADE: ',atividade, )

#COD1

print('=' * 30)
preco = float(input('Preço do produto: R$ '))
print('=' * 30)

desconto = preco * 0.05
preco_final = preco - desconto

print(f'Preço original: R$ {preco:.2f}')
print(f'Desconto de 5%: R$ {desconto:.2f}')
print(f'Preço com desconto: R$ {preco_final:.2f}')

