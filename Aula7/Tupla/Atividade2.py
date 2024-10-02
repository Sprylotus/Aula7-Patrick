import os

os.system('cls')


n1 = int(input('Informe o número: '))
n2 = int(input('Informe o número: '))
n3 = int(input('Informe o número: '))
n4 = int(input('Informe o número: '))
n5 = int(input('Informe o número: '))

tupla = (n1, n2, n3, n4, n5)


maior = max(tupla)
menor = min(tupla)
soma = sum(tupla)
ordem = (tupla)

ord = sorted(ordem)

print('\n----- Resultados -----')
print(f'O maior número é: {maior}')
print(f'O menor número é: {menor}')
print(f'A soma é: {soma}')
print(f'Os números em ordem crescente ficam: {ord}')
print('----------------------')