'''
Pedrinho está organizando um evento em sua Universidade. O evento deverá ser no mês de Abril, iniciando e terminando dentro do mês. O problema é que Pedrinho quer calcular o tempo que o evento vai durar, uma vez que ele sabe quando inicia e quando termina o evento.

Sabendo que o evento pode durar de poucos segundos a vários dias, você deverá ajudar Pedrinho a calcular a duração deste evento.

Entrada
Como entrada, na primeira linha vai haver a descrição “Dia”, seguido de um espaço e o dia do mês no qual o evento vai começar. Na linha seguinte, será informado o momento no qual o evento vai iniciar, no formato hh : mm : ss. Na terceira e quarta linha de entrada haverá outra informação no mesmo formato das duas primeiras linhas, indicando o término do evento.

Saída
Na saída, deve ser apresentada a duração do evento, no seguinte formato:

W dia(s)
X hora(s)
Y minuto(s)
Z segundo(s)

Obs: Considere que o evento do caso de teste para o problema tem duração mínima de 1 minuto.
'''
dia1 = input().split("Dia ")
data1 = input().split(" : ")

PrimeiroDia = int(dia1[1])
hora1 = int(data1[0])
minuto1 = int(data1[1])
segundo1 = int(data1[2])

dia2 = input().split("Dia ")
data2 = input().split(" : ")

SegundoDia = int(dia2[1])
hora2 = int(data2[0])
minuto2 = int(data2[1])
segundo2 = int(data2[2])

total = (SegundoDia * 86400 + hora2 * 3600 + minuto2 * 60 + segundo2) - (PrimeiroDia * 86400 + hora1 * 3600 + minuto1 * 60 + segundo1)  
dia = total // 86400
hora = total % 86400
minuto = hora % 3600
segundo = minuto % 60
hora = hora // 3600

minuto = minuto // 60

print(dia,"dia(s)")
print(hora,"hora(s)")
print(minuto,"minuto(s)")
print(segundo, "segundo(s)")




