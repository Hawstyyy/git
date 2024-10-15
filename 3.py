# 3 - Escreva uma função que verifique se uma palavra ou frase é um palíndromo (pode ser lida da mesma maneira de trás para frente).
try:
  palavra = input("Insira a sua palavra: ")
except ValueError as err:
  print(f"Erro: {err}")

palavraRev = ''

for x in range(len(palavra)-1, -1, -1):
  palavraRev += palavra[x]

if palavraRev == palavra:
  print("é um palíndromo")
else:
  print("não é palíndromo")