# 4 - Faça um programa que verifique se um número fornecido é primo.

num = int(input('Insira o seu número: '))
primo = 0

for i in range(1, num+1):
  if num % i == 0:
    primo += 1

if primo == 2:
  print(num, 'é primo')
else:
  print(num, 'não é primo')