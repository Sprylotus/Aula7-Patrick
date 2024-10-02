import os

os.system('cls')


def decoracao():
    print(30*'=')




def saudacao(txt):
    print(f'Olá {txt}')


def somar(a, b):
    total = a + b
    med = (a + b) / 2
    # print(f'Total é: {total}')
    return total, med  

# decoracao()
# print('Iniciando Programa')
# print('nome: ')
# print('idade: ')
# print('cidade: ')

# decoracao()
# print('Dados Pessoais')
# print('CPF: ')
# print('RG: ')

# decoracao()
# print('Rede Social')
# print('Linkedin')
# print('GitHub')


# print('INICIANDO O PROGRAMA')
# nome = input('Informe seu nome: ')
# cpf = input('Informe seu CPF: ')

# decoracao()
# saudacao(nome)
# saudacao(cpf)
    

n1 = float(input('número: '))
n2 = float(input('número: '))

valor, media = somar(n1, n2)

print(valor)
print(media)