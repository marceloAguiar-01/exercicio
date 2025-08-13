#D011 – Calcular área de uma parede e quantidade de tinta (1L → 2m²)


professor = 'MICHALES CAMURÇA'
data = '08/08/2025'
aluno = 'Marcelo Aguiar de Barros'
atividade = 'D0011-📌 Objetivo:D011 – Calcular área de uma parede e quantidade de tinta (1L → 2m²)
'

print('CETAM - CENTRO DE EDUCAÇÃO TECNOLÓGICA DO AMAZONAS')
print('CURSO: DESENVOLVIMENTO DE SISTEMA')
print('COMPONENTE: LINGUAGEM DE PROGRAMAÇÃO')
print('DATA: ',data, )
print('PROFESSOR:', professor)
print('ALUNO: ', aluno, )
print('ATIVIDADE: ',atividade, )

#COD1

print('=' * 30)
largura = float(input('Largura da parede (m): '))
altura = float(input('Altura da parede (m): '))
print('=' * 30)

area = largura * altura
tinta = area / 2  # 1 litro para 2m²

print(f'Área da parede: {area:.2f} m²')
print(f'Quantidade de tinta necessária: {tinta:.2f} litros')
