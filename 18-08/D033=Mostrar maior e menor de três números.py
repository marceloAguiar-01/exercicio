#📊 D033: Mostrar maior e menor de três números.
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



n1, n2, n3 = map(int, input("Digite três números separados por espaço: ").split())

menor = n1
if n2 < menor:
    menor = n2
elif n3 < menor:
    menor = n3

maior = n1
if n2 > maior:
    maior = n2
elif n3 > maior:
    maior = n3

print(f"O menor número é: {menor}")
print(f"O maior número é: {maior}")
