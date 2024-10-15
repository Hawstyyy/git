# 2 - Desenvolva um programa que mostre a tabuada de um número informado pelo usuário.

def tabuada(n):
  for x in range(1,10+1):
    print(f"{n} x {x} = {n * x}")

num = int(input())

tabuada(num)