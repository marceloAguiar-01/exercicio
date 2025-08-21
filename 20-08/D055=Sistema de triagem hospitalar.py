#D055: Sistema de triagem hospitalar:
# Paciente é considerado urgente se: 
#Idade menor que 12 ou maior que 65, ou 
#apresentar febre e pressão alta.

from cabecalho import exibir_cabecalho

print('=='*30)
exibir_cabecalho('D055 - Sistema de triagem hospitalar', '21/08/2025')
print('=='*30)

idade = int(input('Digite a idade do paciente: '))
febre = input('O paciente apresenta febre? (s/n): ').strip().lower()
pressao_alta = input('O paciente apresenta pressão alta? (s/n): ').strip().lower()
febre = febre == 's'
pressao_alta = pressao_alta == 's'
if idade < 12 or idade > 65 or (febre and pressao_alta):
    print('O paciente é considerado urgente.')
else:
    print('O paciente não é considerado urgente.')