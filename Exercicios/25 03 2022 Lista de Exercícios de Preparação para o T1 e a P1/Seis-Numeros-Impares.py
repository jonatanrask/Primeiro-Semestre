'''
Leia um valor inteiro X. Em seguida apresente os 6 valores ímpares consecutivos a partir de X, 
um valor por linha, inclusive o X ser for o caso.

Entrada
A entrada será um valor inteiro positivo.

Saída
A saída será uma sequência de seis números ímpares.
'''
contagem = 0
numero = int(input())

while(contagem < 6):
    if numero % 2 != 0:
        print(numero)
        contagem = contagem + 1
    numero = numero + 1