# 6 - Escreva um algoritmo que receba uma lista de números e retorne a lista ordenada de forma crescente (Bubble sort).

lista = input("insira a lista de número que deseja separados por virgula: ").split(",")

size = len(lista)
for i in range(size -1): 
    for j in range (size -1):
        if lista[j] > lista[j + 1]:
            lista[j], lista[j + 1] = lista[j + 1], lista[j]
print(lista)