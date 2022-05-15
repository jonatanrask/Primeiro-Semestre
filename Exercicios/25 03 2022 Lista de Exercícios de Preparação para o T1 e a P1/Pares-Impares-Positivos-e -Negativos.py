'''
Leia 5 valores Inteiros. A seguir mostre quantos valores digitados foram pares, quantos valores
digitados foram ímpares, quantos valores digitados foram positivos e quantos valores digitados
foram negativos.

Entrada
O arquivo de entrada contém 5 valores inteiros quaisquer.

Saída
Imprima a mensagem conforme o exemplo fornecido, uma mensagem por linha, não esquecendo o
final de linha após cada uma.
'''
par = 0
impar = 0
positivo = 0
negativo = 0

for i in range(0, 5, 1):
    valor = int(input())
    if valor % 2 == 0:
        par = par + 1
    else: impar = impar + 1
    if valor > 0:
        positivo = positivo + 1
    elif valor < 0:
        negativo = negativo + 1

print(par, "valor(es) par(es)")
print(impar, "valor(es) impar(es)")
print(positivo, "valor(es) positivo(s)")
print(negativo, "valor(es) negativo(s)")
    
