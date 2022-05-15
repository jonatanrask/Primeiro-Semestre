'''
Leia 3 valores de ponto flutuante A, B e C e ordene-os em ordem decrescente, de modo que o lado A 
representa o maior dos 3 lados. A seguir, determine o tipo de triângulo que estes três lados 
formam, com base nos seguintes casos, sempre escrevendo uma mensagem adequada:
se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO
se A2 = B2 + C2, apresente a mensagem: TRIANGULO RETANGULO
se A2 > B2 + C2, apresente a mensagem: TRIANGULO OBTUSANGULO
se A2 < B2 + C2, apresente a mensagem: TRIANGULO ACUTANGULO
se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO
se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES
Entrada
A entrada contem três valores de ponto flutuante de dupla precisão A (0 < A) , B (0 < B) e C 
(0 < C).

Saída
Imprima todas as classificações do triângulo especificado na entrada.
'''

valores = input().split()
primeiro = float(valores[0])
segundo = float(valores[1])
terceiro = float(valores[2])



a = primeiro
if a < segundo:
    a = segundo
if a < terceiro:
    a = terceiro

c = segundo
if c > primeiro:
    c = primeiro
if c > terceiro:
    c = terceiro
b = terceiro
if a == c:
    b = a
else:
    if primeiro == a and segundo == a or terceiro == a and segundo == a or primeiro == a and terceiro == a:
        b = a
    elif primeiro == c and segundo == c or terceiro == c and segundo == c or primeiro == c and terceiro == c:
        b = c
    else:
        if a > primeiro > c:
            b = primeiro
        elif a > segundo > c:
            b = segundo
        else:
            b = terceiro
if a >= b + c:
    print("NAO FORMA TRIANGULO")
elif a * a == b * b + c * c:
    print("TRIANGULO RETANGULO")
elif  a * a > b * b + c * c:
    print("TRIANGULO OBTUSANGULO")
elif a * a < b * b + c * c:
    print("TRIANGULO ACUTANGULO")
if a == b == c:
    print("TRIANGULO EQUILATERO")
elif a == b or a == c or b == a or b == c:
    print("TRIANGULO ISOSCELES")