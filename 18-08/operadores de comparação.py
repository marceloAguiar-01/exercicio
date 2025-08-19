#####  OPERADORES DE COMPARAÇÂO
'''
print(10>5)    # maior que
print(10==5)   # igual
print(10!=5)   # diferente
print(10<5)    #menor
print(>=)    # maior ou igual
print(<=)    # menor ou igual
'''
a = 10
b = 20

print(a==b)    # False
print(a!=b)    #  True
print(a>b)     # False
print(a<b)     #True
print(a>=b)    # False
print(a<=b)    # True


# Atribuição de valores às variáveis
'''
a=input('Digite um valor para comparar: ')
b=input('Digite um valor para comparar: ')

print(f"{a} == {b} → {a == b}")   # a igual a b → False
print(f"{a} != {b} → {a != b}")   # a diferente de b → True
print(f"{a} >  {b} → {a >  b}")   # a maior que b → False
print(f"{a} <  {b} → {a <  b}")   # a menor que b → True
print(f"{a} >= {b} → {a >= b}")   # a maior ou igual a b → False
print(f"{a} <= {b} → {a <= b}")   # a menor ou igual a b → True
'''

# if = se
# else = se não

# sempre terminar alinha com dois pontos:

# if condição:
    # executa caso a condição seje verdadeirs  caso nao seja ele nao executa.
#

'''
tempo = int(input('Quantos anos tem seu carro: '))

if tempo <= 3:
    print('Carro novo')
elif tempo <= 5:
    print('Seu carro é semi novo')
else:
    print('Carro velho')
'''
print('Carro novo' if (t := int(input('Quantos anos tem seu carro: '))) <= 3 else 'Seu carro é semi novo' if t <= 5 else 'Carro velho')

