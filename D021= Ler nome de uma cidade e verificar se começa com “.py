# D021 Ler nome de uma cidade e verificar se começa com “SÃO"

professor = 'MICHALES CAMURÇA'
data = '15/08/2025'
aluno = 'Marcelo Aguiar de Barros'
atividade = ' D021 Ler nome de uma cidade e verificar se começa com SÃO'

print('\nCETAM - CENTRO DE EDUCAÇÃO TECNOLÓGICA DO AMAZONAS')
print('CURSO: DESENVOLVIMENTO DE SISTEMA')
print('COMPONENTE: LINGUAGEM DE PROGRAMAÇÃO')
print('DATA: ',data, )
print('PROFESSOR:', professor)
print('ALUNO: ', aluno, )
print('ATIVIDADE: ',atividade, )


frase = input("Digite uma cidade: ").upper().strip()
print("A palavra 'FRANCISCO' está na frase?", 'SÃO' in frase)


cidade = input("Digite o nome da cidade: ").upper()
print(cidade.startswith("SÃO"))

'''
cidade = input("\nDigite o nome da cidade: ").strip().upper()


if cidade.startswith("SÃO"):
    print("A cidade começa com 'SÃO'.")
else:
    print("A cidade NÃO começa com 'SÃO'.")

'''