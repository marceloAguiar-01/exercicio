#D019 Ler nome completo e mostrar:

professor = 'MICHALES CAMURÇA'
data = '12/08/2025'
aluno = 'Marcelo Aguiar de Barros'
atividade = '''🎯Desafios Aula 06
            D019 Ler nome completo e mostrar:
            Quantidade de caracteres total 
            Nome em maiúsculas e minúsculas.
            Total de letras (sem espaços)
            Quantidade de letras do ultimo nome'''

print('\nCETAM - CENTRO DE EDUCAÇÃO TECNOLÓGICA DO AMAZONAS')
print('CURSO: DESENVOLVIMENTO DE SISTEMA')
print('COMPONENTE: LINGUAGEM DE PROGRAMAÇÃO')
print('DATA: ',data, )
print('PROFESSOR:', professor)
print('ALUNO: ', aluno, )
print('ATIVIDADE: ',atividade, )


name = input(f'digite seu nome: ')
print(f"A frase '{name}' tem {len(name)} caracteres.")
print(f"Frase em maiúsculas: {name.upper()}")
print(f"Nome completo em minúsculo: {name.lower()}")

remover_espacos = name.replace(' ', '')
print(f"Quantidade de letras (sem espaços): {len(remover_espacos)}")

tupla=name.split()
ultimo_nome = tupla[-1]
print(f"Seu último nome tem: {len(ultimo_nome)} letras.")