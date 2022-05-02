'''
Fazer um programa que calcula a conta de água de uma residência, utilizando a tabela a seguir:
Tarifa Fixa R$ 15,05
Consumo Residencial     Água (R$/m³)    Esgoto (R$/m³)
1 a 10 m³                    6,08             4,26
11 a 15 m³                   7,79             5,45
16 a 20 m³                   7,93             5,55
21 a 25 m³                   8,75             6,13
26 a 30 m³                   10,76            7,53
31 a 50 m³                   12,9             9,03
Acima 50 m³                  14,21            9,95
As unidades de consumo são números inteiros que indicam m³. O valor total é calculado utilizando os 
valores de forma acumulativa, considerando o valor da unidade em cada faixa.
Por exemplo, para 18 m³, deve-se calcular o valor total computando o custo por unidade de consumo de 
cada faixa:
15.05 + (10*6.08 + 5*7.79 + 3*7.93) + (10*4.26 + 5*5.45 + 3*5.55) = 15.05 + 123.54 + 86.50 = 225.09
Após o cálculo do valor total, mostra-se o consumo, a tarifa fixa, o gasto com água, o gasto com 
esgoto, e o valor total a ser pago.

Entrada
Um número inteiro consumo, maior ou igual a zero, representando o consumo em m³.

Saída
O consumo, a tarifa fixa, o gasto com água, o gasto com esgoto, e o valor total a ser pago, conforme 
modelos dos exemplos de saída.
'''
consumo = int(input())

TarifaFIxa = 15.05
tarifa = 0
agua = 0
esgoto = 0

if consumo >= 0:

    if consumo == 0:
        tarifa = TarifaFIxa
    if consumo >= 1:
        if consumo <= 10:
            agua = consumo * 6.08
            esgoto = (consumo * 4.24)
            tarifa = TarifaFIxa + agua + esgoto
        else:
            agua = 10 * 6.08
            esgoto = 10 * 4.26
    if consumo > 10:
        if consumo <= 15:
            agua = agua + ((consumo - 10) * 7.79)
            esgoto = esgoto + ((consumo - 10) * 5.45)
            tarifa = TarifaFIxa + agua + esgoto
        else:
            agua = agua + (5 * 7.79)
            esgoto = esgoto + (5 * 5.45)
    if consumo > 15:
        if consumo <= 20:
            agua = agua + ((consumo - 15) * 7.93)
            esgoto = esgoto + ((consumo - 15) * 5.55)
            tarifa = TarifaFIxa + agua + esgoto
        else:
            agua = agua + (5 * 7.93)
            esgoto = esgoto + (5 * 5.55)
    if consumo > 20:
        if consumo <= 25:
            agua = agua + ((consumo - 20) * 8.75)
            esgoto = esgoto + ((consumo - 20) * 6.13)
            tarifa = TarifaFIxa + agua + esgoto
        else:
            agua = agua + (5 * 8.75)
            esgoto = esgoto + (5 * 6.13)
    if consumo > 25:
        if consumo <= 30:
            agua = agua + ((consumo - 25) * 10.76)
            esgoto = esgoto + ((consumo - 25) * 7.53)
            tarifa = TarifaFIxa + agua + esgoto
        else:
            agua = agua + (5 * 10.76)
            esgoto = esgoto + (5 * 7.53)
    if consumo > 30:
        if consumo <= 50:
            agua = agua + ((consumo - 30) * 12.9)
            esgoto = esgoto + ((consumo - 30) * 9.03)
            tarifa = TarifaFIxa + agua + esgoto
        else:
            agua = agua + (20 * 12.9)
            esgoto = esgoto + (20 * 9.03)
    if consumo > 50:
        agua = agua + ((consumo - 50) * 14.21)
        esgoto = esgoto + ((consumo - 50) * 9.95)
        tarifa = TarifaFIxa + agua + esgoto              


print("Consumo:",consumo,"metros cúbicos")
print("Total a pagar: R$ 15.05 + R$ %2f + R$ %2f = R$ %2f" %(agua,esgoto,tarifa))




