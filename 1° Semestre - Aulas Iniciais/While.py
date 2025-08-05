
# fim = int(input("Digite o último número a imprimir:"))
# x = 1
# while x <= fim:
#     print(x)
#     x+=2

# n = int(input("De qual tabuada precisa:"))
# f = int(input("Digite o final da tabuada:"))
# x = 1
# while x <=f:
#     print(f"{n}X{x}={n*x}")
#     x = x+1

# dp = int(input("Qual o deposito inicial?"))
# tx = int(input("Qual a taxa mensal?"))
# mes = 1
#
# while mes <= 24:
#     dp = dp + (dp * tx) / 100
#     print(f"{dp:.2f}")
#     mes += 1


# Dados da tabela
codigos = [1, 2, 3, 5, 9]
operacoes = [0.50, 1.00, 4.00, 7.00, 8.00]

# Cabeçalho
print(f"{'Código':<10}{'Operação':<10}")
print("-" * 20)

# Linhas da tabela
for codigo, operacao in zip(codigos, operacoes):
    print(f"{codigo:<10}{operacao:<10.2f}")
total = 0
acabou = False

while True:
    num=int(input("Digite um número a somar ou 0 para sair:"))
    if num == 1:
        total = total + 0.50
    elif num == 2:
        total = total + 1.00
    elif num == 3:
        total = total + 4.00
    elif num == 5:
        total = total + 7.00
    elif num == 9:
        total = total + 8.00
    elif num == 0:
        acabou = True
        break
    else:
        print("Esse codigo não existe!")

if acabou:
    print(total)







