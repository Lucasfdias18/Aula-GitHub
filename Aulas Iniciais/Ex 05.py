
op = (input(print("1- Adição\f2- Subtração\f3- Multiplicação\f4- Divisão")))

num1 = float(input(print("Digite o primeiro número:")))
num2 = float(input(print("Digite o segundo número:")))

if op == 1:
    resp = (num1 + num2)
    print(f"Seu resultado é igual a {resp}")
if op == 2:
    resp = (num1 - num2)
    print(f"Seu resultado é igual a {resp}")
if op == 3:
    resp = (num1 * num2)
    print(f"Seu resultado é igual a {resp}")
if op == 4:
    resp = (num1 / num2)
    print(f"Seu resultado é igual a {resp}")