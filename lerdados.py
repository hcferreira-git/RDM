import csv

arq_listas = open('C:/Temp/Dados.csv', 'r')
lista = arq_listas.read().split('\n')
arq_listas.close()

print(lista)

for r in lista:
    print(r)