from cabecalho import exibir_cabecalho

print('=='*30)
exibir_cabecalho('D052 - Pergunte se um aluno tem nota ≥ 7 ou fez trabalho extra', '21/08/2025')
print('=='*30)

nota = float(input('Digite a nota do aluno (0 a 10): '))
trabalho_extra = input('O aluno fez trabalho extra? (s/n): ').strip().lower()
trabalho_extra = trabalho_extra == 's'
if nota >= 7 or trabalho_extra:
    print('O aluno foi aprovado.')  
else:
    print('O aluno não foi aprovado.')


    