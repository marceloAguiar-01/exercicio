'''
 D044: Média do aluno (aprovado, recuperação, reprovado).
 • Leia 4 notas de um aluno e calcule a média.
 • Informe a situação do aluno com base na média:
 • Média abaixo de 5.0: REPROVADO
 • Média abaixo 7.0: RECUPERAÇÃO
 • Média 7.0 ou superior: APROVADO
'''

professor = 'MICHALES CAMURÇA'
data = '20/08/2025'
aluno = 'Marcelo Aguiar de Barros'
atividade = 'D002-📅 Desafio 2: Data de Nascimento Formatada'
print('CETAM - CENTRO DE EDUCAÇÃO TECNOLÓGICA DO AMAZONAS')
print('CURSO: DESENVOLVIMENTO DE SISTEMA')
print('COMPONENTE: LINGUAGEM DE PROGRAMAÇÃO')
print('DATA: ',data, )
print('PROFESSOR:', professor)
print('ALUNO: ', aluno, )
print('ATIVIDADE: ',atividade, )


# Definindo estilos
reset = '\033[m'      # limpa / padrão
negrito = '\033[1m'
sublinhado = '\033[4m'
inverso = '\033[7m'

# Definindo cores de texto (foreground)
preto = '\033[30m'
vermelho = '\033[31m'
verde = '\033[32m'
amarelo = '\033[33m'
azul = '\033[34m'
magenta = '\033[35m'
ciano = '\033[36m'
branco = '\033[37m'


print('=='*30)

print('Média do aluno (aprovado, recuperação, reprovado).') 
print ('==' * 30)

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
nota4 = float(input('Digite a quarta nota: '))

media = (nota1 + nota2 + nota3 + nota4) / 4

print('--'*30)
if media >= 7.0:
    print(f'{negrito}Média: {media:.2f} - {verde}APROVADO{reset}')
elif media < 7.0 and media >= 5.0:
    print(f'{negrito}Média: {media:.2f} - {amarelo}RECUPERAÇÃO{reset}')
else:
    print(f'{negrito}Média: {media:.2f} -{verde} REPROVADO{reset}')