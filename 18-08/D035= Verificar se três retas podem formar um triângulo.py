#�D035: Verificar se três retas podem formar um triângulo.
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


# para formar um triangulo cada lado tem que ser monor que os outros dois lados

a = float(input("Digite o valor da 1ª reta: "))
b = float(input("Digite o valor da 2ª reta: "))
c = float(input("Digite o valor da 3ª reta: "))

if a < b + c and b < a + c and c < a + b:
    print("✅ As retas podem formar um triângulo!")
else:
    print("❌ As retas NÃO podem formar um triângulo.")
