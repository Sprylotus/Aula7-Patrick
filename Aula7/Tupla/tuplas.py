import os

os.system('cls')


tupla_vazia = ()

# Tupla de um elemento
tupla_um_elemento = (10,)
# print(tupla_um_elemento)
# print(type(tupla_um_elemento))

tupla_varios_elementos = (5, 4, 10, 15, 12)
# print(tupla_varios_elementos)

tupla_um_elemento = tupla_um_elemento + tupla_varios_elementos

# Sorted organiza os elementos da tupla em ordem crescente e transforma em lista
# print(sorted(tupla_um_elemento))

nome = input('Informe o nome: ')
nota1 = float(input('Informe a nota: '))
nota2 = float(input('Informe a nota: '))

tupla_notas = (nome, nota1, nota2)

print(f"Dados do Usuário: {tupla_notas}")