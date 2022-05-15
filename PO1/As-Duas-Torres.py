variaveis = input().split()
distancia = int(variaveis[0])
diametro1 = int(variaveis[1])
diametro2 = int(variaveis[2])

icm = distancia / (diametro1 + diametro2)

print("{:.2f}".format(icm))
