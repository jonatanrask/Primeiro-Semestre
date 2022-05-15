'''
Faça um programa que leia um número inteiro N (-1 < N < 10000), e mostre quantos milhares, centenas, 
dezenas e unidades esse número possui.

Entrada
Um número inteiro N (-1 < N < 10000).
Saída

Mostrar em linhas diferentes: a quantidade de milhares, centenas, dezenas e unidades que N possui
'''

valor = int(input()) #Recebendo o numero inteiro a ser analisado

'''
Iniciando variaveis com o valor inicial "0" para ser modificado dependendo da variavel "valor
'''
milhar = 0
centena = 0
dezena = 0
unidade = 0


if valor > 999 and valor <= 10000: #Caso o valor seja maior que 999 ou seja chegue a casa do milhar
    milhar = (valor // 1000) % 1000 #Sera calculado quantos milhares esse valor tem fazendo uma divisão absoluta e vendo quanto sobra
    centena = ((valor // 100) % 10) #Quantas centenas
    dezena = (valor // 10) % 10 #E quantas dezenas
    unidade = (valor // 1) % 10
 

elif valor > 99 and valor <= 999: #Caso o valor se limite as centenas
    centena = ((valor // 100) % 100) #Sera calculado quantas centenas esse valor tem fazendo uma divisão absoluta e vendo quanto sobra
    dezena = (valor // 10) % 10 #quantas dezenas utilizando o metodo anterior
    unidade = valor - ((centena * 100) + (dezena * 10)) #E as unidades com o metodo de sobra ja explicado

elif valor > 9 and valor <= 99: #Caso o valor se limite as dezenas
    dezena = (valor // 10) % 10 #Sera calculado quantas dezenas esse valor tem fazendo uma divisão absoluta e vendo quanto sobra
    unidade = valor - + ((dezena * 10)) #E as unidades com o metodo de sobra ja explicado
elif valor > -1 and valor <= 9: #Caso o valor se limite as dezenas
    unidade = valor #A unidade sera igual ao valor e as casas superiores não existirão logo igual a 0 como inicialmente instanciadas
print("%d:" % valor)
print(milhar, "milhar(es)")
print(centena, "centena(s)")
print(dezena, "dezena(s)")
print(unidade, "unidade(s)")