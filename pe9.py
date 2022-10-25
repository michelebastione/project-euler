##Sappaiamo che a<b<c, a+b+c=1000 e infine che naturalmente a^2+b^2=c^2; quello a cui vogliamo arrivare è il prodotto abc;
##Partendo da queste informazioni, la prima cosa che potremmo fare è
##creare una funzione che, dati 2 numeri a<b in input, restituisce la c che soddisfa le regole precedenti. Proviamoci:

import math                                                 ##importiamo il modulo math, che contiene la funzione sqrt() per la radice quadrata
def terna_pitagorica(x,y):                                  ##definiamo il nome della funzione e le variabili x e y che gli andremo a mettere in input
    z=math.sqrt(x**2+y**2)                                  ##creiamo una variabile c appunto tramite la regola delle triplette pitagoriche 
    return  (x+y+z==1000, z)                                ##restituisce una coppia di valori: il primo è un booleano, ossia True se è vera la condizione enunciata...
                                                            ##...altrimenti restituisce False; il secondo valore invece è il numero z, che ci servirà solo una volta.

##A questo punto abbiamo una funzione che crea una terna pitagorica a partire da due numeri. Però ci serve di iterare questi due numeri.
##Per fare ciò torniamo a considerare le regole da soddisfare: possiamo tranquillamente tranquillamente considerare a+b<500, poichè se così non fosse avremmo...
##...anche a+b>=500 che implica c>=500, siccome a<b<c, ma allora sarebbe a+b+c>1000 e questo è un assurdo, dunque necessariamente a+b<500;
##Allo stesso modo non potrà che essere a<250, altrimenti a+b>500, e questo non è possibile;
##Dunque adesso non ci resta che iterare tutte le combinazioni possibili rimaste:


for a in range(1,250):                                      ##per tutte le a tra 1 e 250 non incluso(ricorda le regole del range):
    for b in range(a+1,500):                                ##per tutte le b tra a+1 e 500:
        if terna_pitagorica(a,b)[0]:                        ##se il primo valore della funzione terna_pitagorica(a,b) è True:
            print("abc=",a*b*terna_pitagorica(a,b)[1])      ##stampa il prodotto tra a,b e il secondo valore della funzione terna_pitagorica(a,b).


##N.B: io ho usato una funzione per essere più ordinato, ma nukka ti vieta di fare quei calcoli all'interno del ciclo for se preferisci.
