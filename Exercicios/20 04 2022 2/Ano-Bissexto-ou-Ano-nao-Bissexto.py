'''
A antiga raça de Gulamatu é muito avançada no seu esquema de cálculo dos anos. Eles entendem o que é 
ano bissexto (ano que é divisível por 4 e não é divisível por 100, com a ressalva de que ano que são 
divisíveis por 400 são também anos bissextos.), E têm também alguns anos que ocorrem alguns 
festivais. Um deles é o festival Huluculu (acontece em anos divisíveis por 15) e o festival 
Bulukulu (acontece em anos divisíveis por 55 desde que também seja um ano bissexto). Dado um ano 
você terá de indicar quais propriedades este ano tem. Se o ano não é ano bissexto e nem ano de 
festival imprima a linha 'This is an ordinary year.', ou seja, que é um ano comum. A ordem de 
impressão das propriedades dos anos (se presente) é leap year -> huluculu -> bulukulu.

Entrada
A entrada conterá vários casos de teste. Cada caso de teste consiste de uma linha contendo um ano que 
nunca será menor do que 2000 (para evitar regras anteriores diferentes para anos bissextos), mas pode 
ter mais do que 1.000 dígitos. O final da entrada é determinado por fim de arquivo (EOF).

Saída
Para cada entrada, imprima as diferentes propriedades dos anos em diferentes linhas de acordo com a 
descrição anterior e os exemplos fornecidos abaixo.  Uma linha em branco deve separar cada caso de 
teste de saída. Note que existem quatro diferentes propriedades. Obviamente não deverá ter uma linha 
em branco após o último caso de teste.
'''
'''
Arquivo para usar no exercicio = teste.txt

comando para testar no terminal:

Windows PowerShell: Get-Content teste.txt | python Ano-Bissexto-ou-Ano-nao-Bissexto.py
Linux: Python3 Ano-Bissexto-ou-Ano-nao-Bissexto.py < teste.txt
'''
ano = 0
linha = 0
while(True):
    verificacao = 0
    try:
        ano = int(input())
        if linha != 0:
            if ano != 0:
                print("")
            else:
                linha = linha + 1
        elif linha == 0:
            linha = linha + 1
        if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 and ano % 100 == 0:
            verificacao = 1
        if ano % 15 == 0:
            verificacao = verificacao + 2
        if ano % 55 == 0 and verificacao == 1 or ano % 55 == 0 and verificacao == 3:
            verificacao = verificacao + 3
        if verificacao == 0:
            print("This is an ordinary year.")
        elif verificacao == 1:
            print("This is leap year.")
        elif verificacao == 2:
            print("This is huluculu festival year.")
        elif verificacao == 3:
            print("This is leap year.")
            print("This is huluculu festival year.")
        elif verificacao == 4:
            print("This is leap year.")
            print("This is bulukulu festival year.")
        elif verificacao == 6:
            print("This is leap year.")
            print("This is huluculu festival year.")
            print("This is bulukulu festival year.")

    except EOFError:
        break