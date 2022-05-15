'''
Fazer um programa que leia vários casos de teste, terminados com fim de arquivo (EOF). Cada caso de 
teste corresponde a uma leitura de 10 números inteiros, com definição pelo programa de qual é o menor 
número lido, x; seguida de uma leitura de 10 números inteiros, com definição pelo programa de qual é 
o maior número lido, y. O programa deverá mostrar a média, com uma casa decimal, dos valores inteiros 
entre x e y, incluindo x e y.

Entrada
Em cada caso de teste, há a leitura de 10 valores inteiros seguida da leitura de mais 10 valores 
inteiros. Cada valor será lido em uma linha separada.

Saída
Em cada caso de teste, mostra-se a média, com uma casa decimal, dos valores inteiros entre x e y, 
incluindo x e y.
'''

'''
Arquivo para usar no exercicio = teste.txt

comando para testar no terminal:

Windows PowerShell: Get-Content teste.txt | python Media-entre-minimo-e-maximo.py
Linux: Python3 Media-entre-minimo-e-maximo.py < teste.txt
'''

x = 0
y = 0
maior = 0
menor = 0

while True:

    try:
        for i in range(0, 10, 1):
            #print(i)
            x = int(input())
            if i == 0:
                menor = x
            if menor > x:
                menor = x
            #print("esse é o x",x)
            #print("esse é o menor",menor)
        
        for i in range(0, 10, 1):
            y = int(input())
            if i == 0:
                maior = y
            if maior < y:
                maior = y
            #print("esse é o y",y)
            #print("esse é o maior",maior)
        media = (maior + menor) / 2
        print(media)
    except EOFError:
        break


