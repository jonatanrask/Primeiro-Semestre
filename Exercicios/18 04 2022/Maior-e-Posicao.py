'''
Leia 100 valores inteiros. Apresente então o maior valor lido e a posição dentre os 100 valores lidos.

Entrada
O arquivo de entrada contém 100 números inteiros, positivos e distintos.

Saída
Apresente o maior valor lido e a posição de entrada, conforme exemplo abaixo.
'''

maior = 0
PosicaoAtual = 0
for i in range(1, 101, 1):
    numero = int(input())
    if numero > maior:
        maior = numero
        PosicaoAtual = i
print(maior)
print(PosicaoAtual)
    
