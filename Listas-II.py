# Criação de lista de alunos
from gmpy2 import lucas

# nome_alunos = []
#
# nome_alunos.append("Lucas")
# print(nome_alunos)
#
# nome_alunos.append("Leticia")
# print(nome_alunos)

#####################################################################
# n_a = []
#
# while True:
#     nome = input("Digite o nome de seus colegas:\n")
#     print("(Digite fim para sair)")
#     if nome == str("fim"):
#         break
#     n_a.append(nome)
#
# x = 0
# while x < len(n_a):
#     print(n_a[x])
#     x += 1

# nome = []
# nome = nome + ["Lucas"]
# nome += ["Felipe"]


######################################################################
# nomev = []
#
# while True:
#     nome = input("Digite o nome de três colegas!\n")
#
#     if str(nome) == (''):
#         break
#     nomev.append(nome)
#
#
#
# nomem = []
#
# while True:
#     nomei = input("Digite o nome de três vitimas!\n")
#
#     if str(nomei) == (''):
#         break
#     nomem.append(nomei)
#
# y = 0
# while y < len(nomem):
#     print(nomem[y])
#     y += 1
#
# x = 0
# while x < len(nomev):
#     print(nomev[x])
#     x += 1
#
# nomev.extend (nomem)

###################################################################

alunas = ["Lunna", "Anna", "Leticia", "Karem"]
procura = int(input("Escreva o nome de quem quer econtrar:"))
x = 0
while x <len(alunas):
    if alunas[x] == procura:
        encon = True
        break
    else:
        encon = False
    x += 1

    if encon == True:
        print(f"{procura} está na posição {x} da fila.")
    else:
        print(f"{procura} não foi encontrada na fila.")