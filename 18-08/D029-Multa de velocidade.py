# D029: Multa de velocidade (> 80 km/h → R$ 7 por km acima)
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


velocidade_limite = 80
multa = 7.00

velocidade_veiculo = int(input('Digite a velocidade que o veiculo estava trafegando: '))

velocidade_acima = velocidade_veiculo - velocidade_limite
valor_multa = velocidade_acima * multa

if velocidade_veiculo > velocidade_limite:
     print(f'Você excedeu o limite em {velocidade_veiculo:.0f} km/h.\nE sua multa foi de {valor_multa}')
     
else :
    print(f'Você estava dentro do limite de velocidade: {velocidade_veiculo}, que é de {velocidade_limite}km/h!')