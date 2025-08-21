from cabecalho import exibir_cabecalho

exibir_cabecalho('D047: Cálculo de IMC com classificação.', '21/08/2025')

from cores import vermelho, verde, amarelo, fundo_vermelho, reset


peso = float(input('Digite seu peso para verificar seu \033[1mIMC\033[m: ').replace(',', '.').strip())
altura = float(input('Digite sua altura para verificar seu \033[1mIMC\033[m: ').replace(',', '.').strip())

imc = 2/(altura**2)
print('Seu peso é: ',peso)
print('Sua altura é: ',altura)
print('Seu indice de massa corporal é: ',imc)

if imc < 18.5:
    print(f'{vermelho}Você esta abaixo do peso!{reset}')
elif imc >=18.5 and imc < 25:
    print(f'{verde}Você esta no peso ideal!{reset}')
elif imc >=25 and imc <30:
    print(f'{amarelo}Você esta no sobrepeso!{reset}')
elif imc >=30 and imc <40:
    print(f'{vermelho}Você esta obeso!{reset}')
else:
    print(f'{fundo_vermelho}Você esta com obesidade morbida!{reset}')
