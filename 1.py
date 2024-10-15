# 1 - Crie uma função que calcule o fatorial de um número dado pelo usuário.

def fatorial(n):
  res = n
  for x in range(n-1,1,-1):
    res *= x
  print(res)

num1 = int(input())

fatorial(num1)