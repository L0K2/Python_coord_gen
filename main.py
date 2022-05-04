import random

Graus = random.randint(0,90)

Minutos = random.randint(0,60)

Segundos = random.randint(0,60)

Graus2 = random.randint(0,90)

Minutos2 = random.randint(0,60)

Segundos2 = random.randint(0,60)

Norte_sul = ['N','S']
Leste_oeste = ['E','W']

NS = random.randint(0,1)
LS = random.randint(0,1)

print("A coordenada é:", Graus, "°", Minutos, "'", Segundos, "''", Norte_sul[NS], Graus2, "°", Minutos2, "'", Segundos2, "''", Leste_oeste[LS])



