'''
Neste problema, você deverá ler 3 palavras que definem o tipo de animal possível segundo
 o esquema abaixo, da esquerda para a direita.  Em seguida conclua qual dos animais seguintes 
 foi escolhido, através das três palavras fornecidas.

 https://resources.beecrowd.com.br/gallery/images/problems/UOJ_1049_b.png

 Entrada
A entrada contém 3 palavras, uma em cada linha, necessárias para identificar o animal segundo a 
figura acima, com todas as letras minúsculas.

Saída
Imprima o nome do animal correspondente à entrada fornecida.
'''

vertebra = input()
tipo = input()
alimento = input()

if vertebra == "vertebrado":
    if tipo == "ave":
        if alimento == "carnivoro":
            print("aguia")
        elif alimento == "onivoro":
            print("pomba")
    elif tipo == "mamifero":
        if alimento == "onivoro":
            print("homem")
        elif alimento == "herbivoro":
            print("vaca")
elif vertebra == "invertebrado":
    if tipo == "inseto":
        if alimento == "hematofago":
            print("pulga")
        elif alimento == "herbivoro":
            print("lagarta")
    elif tipo == "anelideo":
        if alimento == "hematofago":
            print("sanguessuga")
        elif alimento == "onivoro":
            print("minhoca")