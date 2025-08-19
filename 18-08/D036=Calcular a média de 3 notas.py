#D036: Situação do aluno: Calcular a média de 3 notas, para status de Aprovado 
#média no mínimo 7.0, caso contrario Reprovado

data = '18/08/2025'
aluno = 'Marcelo Aguiar de Barros'
atividade = 'D036=Calcular a média de 3 notas, para status de Aprovado média no mínimo 7.0, caso contrario Reprovado'

print('CETAM - CENTRO DE EDUCAÇÃO TECNOLÓGICA DO AMAZONAS')
print('CURSO: DESENVOLVIMENTO DE SISTEMA')
print('COMPONENTE: LINGUAGEM DE PROGRAMAÇÃO')
print('DATA: ',data, )
print('PROFESSOR: MICHALES CAMURÇA')
print('ALUNO: ', aluno, )
print('ATIVIDADE: ',atividade, )



nota1, nota2 ,nota3= map(float,input('Digite 1º , 2º e 3º nota com espaço entere elas: ').replace(',', '.').split())
print(f"A média é {(nota1 + nota2 + nota3) / 3:.1f}")


media = (nota1 + nota2 + nota3) / 3

if media <= 6:
    print('Você não conseguiu a média, você não passou, se esforce mais e tente novamente!') 
elif media == 7 or media < 9:
    print('Você passou, continue se esforsando para melhorar cada vez mais!')
else :
    print('Parabens você passou com nota maxima parabens, continue assim!')