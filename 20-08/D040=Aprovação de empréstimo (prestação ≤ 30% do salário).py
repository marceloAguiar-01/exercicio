'''
D040: Aprovação de empréstimo (prestação ≤ 30% do salário).
 • Crie um programa que aprova ou nega um empréstimo bancário para 
a compra de uma casa.
 • Ele deve perguntar o valor da casa, 
• o salário do comprador 
• em quantos anos ele irá pagar.
 • Calcule o valor da prestação mensal e verifique se ele excede 30% do 
salário. Se exceder, o empréstimo deve ser negado.
'''

professor = 'MICHALES CAMURÇA'
data = '20/08/2025'
aluno = 'Marcelo Aguiar de Barros'
atividade = 'D002-📅 Desafio 2: Data de Nascimento Formatada'
print('CETAM - CENTRO DE EDUCAÇÃO TECNOLÓGICA DO AMAZONAS')
print('CURSO: DESENVOLVIMENTO DE SISTEMA')
print('COMPONENTE: LINGUAGEM DE PROGRAMAÇÃO')
print('DATA: ',data, )
print('PROFESSOR:', professor)
print('ALUNO: ', aluno, )
print('ATIVIDADE: ',atividade, )


# Definindo estilos
reset = '\033[m'      # limpa / padrão
negrito = '\033[1m'
sublinhado = '\033[4m'
inverso = '\033[7m'

# Definindo cores de texto (foreground)
preto = '\033[30m'
vermelho = '\033[31m'
verde = '\033[32m'
amarelo = '\033[33m'
azul = '\033[34m'
magenta = '\033[35m'
ciano = '\033[36m'
branco = '\033[37m'

print('='*30)

print('Calculadora de Empréstimo Bancário')

print('='*30)


print('='*30)
salario = float(input('Informe o salário do comprador: R$ '))
valor_casa = float(input('Informe o valor da casa: R$ '))
anos = int(input('Em quantos anos o empréstimo será pago? '))
print('='*30)
# Cálculo da prestação mensal 
prestacao_mensal = valor_casa / (anos * 12)
# Verifica se o valor da prestação mensal
if prestacao_mensal <= (salario * 0.3):
# Verifica se a prestação mensal é <= 30% do salário
    print(f'{verde}Empréstimo aprovado!{reset}')
    print(f'Valor da prestação mensal: R$ {prestacao_mensal:.2f} x {anos * 12} meses')
else:
    print(f'Valor da prestação mensal: R$ {prestacao_mensal:.2f} x {anos * 12} meses')
    print(f'{vermelho}Empréstimo negado!{reset}')
    print(f'Valor máximo permitido para a prestação: R$ {salario * 0.3:.2f}')






















