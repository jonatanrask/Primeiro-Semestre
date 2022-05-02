'''
Faça um programa que leia um valor N. Este N será o tamanho de um vetor X[N]. A seguir, leia cada um 
dos valores de X, encontre o menor elemento deste vetor e a sua posição dentro do vetor, mostrando 
esta informação.

Entrada
A primeira linha de entrada contem um único inteiro N (1 < N < 1000), indicando o número de elementos 
que deverão ser lidos em seguida para o vetor X[N] de inteiros. A segunda linha contém cada um dos N 
valores, separados por um espaço. Vale lembrar que nenhuma entrada haverá números repetidos.

Saída
A primeira linha apresenta a mensagem “Menor valor:” seguida de um espaço e do menor valor lido na 
entrada. A segunda linha apresenta a mensagem “Posicao:” seguido de um espaço e da posição do vetor 
na qual se encontra o menor valor lido, lembrando que o vetor inicia na posição zero.
'''
tamanho = int(input())
numeros = input().split()
vetor = []
PosicaoFinal = 0

for i in range(tamanho):
    vetor.append(int(numeros[i]))
for i in range(0, tamanho, 1):
    if i == 0:
        menor = vetor[i]
        PosicaoFinal = i
    else:
        if vetor[i] < menor:
            menor = vetor[i]
            PosicaoFinal = i
print("Menor valor:", menor)
print("Posicao:", PosicaoFinal)



