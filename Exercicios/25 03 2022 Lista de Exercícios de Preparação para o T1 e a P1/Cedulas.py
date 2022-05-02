"""
Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o 
valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre
 o valor lido e a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).

Saída
Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias, conforme o 
exemplo fornecido. Não esqueça de imprimir o fim de linha após cada linha, caso contrário seu programa 
apresentará a mensagem: “Presentation Error”
"""

valor = int(input())

cem = valor // 100
cinquenta = ((valor - (cem * 100)) // 50)
vinte = ((valor - (cinquenta * 50) - (cem * 100)) // 20)
dez = ((valor - (cinquenta * 50) - (cem * 100) - (vinte * 20)) // 10)
cinco = ((valor - (cinquenta * 50) - (cem * 100) - (vinte * 20) - (dez * 10)) // 5)
dois =((valor - (cinquenta * 50) - (cem * 100) - (vinte * 20) - (dez * 10) - (cinco * 5)) // 2)
um =  ((valor - (cinquenta * 50) - (cem * 100) - (vinte * 20) - (dez * 10) - (cinco * 5) - (dois * 2)) // 1)

print(valor)
print(cem,"nota(s) de R$ 100,00")
print(cinquenta,"nota(s) de R$ 50,00")
print(vinte,"nota(s) de R$ 20,00")
print(dez,"nota(s) de R$ 10,00")
print(cinco,"nota(s) de R$ 5,00")
print(dois,"nota(s) de R$ 2,00")
print(um,"nota(s) de R$ 1,00")