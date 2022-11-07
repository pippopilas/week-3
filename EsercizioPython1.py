"""
Si scriva un programma in Python che permetta, in base alla scelta dell'utente, di calcolare il perimetro di un: 
-QUADRATO (perimetro = lato*4)
-CERCHIO (circonferenza = 2*pi greco*r)
-RETTANGOLO (perimetro = base*2 + altezza*2)
"""
import math #importo la libreria math per l'utilizzo del pi greco

def menu ():
        print ("Scegli cosa calcolare: \n \n1) Perimetro quadrato \n2) Circonferenza cerchio \n3) Perimetro rettangolo\n")

def quadrato (): #definisco la funzione quadrato
        x = float (input ("\nInserisci il valore del lato del quadrato: ")) #gli input mi permetteranno di inserire dei valori 
        print ("\nIl perimetro del quadrato con lato x è",x*4)

def cerchio (): #definisco la funzione cerchio
        x = float (input ("\nInserisci il valore del raggio del cerchio: "))
        print ("\nLa circonferenza del cerchio è", 2*math.pi*x)

def rettangolo (): #definisco la funzione rettangolo
        x = float (input ("\nInserisci il valore della base: "))  
        y = float (input ("\nInserisci il valore dell'altezza: "))
        print ("\nIl perimetro del rettangolo è", x*2 + y*2)


menu () #richiamerò la funzione menu che mi darà la possibilità di inserire un input numerico per poi scegliere la funzione da richiamare
z = int (input ()) 

if z == 1:
        quadrato () #se premo 1 andrò a richiamare la funzione quadrato definita sopra

elif z == 2:
        cerchio() #se premo 2 andrò a richiamare la funzione cerchio definita sopra

elif z == 3:
        rettangolo () #se premo 3 andrò a richiamare la funzione rettangolo definita sopra

else:
        print ("\nInserisci un input valido") #premendo qualsiasi altro tasto avrò un errore e il programma si chiuderà