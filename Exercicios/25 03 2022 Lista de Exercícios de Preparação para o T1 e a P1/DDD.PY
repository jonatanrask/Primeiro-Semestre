'''
Leia um número inteiro que representa um código de DDD para discagem interurbana. Em seguida, informe à qual cidade o DDD pertence, 
considerando a tabela abaixo:

https://resources.beecrowd.com.br/gallery/images/problems/UOJ_1050.png

Se a entrada for qualquer outro DDD que não esteja presente na tabela acima, o programa deverá informar:
DDD nao cadastrado

Entrada
A entrada consiste de um único valor inteiro.

Saída
Imprima o nome da cidade correspondente ao DDD existente na entrada. Imprima DDD nao cadastrado caso não existir DDD correspondente ao 
número digitado.
'''

numero = int(input())
destino = ""
if numero == 61:
    destino = "Brasilia"
elif numero == 71:
    destino = "Salvador"
elif numero == 11:
    destino = "Sao Paulo"
elif numero == 21:
    destino = "Rio de Janeiro"
elif numero == 32:
    destino = "Juiz de Fora"
elif numero == 19:
    destino = "Campinas"
elif numero == 27:
    destino = "Vitoria"
elif numero == 31:
    destino = "Belo Horizonte"
else:
    destino = "DDD nao cadastrado"

print(destino)
