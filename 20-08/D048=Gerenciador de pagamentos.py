from cabecalho import exibir_cabecalho

exibir_cabecalho('D048: Gerenciador de pagamentos (descontos e juros).', '21/08/2025')

from cores import vermelho, verde, amarelo, fundo_vermelho, reset

preco_produto = float(input('Digite o valor do produto: ').replace(',', '.').strip())


print(f'''
1. À vista (dinheiro/cheque): 10% de desconto
2. À vista no cartão: 5% de desconto
3. Em até 2x no cartão: Preço normal
4. 3x ou mais no cartão: 20% de juros
''')

pagamento = int(input('Selecione a forma de pagamento: '))
print('-'*30)
if pagamento == 1:
    print(f'você escolheu a opção 1!')
    print('-'*30)
    print(f'o valor à vista lhe da 10% de desconto o valor sera de: ${verde}{preco_produto*0.90:.2f}{reset} reais!')
elif pagamento == 2:
    print(f'você escolheu a opção 2!')
    print(f'o valor à vista no cartão lhe  da 5% de desconto o valor sera de: ${verde}{preco_produto*0.95:.2f}{reset} reais!')
elif pagamento == 3:
    print(f'você escolheu a opção 3!')
    print(f'o valor à 2x no cartão e o valor sera de: ${verde}{preco_produto/2:.2f}{reset} reais, por parcela!')
else :
    print(f'você escolheu a opção 4 ')
    print(f'o valor à 3x no cartão tera um acrescimo de 20% e o valor sera de: ${verde}{preco_produto*1.2:.2f} {reset}reais, por parcela!')