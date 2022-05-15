'''
Nick é um cientista que viaja por diversos universos paralelos, juntamente com o seu neto, Mory. Em 
um desses universos, havia um programa de televisão, que premiava quem adivinhasse as alturas máximas 
de arremessos de frutas. Neste local, a massa da fruta não influenciava na altura máxima do arremesso.
Nick calculava o ângulo do arremesso, que formava sempre uma parábola, e extraía uma função de 
segundo grau da trajetória. Ajude Nick e Mory a ganhar muitos prêmios neste programa.

Entrada
A entrada é composta por vários casos de teste. A primeira linha contém um número inteiro 
T (2 <= T <= 99) relativo ao número de casos de teste. As T linhas seguintes possuem três valores 
inteiros A (A < 0), B e C (-100 <= B, C <= 100), representando os coeficientes de uma função de 
segundo grau, na forma ax2 + bx + c.

Saída
Para cada caso de teste de entrada do seu programa, você deve imprimir um número real, com 
aproximação de duas casas decimais, a altura máxima do arremesso de uma fruta.
'''

teste = int(input()) #Recebe um inteiro 


for i in range(0, teste, 1): #Calcula o numero de repetições baseado no inteiro
    valores = input().split() #Recebe uma string com 3 valores e separa ele apagando os espaços
    a = int(valores[0]) #primeiro valor recebido
    b = int(valores[1]) #Segundo valor recebido
    c = int(valores[2]) #Terceiro valor recebido
    
    delta = (b * b) - (4 * a * c) #Calcula o delta da formula basica de equação do segundo grau
    resultado = -(delta / (4 * a)) #Chega no resultado com a segunda parte do resultado
    print("{:.2f}".format(resultado)) #Printa o resultado formatando com duas casas decimais