# D020 Ler número (0 a 9999) e exibir cada dígito separadamente (unidade, dezena, centena, milhar).


professor = 'MICHALES CAMURÇA'
data = '12/08/2025'
aluno = 'Marcelo Aguiar de Barros'
atividade = '''D020 Ler número (0 a 9999) e exibir 
            cada dígito separadamente 
            (unidade, dezena, centena, milhar).'''

print('\nCETAM - CENTRO DE EDUCAÇÃO TECNOLÓGICA DO AMAZONAS')
print('CURSO: DESENVOLVIMENTO DE SISTEMA')
print('COMPONENTE: LINGUAGEM DE PROGRAMAÇÃO')
print('DATA: ',data, )
print('PROFESSOR:', professor)
print('ALUNO: ', aluno, )
print('ATIVIDADE: ',atividade, )


num = int(input("Digite um número entre 0 e 9999: "))

# Garante que a string tenha 4 dígitos completando com zeros a esquerda.
#numero = num.zfill(4)

print(f"unidade : {num % 10}")
print(f"dezena  : {num // 10 % 10}")
print(f"centena : {num // 100 % 10}")
print(f"milhares: {num // 1000 % 10}")


