'''
Ler um valor N. Calcular e escrever seu respectivo fatorial. 
Fatorial de N = N * (N-1) * (N-2) * (N-3) * ... * 1.

Entrada
A entrada contém um valor inteiro N (0 < N < 13).

Saída
A saída contém um valor inteiro, correspondente ao fatorial de N.
'''
idade = 0
total = 0
quantidade = 0
while(True):
    idade = int(input())
    if idade < 0:
        break
    else:
        total = total + idade
        quantidade = quantidade + 1
media = total / quantidade
print("{:.2f}".format(media))