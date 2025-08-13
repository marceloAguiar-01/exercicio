#D007 – Ler duas notas, calcular e mostrar a média (atenção à ordem de precedência)


professor = 'MICHALES CAMURÇA'
data = '08/08/2025'
aluno = 'Marcelo Aguiar de Barros'
atividade = 'D007-📌 Objetivo:D007 – Ler duas notas, calcular e mostrar a média (atenção à ordem de precedência)'


print('CETAM - CENTRO DE EDUCAÇÃO TECNOLÓGICA DO AMAZONAS')
print('CURSO: DESENVOLVIMENTO DE SISTEMA')
print('COMPONENTE: LINGUAGEM DE PROGRAMAÇÃO')
print('DATA: ',data, )
print('PROFESSOR:', professor)
print('ALUNO: ', aluno, )
print('ATIVIDADE: ',atividade, )

#COD1

print('='*20)
nota1 = float(input('Digite a 1º nota: '))
nota2 = float(input('Digite a 2º nota: '))
print('='*20)

media = (nota1+nota2)/2
print('Media das noas é: ',media)


#COD2

'''
nota1 = int(input('Digite a 1ª nota: '))
nota2 = int(input('Digite a 2ª nota: '))

print(f'Média das notas é: {(nota1 + nota2) / 2}')
'''
#COD3
'''
nota1, nota2 = map(int, input('Digite as duas notas separadas por espaço: ').split())
print(f'Media das noas é:{(nota1+nota2)/2} ')
'''
