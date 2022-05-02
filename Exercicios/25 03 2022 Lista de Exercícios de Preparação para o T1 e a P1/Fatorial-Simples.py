'''
Ler um valor N. Calcular e escrever seu respectivo fatorial. 
Fatorial de N = N * (N-1) * (N-2) * (N-3) * ... * 1.

Entrada
A entrada contém um valor inteiro N (0 < N < 13).

Saída
A saída contém um valor inteiro, correspondente ao fatorial de N.
'''
n = int(input())
n2 = n
vezes = n + 1
fatorial = 1
while (fatorial < vezes):
    n = n * (n2 - fatorial)
    fatorial = fatorial + 1
print(n)     