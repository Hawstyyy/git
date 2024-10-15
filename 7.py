# 7 - Faça um programa que converta uma temperatura de Celsius para Fahrenheit e vice-versa. O usuário deverá escolher a conversão desejada.

while True:
  try:
    choice = int(input('''1 - converter para Fahrenheit
2 - converter para celsius
- '''))
  except ValueError as err:
    print("Valor inválido: ",err)
  
  if choice == 1:
    celsius = int(input('Insira a temperatura em Celsius: '))
    f = (celsius * 1.8) + 32
    print(f'{celsius}° em Fahrenheit será: {f}')
    break
  else:
    f = int(input('Insira a temperatura em Fahrenheit: '))
    celsius = (f - 32) / 1.8
    print(f'{f} em Celsius será: {celsius}')
    break