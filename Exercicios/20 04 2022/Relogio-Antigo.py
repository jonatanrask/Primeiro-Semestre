'''
Ezequiel possui um relógio muito antigo e valioso, mas algumas características dele foram perdidas 
com o passar do tempo. Os ponteiros ainda marcam as horas e os minutos corretamente, mas seus 
marcadores e números se tornaram ilegíveis.

Ezequiel utiliza um instrumento auxiliar para observar os ângulos formados pelos ponteiros de 
hora e de minuto. Ele pede para você ajudá-lo escrevendo um programa que indica a hora e o minuto 
do momento da medição. Considere que às 00:00 os dois ângulos medidos são iguais a zero e que ambos 
os ponteiros só se movimentam quando se completa uma unidade de tempo (hora ou minuto) correspondente.

Entrada
A entrada consiste em vários casos de teste e é finalizada pelo fim de arquivo (EOF). Cada linha 
corresponde a um caso de teste e contém dois valores inteiros h e m (0 ≤ h, m < 360) que são, 
respectivamente, os ângulos medidos sobre os ponteiros de hora e de minuto.

Saída
Para cada caso de teste, imprima uma única linha com o valor da hora e do minuto no formato 
"hh:mm" (sem aspas), conforme pode ser observado nos exemplos.
'''

'''
Arquivo para usar no exercicio = teste.txt

comando para testar no terminal:

Windows PowerShell: Get-Content teste.txt | python Relogio-Antigo.py
Linux: Python3 Relogio-Antigo.py < teste.txt
'''

while(True):

    try:

        hora = input().split()
        horas = int(hora[0])
        minutos = int(hora[1])

        if horas < 90:
            horas = (horas / 60) * 10
        else:
            horas = (horas / 60) * 2
        minutos = (minutos / 60) * 10

        if horas >= 10 and minutos >= 10:
            print("{:.0f}:{:.0f}".format(horas, minutos))
        elif horas < 10 and minutos >= 10:
            print("0{:.0f}:{:.0f}".format(horas, minutos))
        elif horas >= 10 and minutos < 10:
            print("{:.0f}:0{:.0f}".format(horas, minutos))
        elif horas < 10 and minutos < 10:
            print("0{:.0f}:0{:.0f}".format(horas, minutos))
    except EOFError:
        break