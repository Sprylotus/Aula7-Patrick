import os

os.system('cls')


# lista das previsões
lista_previsoes = ['Nublado', "Chuvoso", "Tempestade", "Ensolarado", 'Ensolarado']

# lista dos dias da semana
lista_dias = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta']

# declara duas listas vazias
dias_ensolarados = []
dias_sem_sol = []

# for p in lista_previsoes:
#     if p == "Ensolarado":
#         dias_ensolarados.append(p)
#     else:
#         dias_sem_sol.append(p)

# print(f"Dias ensolarados: {dias_ensolarados}")

# print(f'Dias sem sol: {dias_sem_sol}')

# Enumarate utilizado para transformar as 
for i, v in enumerate(lista_previsoes):

    if lista_previsoes[i] == 'Ensolarado':
        dias_ensolarados.append(lista_dias[i])
    else:
        dias_sem_sol.append(lista_dias[i])

#     if p == "Ensolarado":
#         dias_ensolarados.append(p)
#     else:
#         dias_sem_sol.append(p)

print(f"Dias ensolarados: {dias_ensolarados}")

print(f'Dias sem sol: {dias_sem_sol}')