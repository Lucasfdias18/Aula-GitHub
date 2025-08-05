#Lucas Ferreira Dias RM562577

#Você foi contratado para desenvolver um programa em Python para calcular a média semestral das disciplinas
#cursadas em uma faculdade.

#3 Checkpoints
#2 Sprints
#1 Global Solution (GS

print("Digite a baixo as notas solicitadas para calcular sua Média Semestral!")

C1 = float(input(print("Digite sua nota do primeiro checkpoint!\f")))
C2 = float(input(print("Digite sua nota do segundo checkpoint!\f")))
C3 = float(input(print("Digite sua nota do terceiro checkpoint!\f")))

notacheck = C1 + C2 + C3

if C1 < C3 and C2:
    notacheck = (C2 + C3)

if C2 < C1 and C3:
    notacheck = (C1 + C3)

if C3 < C1 and C2:
    notacheck = (C1 + C2)

else:
    notacheck = (C1 + C2)


S1 = int(input(print("Digite sua nota do primeiro Sprint!\f")))
S2 = int(input(print("Digite sua nota do segundo Sprint!\f")))

notasp = S1 + S2

notart = (notasp + notacheck) /4

GS = float(input(print("Digite sua nota da Global Solution!\f")))

print(f"Sua nota Semestral é igual à: {(notart * 0.4) + (GS * 0.6)}")
