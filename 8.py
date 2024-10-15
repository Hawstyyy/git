# 8 - Crie um algoritmo que receba 5 números e exiba o maior e o menor número informados. 
lista = []
for x in range(5):
  lista.append(int(input("Insira o seu número: ")))

maior = lista[0]
menor = lista[0]

for x in lista:
  if x > maior:
    maior = x
  if x < menor:
    menor = x

print(f'o maior número é: {maior}')
print(f'o menor número é: {menor}')