from cabecalho import exibir_cabecalho

print('=='*30)
exibir_cabecalho('D049 - Jokenpô contra o computador', '21/08/2025')
print('=='*30)

numero = int(input('Digite um número entre 10 e 50: '))

if 10 <= numero <= 50:
    print(f'O número {numero} está entre 10 e 50.')
else:
    print(f'O número {numero} não está entre 10 e 50. Por favor, tente novamente.')
