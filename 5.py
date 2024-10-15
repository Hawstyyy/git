# 5  - Desenvolva uma função que mostre os n primeiros termos da sequência de Fibonacci, onde n é informado pelo usuário.

n = int(input())
fibonacci1 = 0
fibonacci2 = 1
fibonacci3 = 0

for x in range(0,n):
    print(f"{fibonacci3}")

    fibonacci3 = fibonacci1 + fibonacci2
    fibonacci1 = fibonacci2
    fibonacci2 = fibonacci3