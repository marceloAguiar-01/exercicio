'''
D039: Cinema v2.0 – Proibir menor de 12 desacompanhado.
 • Adicione uma verificação para a entrada de:
 • "menor desacompanhado". 
• Se a idade for menor que 12 anos, 
• informe que a entrada só é permitida com um responsável.
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

idade = int(input('Digite a sua idade: '))

if idade < 12:
    acompanhado = input('Você está acompanhado por um responsável? (sim/não): ').strip().lower()
    if acompanhado == 'não':
        print("\033[41mVocê não pode entrar desacompanhado de um responsável.\033[m]")
    elif acompanhado == 'sim':
        print("\033[42mEntrada liberada.\033[m")
    else:
        print("\033[33mEntrada permitida apenas com responsável.\033[m]")
else:
    print("\033[42m Entrada liberada\033[m")

   


