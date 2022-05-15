'''
Timelimit: 1
Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica,
 e informe-o expresso no formato horas:minutos:segundos.

Entrada
O arquivo de entrada contém um valor inteiro N.

Saída
Imprima o tempo lido no arquivo de entrada (segundos), convertido para horas:minutos:segundos, 
conforme exemplo fornecido.
'''
n = int(input())
horas = n // 3600
segundos = n % 3600
minutos = segundos // 60
segundosFinal = segundos % 60 
print("{:.0f}:{:.0f}:{:.0f}".format(horas,minutos,segundosFinal))