# Teste Lista com carros
carros = ["Mcqueen", "Mater", "DocHudson", "Chick Hicks"]
print (carros)
print(len(carros))

# res = input(f"Qual o Melhor carro de Carros?\n")
# if res==(carros[0]):
#     print ("Kachow")

carros[1] = "Sally"
carros_back = carros[1:4]    # ou carros[:] para mostrar todos novos
print(carros_back)


    #Lista Simples
# notas = [6,8,4,1,2]
# soma = 0
# x = 0
# while x < 5:
#     soma+=notas[x]
#     x+= 1
# print(f"Média = {(soma/x):.2f}")

  # fatiamento de lista
# L = [1,2,3,4,5]
# print(L[0:5]) = 1,2,3,4,5
# print(L[:5]) = 1,2,3,4,5
# print(L[:-1]) = 1,2,3,4
# print(L[1:3]) = 2,3
# print(L[1:4]) = 2,3,4
# print(L[3:]) = 4,5
# print(L[:3]) = 1,2,3
# print(L[-1]) = 5
# print(L[-2]) = 4