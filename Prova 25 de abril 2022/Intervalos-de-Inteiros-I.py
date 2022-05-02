'''
Faça um programa que leia vários intervalos abertos de inteiros. Para cada intervalo mostrar as 
quantidades de inteiros, de pares, de ímpares e de inteiros divisíveis por 5. Não ler o próximo 
intervalo caso, no intervalo atual, a quantidade de divisíveis por 5 for par.

Entrada
A entrada é um conjunto de casos de teste. Cada caso de teste é um intervalo aberto de 
inteiros (x, y), x >= 0 e x < y, com x e y lidos na mesma linha, separados por espaço.

Saida
Para cada caso de teste, mostrar as quantidades de inteiros, de pares, de ímpares e de inteiros 
divisíveis por 5, seguindo o formato do modelo do exemplo de saída. Entre a saída de um caso de teste 
e a do próximo deve haver uma linha em branco, mas sem linha em branco após o último caso de teste.
'''
divisiveis = 1

while(divisiveis % 2 != 0):
    xs, ys = input().split()

    x = int(xs)
    y = int(ys)
    divisiveis = 0
    inteiros = 0
    QtdPares = 0
    QtdImpars = 0



    for n in range(x + 1, y, 1):
        inteiros = y - x - 1
        parouimpar = n % 2
        if parouimpar == 0:
            QtdPares = QtdPares + 1
        else:
            QtdImpars = QtdImpars + 1
        if n % 5 == 0:
            divisiveis = divisiveis + 1
    print("Intervalo (%d, %d):"%(x, y))        
    print("Quantidade de inteiros:", inteiros)
    print("Quantidade de pares:", QtdPares)
    print("Quantidade de ímpares:",QtdImpars)
    print("Quantidade de divisíveis por 5:", divisiveis)
    if divisiveis % 2 != 0:
        print("")



    
    
   