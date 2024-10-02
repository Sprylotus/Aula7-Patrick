import os

os.system('cls')


def paridade(a):
    if n % 2 == 0:
        print('Par')
    else:
        print('Ímpar')
    return n


n = int(input('Informe um número: '))

num = paridade(n)

print(num)