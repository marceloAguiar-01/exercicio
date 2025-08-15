# D024 — Ler nome completo e mostrar: Primeiro e último nome separadamente

professor = 'MICHALES CAMURÇA'
data = '15/08/2025'
aluno = 'Marcelo Aguiar de Barros'
atividade = "D024 — Ler nome completo e mostrar: Primeiro e último nome separadamente "

print('\nCETAM - CENTRO DE EDUCAÇÃO TECNOLÓGICA DO AMAZONAS')
print('CURSO: DESENVOLVIMENTO DE SISTEMA')
print('COMPONENTE: LINGUAGEM DE PROGRAMAÇÃO')
print('DATA: ',data, )
print('PROFESSOR:', professor)
print('ALUNO: ', aluno, )
print('ATIVIDADE: ',atividade)


nome_completo = input("Digite seu nome completo: ").strip().split()

primeiro_nome = nome_completo[0]
ultimo_nome = nome_completo[-1]

print("\nRESULTADO:")
print(f"Primeiro nome: {primeiro_nome}")
print(f"Último nome: {ultimo_nome}")
