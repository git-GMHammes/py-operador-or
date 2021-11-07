#
# Operador Or
#
print(f'\n Teste 1: if else\n')
nome1 = input('Digite o seu nome: ')
if nome1:
    print(f'Olá: {nome1} \n')
else:
    print(f' Você não dgitou nada no Teste 1')
#
print(f'\n Teste 2: ternário Or\n')
nome2 = input('Digite o seu nome: ')
print(nome2 or 'Você não dgitou nada no Teste 2 \n ')
