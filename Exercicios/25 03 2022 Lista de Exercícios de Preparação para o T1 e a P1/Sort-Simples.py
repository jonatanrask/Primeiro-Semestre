'''
Leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os valores em 
ordem crescente, uma linha em branco e em seguida, os valores na sequência como foram lidos.

Entrada
A entrada contem três números inteiros.

Saída
Imprima a saída conforme foi especificado.
'''

valores = input().split()
valor1 = int(valores[0])
valor2 = int(valores[1])
valor3 = int(valores[2])

maior = valor1
if maior < valor2:
    maior = valor2
if maior < valor3:
    maior = valor3

menor = valor2
if menor > valor1:
    menor = valor1
if menor > valor3:
    menor = valor3
 
meio = valor3
if valor1 != maior and valor1 != menor:
    meio = valor1
if valor2 != maior and valor2 != menor:
    meio = valor2

 
print(menor)
print(meio)
print(maior)
print()
print(valores[0])
print(valores[1])
print(valores[2])

