from cabecalho import exibir_cabecalho

print('=='*30)
exibir_cabecalho('D054= Promoção de loja', '21/08/2025')
print('=='*30)

valor_compra = float(input('Digite o valor total da compra: R$ '))
if valor_compra > 100:
    desconto = valor_compra * 0.10
    valor_final = valor_compra - desconto
    print(f'Parabéns! Você ganhou um desconto de 10%.')
    print(f'Valor final da compra: R$ {valor_final:.2f}')
else:
    print('Desculpe, você não ganhou desconto. Compre acima de R$ 100 para ganhar 10% de desconto.')
    print(f'Valor final da compra: R$ {valor_compra:.2f}')