# D053: Aprovado na disciplina:
# O aluno é aprovado se tiver média ≥ 7ou média entre 5 e 6,9 com frequência ≥ 75%.
from cabecalho import exibir_cabecalho

print('=='*30)
exibir_cabecalho('D053 - Aprovado na disciplina', '21/08/2025')
print('=='*30)

media = float(input('Digite a média do aluno (0 a 10): '))
frequencia = float(input('Digite a frequência do aluno (0 a 100): '))
if media >= 7 or (5 <= media < 7 and frequencia >= 75):
    print('O aluno foi aprovado.') 
else:
    print('O aluno não foi aprovado.')
