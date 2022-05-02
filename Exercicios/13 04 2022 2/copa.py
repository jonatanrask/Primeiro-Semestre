'''
Timelimit: 1
O sorteio das posições dos jogadores na chave decisiva da copa do mundo de ping-pong está deixando 
a todos nervosos. É que ninguém quer pegar o jogador mais bem ranqueado, o Mestre Kung, logo nas 
oitavas de final, ou nas quartas de final. Melhor que só seja possível enfrentar Mestre Kung na 
semifinal ou na final!

A chave possui 16 posições numeradas de 1 a 16, como na figura abaixo. A organização da copa vai 
fazer um sorteio para definir em qual posição cada jogador vai iniciar a chave decisiva. Nas oitavas 
de final, o jogador na posição 1 enfrenta o jogador na posição 2; o da posição 3 enfrenta o da 
posição 4; e assim por diante, como na figura.

https://resources.beecrowd.com.br/gallery/images/problems/UOJ_2830.png

O objetivo deste problema é, dadas as posições de Mestre Kung e Mestre Lu na chave, decidir em que 
fase da competição Mestre Kung e Mestre Lu vão se enfrentar, caso vençam todas as suas respectivas 
partidas antes de se enfrentarem. Por exemplo, se o sorteio da chave determinar que Mestre Kung 
ocupará a posição 1 e Mestre Lu a posição 2 da chave, eles se encontrarão nas oitavas de final; 
se Mestre Kung ocupar a posição 6 e Mestre Kung ocupar a posição 9 da chave, eles se encontrarão 
somente na final.

Entrada
A entrada consiste de duas linhas. A primeira linha da entrada contém um inteiro K (1 ≤ K ≤ 16) que 
indica a posição de Mestre Kung na chave. A segunda linha da entrada contém um inteiro L (1 ≤ L ≤ 16, K ≠ L) 
que indica a posição de Mestre Lu na chave.

Saída
Seu programa deve produzir uma linha contendo uma das palavras seguintes, decidindo a fase em que 
vão se enfrentar os jogadores Mestre Kung e Mestre Lu, se eles chegarem a se enfrentar: oitavas, 
quartas, semifinal ou final.
'''

kung = int(input())
lu = int(input())

   
if kung > lu and kung % 2 == 0 and kung - lu == 1:
    print("oitavas")
elif lu > kung and lu % 2 == 0 and lu - kung == 1:
    print("oitavas")
elif kung >= 1 and kung <= 4 and lu >= 5 and lu <= 8 or kung >= 9 and kung <= 12 and lu >= 13 and lu <= 16:  
    print("semifinal")
elif lu >= 1 and lu <= 4 and kung >= 5 and kung <= 8 or lu >= 9 and lu <= 12 and kung >= 13 and kung <= 16: 
    print("semifinal")
elif(kung <= 8 and lu > 8 or lu <= 8 and kung > 8):
    print("final")
else:
    print("quartas")

