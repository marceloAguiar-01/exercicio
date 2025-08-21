from cabecalho import exibir_cabecalho

print('=='*30)
exibir_cabecalho('D049 - Jokenpô contra o computador', '21/08/2025')

from random import choice
from cores import verde, vermelho, reset

print(f'''
Vamos jogar Jokenpô contra o computador!   
1. Pedra
2. Papel
3. Tesoura
''')

jogador = int(input('Escolha sua jogada (1, 2 ou 3): '))
if jogador not in [1, 2, 3]:
    print(f'{vermelho}Opção inválida! Por favor, escolha 1, 2 ou 3.{reset}')

else:
    opcoes = {1: 'Pedra', 2: 'Papel', 3: 'Tesoura'}
    computador = choice([1, 2, 3])

    print(f'Você escolheu: {opcoes[jogador]}')
    print(f'O computador escolheu: {opcoes[computador]}')

    if jogador == computador:
        print(f'{verde}Empate! Ambos escolheram {opcoes[jogador]}.{reset}')

    elif (jogador == 1 and computador == 3) or (jogador == 2 and computador == 1) or (jogador == 3 and computador == 2):
        print(f'{verde}Você venceu!{reset}')
        
    else:
        print(f'{vermelho}Você perdeu!{reset}')