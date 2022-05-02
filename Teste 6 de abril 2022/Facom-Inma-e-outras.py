'''
Faça um programa que leia 5 códigos de curso de 5 estudantes da UFMS. Então conte quantos códigos 
são da Faculdade de Computação - Facom, quantos códigos são do Instituto de Matemática - Inma e 
quantos são de outras unidades. Mostre o resultado da contabilização.Os códigos dos cursos da Facom 
são: 1902: Análise e Desenvolvimento de Sistemas - Tecnologia; 
1904: Ciência da Computação - Bacharelado; 1905: Engenharia de Computação - Bacharelado; 
1906: Engenharia de Software - Bacharelado; 1907: Sistemas de Informação - Bacharelado. 
Os códigos de cursos do Inma são: 2201: Matemática - Licenciatura (Integral); 
2202: Matemática - Licenciatura (Noturno); 2203: Matemática - Bacharelado (Matutino); 
2291: Matemática - Licenciatura (A distância).

Entrada
Leia 5 números inteiros em uma mesma linha, separados por espaços, representado códigos de curso.

Saída
Mostre a quantidade de códigos de estudantes que são da Facom, do Inma e de outras unidades. Na 
primeira linha escreva "Facom: " seguido da quantidade de estudantes da Facom, na  segunda linha 
escreva "Inma: " seguido da quantidade de estudantes do Inma; e na terceira linha escreva  
"Outras unidades: " seguido da quantidade de estudantes que não são da Facom nem do Inma.
'''


codigos = input().split() #Um input que vai receber varias entradas e separar elas se baseando no que foi expecificado no caso um espaço em branco

# Variaveis a baixo vao separar as entradas que o input a variavel codigos recebeu e transformalas em numeros inteiros, como cada parte do input
#foi separada pelos espaços cada variavel vai pegar o input de cada casa sendo a primeira iniciando em "0" e a ultima na 5° casa 
codigo1 = int(codigos[0])
codigo2 = int(codigos[1])
codigo3 = int(codigos[2])
codigo4 = int(codigos[3])
codigo5 = int(codigos[4])

# Iniciando variavel com valor predefinido para fins de calculo futuro. como até então nenhum calculo foi feito temos ambas se iniciando em 0
#como nenhuma entrada recebida ainda
facom = 0
inma = 0


# Cada "if" abaixo vai verificar se o codigo vai corresponder ao codigo de algum curso da facom, caso seja correpondente vai somar a variavel facom
#que se iniciou com 0 e a cada if aceito vai ser somado + 1
if codigo1 == 1902 or codigo1 == 1904 or codigo1 == 1905 or codigo1 == 1906 or codigo1 == 1907:
    facom = facom + 1
if codigo2 == 1902 or codigo2 == 1904 or codigo2 == 1905 or codigo2 == 1906 or codigo2 == 1907:
    facom = facom + 1
if codigo3 == 1902 or codigo3 == 1904 or codigo3 == 1905 or codigo3 == 1906 or codigo3 == 1907:
    facom = facom + 1
if codigo4 == 1902 or codigo4 == 1904 or codigo4 == 1905 or codigo4 == 1906 or codigo4 == 1907:
    facom = facom + 1
if codigo5 == 1902 or codigo5 == 1904 or codigo5 == 1905 or codigo5 == 1906 or codigo5 == 1907:
    facom = facom + 1

#A mesma logica do metodo anterior mas agora aplicando os codigos dos cursos da Inma
if codigo1 == 2201 or codigo1 == 2202 or codigo1 == 2203 or codigo1 == 2291:
    inma = inma + 1
if codigo2 == 2201 or codigo2 == 2202 or codigo2 == 2203 or codigo2 == 2291:
    inma = inma + 1
if codigo3 == 2201 or codigo3 == 2202 or codigo3 == 2203 or codigo3 == 2291:
    inma = inma + 1
if codigo4 == 2201 or codigo4 == 2202 or codigo4 == 2203 or codigo4 == 2291:
    inma = inma + 1
if codigo5 == 2201 or codigo5 == 2202 or codigo5 == 2203 or codigo5 == 2291:
    inma = inma + 1

# Esse calculo simples vai chegar ao resultado de quantos codigos são de cursos diferentes do que se encontram na Facom e na Inma
#para isso foi apenas colocar o valor de entradas de codigo e diminuir pelo numero de cursos da Facom e Inma assim podendo chegar ao resultado
#de quantos codigos não são de cursos da Facom e Inma
outros = 5 - facom - inma

#print de cada resultado optido 
print ("Facom:", facom)
print ("Inma:", inma)
print ("Outras unidades:", outros)