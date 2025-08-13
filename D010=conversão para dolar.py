#D010 – Calcular quantos dólares é possível comprar (cotação: R$3,27)



professor = 'MICHALES CAMURÇA'
data = '08/08/2025'
aluno = 'Marcelo Aguiar de Barros'
atividade = 'D0010-📌 Objetivo:D010 – Calcular quantos dólares é possível comprar (cotação: R$3,27)'

print('CETAM - CENTRO DE EDUCAÇÃO TECNOLÓGICA DO AMAZONAS')
print('CURSO: DESENVOLVIMENTO DE SISTEMA')
print('COMPONENTE: LINGUAGEM DE PROGRAMAÇÃO')
print('DATA: ',data, )
print('PROFESSOR:', professor)
print('ALUNO: ', aluno, )
print('ATIVIDADE: ',atividade, )

#COD1

print('=' * 30)
reais = float(input('Quanto dinheiro você tem em reais? R$ '))
print('=' * 30)

cotacao = 3.27
dolares = reais / cotacao

print(f'Com R$ {reais:.2f} você pode comprar US$ {dolares:.2f} (cotação: R$ {cotacao})')
