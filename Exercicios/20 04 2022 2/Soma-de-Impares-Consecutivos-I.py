'''
Leia 2 valores inteiros X e Y. A seguir, calcule e mostre a soma dos números impares entre eles.

Entrada
O arquivo de entrada contém dois valores inteiros.

Saída
O programa deve imprimir um valor inteiro. Este valor é a soma dos valores ímpares que estão entre 
os valores fornecidos na entrada que deverá caber em um inteiro.
'''
primeiro = int(input())
segundo = int(input())
media = 0
impar = 0

if primeiro > segundo:
    for i in range(segundo + 1, primeiro, 1):
        if i == segundo + 1:
            if i % 2 != 0:
                impar = i
        else:
            if i % 2 != 0:
                impar = impar + i
if segundo > primeiro:
    for i in range(primeiro + 1, segundo, 1):
        if i == primeiro + 1:
            if i % 2 != 0:
                impar = i
        else:
            if i % 2 != 0:
                impar = impar + i
print(impar)