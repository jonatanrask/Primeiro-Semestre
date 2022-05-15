'''
Leia 1 valor inteiro N (2 < N < 1000). A seguir, mostre a tabuada de N:      
1 x N = N      2 x N = 2N        ...       10 x N = 10N

Entrada
A entrada contém um valor inteiro N (2 < N < 1000).

Saída
Imprima a tabuada de N, conforme o exemplo fornecido.
'''

entrada = int(input())

if entrada > 2 and entrada < 1000:
    tabuada = entrada
    print("1 x",entrada,"=",tabuada)
    tabuada = entrada * 2
    print("2 x",entrada,"=",tabuada)
    tabuada = entrada * 3
    print("3 x",entrada,"=",tabuada)
    tabuada = entrada * 4
    print("4 x",entrada,"=",tabuada)
    tabuada = entrada * 5
    print("5 x",entrada,"=",tabuada)
    tabuada = entrada * 6
    print("6 x",entrada,"=",tabuada)
    tabuada = entrada * 7
    print("7 x",entrada,"=",tabuada)
    tabuada = entrada * 8
    print("8 x",entrada,"=",tabuada)
    tabuada = entrada * 9
    print("9 x",entrada,"=",tabuada)
    tabuada = entrada * 10
    print("10 x",entrada,"=",tabuada)