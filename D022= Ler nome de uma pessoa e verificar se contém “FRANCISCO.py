# 👤 D022 — Ler nome de uma pessoa e verificar se contém “FRANCISCO".

professor = 'MICHALES CAMURÇA'
data = '15/08/2025'
aluno = 'Marcelo Aguiar de Barros'
atividade = ' D022 — Ler nome de uma pessoa e verificar se contém “FRANCISCO".'

print('\nCETAM - CENTRO DE EDUCAÇÃO TECNOLÓGICA DO AMAZONAS')
print('CURSO: DESENVOLVIMENTO DE SISTEMA')
print('COMPONENTE: LINGUAGEM DE PROGRAMAÇÃO')
print('DATA: ',data, )
print('PROFESSOR:', professor)
print('ALUNO: ', aluno, )
print('ATIVIDADE: ',atividade, )




frase = input("Digite um nome: ").upper().strip()
print("A palavra 'FRANCISCO' está na frase?", 'FRANCISCO' in frase)

#COD2
nome = input("Digite um nome: ").upper().strip()
print(nome.startswith("FRANCISCO"))


#COD3
'''
if nome.startswith("SÃO"):
    print("A nome começa com 'FRANCISCO'.")
else:
    print("A nome não começa com 'francisco'.")
'''