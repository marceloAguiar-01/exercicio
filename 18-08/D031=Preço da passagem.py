# D031: Multa de velocidade (> 80 km/h → R$ 7 por km acima)
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



km=int(input('Digite a distancia a ser percorrida em km: '))

if km <= 200:
    preco=0.5*km
    print(f"O valor da passagem até 200 km sera de :$ {preco} reais.")
else :
    preco=0.45*km
    print(f"O valor da passagem até 200 km sera de :$ {preco} reais.")