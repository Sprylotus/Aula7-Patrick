import os

os.system('cls')


nome = input('Informe o nome: ')
cargo = input('Informe o cargo: ')
salario = float(input('Informe o salário: '))
idade = float(input('Informe a idade: '))

tupla = (nome, cargo, salario, idade)

print(f'Seus dados: {tupla}')