'''
programa que vai receber 2 inteiros, um para variavel m outro para variavel n e mostrar todos o inteiros entre eles
inclusive ele; e depois mostrar a soma de todos os numero mostrados
'''




teste = 1 #Para manter o while rodando
while (teste == 1): #Enquanto o teste for igual a 1 o teste vai ser repetido
    vetor = [] #Iniciando a lista e tbm resetando ela
    numeros = "" #Iniciando uma string
    resultado = 0 #Iniciando a variavel int
    mn = input().split() #recebe um entrada com 2 valores e um espaço e pega os 2 valores apenas
    m = int(mn[0]) #O primeiro valor transformado em inteiro
    n = int(mn[1]) #O segundo valor transformado em inteiro

    if (m > 0 and n > 0): # caso m n forem maior que 0
        if m > n: #Verifica quando é o maior valor para saber em que ponto começar os calculos
            for i in range(n, m + 1, 1): #Verificando todos valores do menor valor ao maior
                vetor.append(i) #Adicionando os valores a uma lista
            for numero in vetor: #Verificando cada valor na lista
                if numero == vetor[0]: #Caso seja o primeiro valor da lista
                    numeros = str(numero) + " " #Transforma esse valor em string concatena a um espaço e é adicionado a uma variavel
                else: #Caso nao seja o primeiro
                    numeros = numeros + str(numero) + " " #Transforma a proxima variavel em string e adicona o espaço a frente
                resultado = resultado + numero #Aqui é somado cada valor verificado pelo for int
            print(numeros + "Sum=" + str(resultado)) #Printa o resultado final analisado
        elif n > m: #Verifica quando é o maior valor para saber em que ponto começar os calculos
            for i in range(m, n + 1, 1): #Verificando todos valores do menor valor ao maior
                vetor.append(i) #Adicionando os valores a uma lista
            for numero in vetor: #Verificando cada valor na lista
                if numero == vetor[0]: #Caso seja o primeiro valor da lista
                    numeros = str(numero) + " " #Transforma esse valor em string concatena a um espaço e é adicionado a uma variavel
                else: #Caso nao seja o primeiro
                    numeros = numeros + str(numero) + " " #Transforma a proxima variavel em string e adicona o espaço a frente
                resultado = resultado + numero #Aqui é somado cada valor verificado pelo for int
            print(numeros + "Sum=" + str(resultado)) #Printa o resultado final analisado
        elif m == n: #Caso for igual
            print(m,"Sum={d}".format(m + n)) #Então não a valores entre ele e so mostra o valor e a soma dos 2
    else: #caso não for 0 ou menor
        teste = 0 # o teste é atualizado e o while para
