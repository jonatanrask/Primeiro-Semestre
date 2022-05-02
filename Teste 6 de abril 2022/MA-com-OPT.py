'''
Faça um programa que calcule a média de aproveitamento (MA) da disciplina Algoritmos e Programação 
com aplicação da nota da prova optativa (OPT).
Após ler as notas da provas P1, P2 e P3 e do trabalho prático TP, seu programa deverá calcular 
MA = (80% da média de P1, P2 e P3) + (20% da nota do trabalho prático).
Se MA for menor que 6,0 deve-se mostrar a mensagem "O(A) estudante precisa fazer a prova optativa!" 
e ler a nota da prova optativa (OPT). E então deve-se substituir a menor nota MN, entre P1, P2 e P3, 
por OPT, se MN < OPT, e calcular novamente MA. O MA final deve ser mostrado, bem como a informação 
"Estudante aprovado(a)" se o(a) estudante foi aprovado(a)  (MA >= 6,0), e "Estudante reprovado(a)" 
se o(a) estudante foi reprovado(a) (MA < 6,0). Assume-se que o estudante não reprovará por faltas.

Entrada
A entrada consiste das notas da provas P1, P2 e P3 e do trabalho prático TP, na mesma linha, 
separadas por espaços. E na próxima linha, se MA for menor que 6,0, deve-se ler a nota da prova 
optativa (OPT). Todas as notas são em ponto flutuante (número real).

Saída
A saída será "O(A) estudante precisa fazer a prova optativa!", se o(a) estudante precisou fazer a 
prova optativa, em uma linha. Na próxima linha deve ser mostrada a mensagem "MA: " seguido do valor 
de MA com uma casa decimal em uma linha, seguida de "Estudante aprovado(a)" ou "Estudante 
reprovado(a)" na próxima linha.
'''

provas = input().split() #Um input que vai receber varias entradas e separar elas se baseando no que foi expecificado no caso um espaço em branco

'''
 Variaveis a baixo vao separar as entradas que o input a variavel codigos recebeu e transformalas em numeros inteiros, como cada parte do input
foi separada pelos espaços cada variavel vai pegar o input de cada casa sendo a primeira iniciando em "0" e a ultima na 5° casa 
'''
p1 = float(provas[0])
p2 = float(provas[1])
p3 = float(provas[2])
tp = float(provas[3])


ma = (((p1 + p2 + p3) / 3) * 0.8) + (tp * 0.2) #Calculo da media utilizando as variaveis


if ma >= 6: #Verificando se a media é igual ou maior ao valor necessario para ser aprovador
    print ("MA: {:.1f}".format(ma)) #caso seja igual vai imprimir a media   
    print("Estudante aprovado(a)") #e a mensagem de aprovação

else:#Verificando se a media é menor ao valor necessario para ser aprovador
    print("O(A) estudante precisa fazer a prova optativa!") #caso seja igual vai imprimir a mensagem dizendo que precisa da PO   
    opt = float(input()) #input recebendo a nota da prova optativa
    if opt < p1 and opt < p2 and opt < p3:
        p1 = p1
        p2 = p2
        p3 = p3
    elif p1 < p2 and p1 < p3: #if verificando se a prova 1 é a menor nota recebida
        p1 = opt # caso seja o valor da prova 1 vai ser substituido pelo valor da Prova Optativa
    elif p2 < p1 and p2 < p3: #elif verificando se a prova 2 é a menor nota recebida caso a codição anterior nao seja verdade
        p2 = opt # caso seja o valor da prova 2 vai ser substituido pelo valor da Prova Optativa
    elif p3 < p1 and p3 < p2:  #elif verificando se a prova 2 é a menor nota recebida caso as codições anteriores nao sejam verdade
        p3 = opt # caso seja o valor da prova 3 vai ser substituido pelo valor da Prova Optativa
    ma = (((p1 + p2 + p3) / 3) * 0.8) + (tp * 0.2) #novamente calculando a media agora com a menor nota substituida 
    if ma >= 6: #Verificando novamente se a nota é igual ou maior que o valor necessario para ser aprovado
        print ("MA: {:.1f}".format(ma)) #caso seja igual vai imprimir a media 
        print("Estudante aprovado(a)") #e a mensagem de aprovação
    else: #Caso a nova media não seja necessaria para ser aprovada
        print ("MA: {:.1f}".format(ma)) #vai imprimir a nova media
        print("Estudante reprovado(a)") #e a mensagem de reprovação


       