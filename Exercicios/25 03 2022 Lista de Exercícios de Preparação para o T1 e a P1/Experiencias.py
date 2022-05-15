'''
Maria acabou de iniciar seu curso de graduação na faculdade de medicina e precisa de sua ajuda para organizar os experimentos de um laboratório o qual ela é responsável. Ela quer saber no final do ano, quantas cobaias foram utilizadas no laboratório e o percentual de cada tipo de cobaia utilizada.

Este laboratório em especial utiliza três tipos de cobaias: sapos, ratos e coelhos. Para obter estas informações, ela sabe exatamente o número de experimentos que foram realizados, o tipo de cobaia utilizada e a quantidade de cobaias utilizadas em cada experimento.

Entrada
A primeira linha de entrada contém um valor inteiro N que indica os vários casos de teste que vem a seguir. Cada caso de teste contém um inteiro Quantia (1 ≤ Quantia ≤ 15) que representa a quantidade de cobaias utilizadas e um caractere Tipo ('C', 'R' ou 'S'), indicando o tipo de cobaia (R:Rato S:Sapo C:Coelho).

Saída
Apresente o total de cobaias utilizadas, o total de cada tipo de cobaia utilizada e o percentual de cada uma em relação ao total de cobaias utilizadas, sendo que o percentual deve ser apresentado com dois dígitos após o ponto.
'''
sapo = 0
rato = 0
coelho = 0

testes = int(input())

for i in range(0, testes, 1):
    cobaias = input().split()
    quantidade = int(cobaias[0])
    animal = cobaias[1]

    if animal == "S":
        sapo = sapo + quantidade
    elif animal == "R":
        rato = rato + quantidade
    elif animal == "C":
        coelho = coelho + quantidade

total = sapo + coelho + rato
PorcentagemSapo = (sapo * 100) / total
PorcentagemCoelho = (coelho * 100) / total
PorcentagemRato = (rato * 100) / total

print("Total:", total ,"cobaias")
print("Total de coelhos:", coelho)
print("Total de ratos:", rato)
print("Total de sapos:", sapo)
print("Percentual de coelhos: {:.2f} %".format(PorcentagemCoelho))
print("Percentual de ratos: {:.2f} %".format(PorcentagemRato))
print("Percentual de sapos: {:.2f} %".format(PorcentagemSapo))
