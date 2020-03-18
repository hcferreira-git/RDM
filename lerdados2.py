import csv

with open ( 'C:/Temp/Dados.csv' , newline = '' ) as csvfile :
    spamreader = csv . reader ( csvfile , delimiter = ';' , quotechar = '|' )


for row in spamreader :
    #print ( ', ' . join ( row ))
    print ( row )
