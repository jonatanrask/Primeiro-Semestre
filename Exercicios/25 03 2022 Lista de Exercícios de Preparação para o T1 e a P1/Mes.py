'''
Leia um valor inteiro entre 1 e 12, inclusive. Correspondente a este 
valor, deve ser apresentado como resposta o mês do ano por extenso,
 em inglês, com a primeira letra maiúscula.

Entrada
A entrada contém um único valor inteiro.

Saída
Imprima por extenso o nome do mês correspondente ao número existente na 
entrada, com a primeira letra em maiúscula.
'''
numero = int(input())
mes = ""
if numero == 1:
    mes = "January"
elif numero == 2:
    mes = "February"
elif numero == 3:
    mes = "March"
elif numero == 4:
    mes = "April"
elif numero == 5:
    mes = "April"
elif numero == 6:
    mes = "June"
elif numero == 7:
    mes = "July"
elif numero == 8:
    mes = "August"
elif numero == 9:
    mes = "September"
elif numero == 10:
    mes = "October"
elif numero == 11:
    mes = "November"
elif numero == 12:
    mes = "December "

print(mes)