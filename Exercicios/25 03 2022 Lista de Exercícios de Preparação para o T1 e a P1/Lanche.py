'''
Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade 
deste item. A seguir, calcule e mostre o valor da conta a pagar.

https://resources.beecrowd.com.br/gallery/images/problems/UOJ_1038_pt.png

Entrada
O arquivo de entrada contém dois valores inteiros correspondentes ao código e à quantidade 
de um item conforme tabela acima.

Saída
O arquivo de saída deve conter a mensagem "Total: R$ " seguido pelo valor a ser pago, com 2 
casas após o ponto decimal.
'''

preco = 0

compra = input().split()
quantidade = int(compra[1])
item = int(compra[0])

if item == 1:
    preco = 4.0
elif item == 2:
    preco = 4.5
elif item == 3:
    preco = 5.0
elif item == 4:
    preco = 2.0
elif item == 5:
    preco = 1.5

PrecoTotal = preco * quantidade
print("Total: R$ {:.2f}".format(PrecoTotal))