#D034: Calcular aumento salarial (≤ R$ 1.250 → 15%; senão 10%).
professor = 'MICHALES CAMURÇA'
data = '18/08/2025'
aluno = 'Marcelo Aguiar de Barros'
atividade = 'D002-📅 Desafio 2: Data de Nascimento Formatada'

print('CETAM - CENTRO DE EDUCAÇÃO TECNOLÓGICA DO AMAZONAS')
print('CURSO: DESENVOLVIMENTO DE SISTEMA')
print('COMPONENTE: LINGUAGEM DE PROGRAMAÇÃO')
print('DATA: ',data, )
print('PROFESSOR:', professor)
print('ALUNO: ', aluno, )
print('ATIVIDADE: ',atividade, )



salario=float(input('Digite o salario a ser calculado: '))

if salario <= 1250:
    print(f"O valor do salario que é de:$ {salario} reais, tera um almento de 15% e sera de {salario*1.15:.2f}.")
else :
    print(f"O valor do salario que é de:$ {salario} reais, tera um almento de 10% e sera de {salario*1.10:.2f}.")