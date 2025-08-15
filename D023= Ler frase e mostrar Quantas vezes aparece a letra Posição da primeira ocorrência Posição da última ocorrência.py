# D023 — Ler frase e mostrar: Quantas vezes aparece a letra ‘A’ Posição da primeira ocorrência Posição da última ocorrência

professor = 'MICHALES CAMURÇA'
data = '15/08/2025'
aluno = 'Marcelo Aguiar de Barros'
atividade = "D023 — Ler frase e mostrar: Quantas vezes aparece a letra ‘A’ Posição da primeira ocorrência Posição da última ocorrência. "

print('\nCETAM - CENTRO DE EDUCAÇÃO TECNOLÓGICA DO AMAZONAS')
print('CURSO: DESENVOLVIMENTO DE SISTEMA')
print('COMPONENTE: LINGUAGEM DE PROGRAMAÇÃO')
print('DATA: ',data, )
print('PROFESSOR:', professor)
print('ALUNO: ', aluno, )
print('ATIVIDADE: ',atividade, )



frase = input("Digite uma frase: ").strip().upper()

quantidade = frase.count('A')
primeira_pos = frase.find('A')
ultima_pos = frase.rfind('A')

print("\nRESULTADO:")
print(f"A letra 'A' aparece {quantidade} vezes.")
print(f"A primeira ocorrência está na posição {primeira_pos}.")
print(f"A última ocorrência está na posição {ultima_pos}.")
