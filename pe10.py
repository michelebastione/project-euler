def is_prime(n,L):
    """ Creiamo una funzione che ci dica se un numero è primo o meno:
'n' - è il numero che vogliamo testare;
'L' - è la lista dei fattori che vogliamo testare. """

    for i in L:                 #per ogni elemento nella lista L:
        if i>n**0.5:            #se è maggiore della radice quadrata di n:
            break               #interrompe il ciclo;
        if n%i==0:              #se i divide n: 
            return False        #restituisce False
    return True                 #altrimenti restitituisce True


def somma_primi(n):
    """ Creiamo una funzione che sommi tutti i numeri primi minori di una data quantità:
'n' - è il numero dove vogliamo arrivare a controllare. """
    
    P=[2]                       #inizializziamo una lista contenente (per adesso) solo il numero 2
    for i in range(3,n+1):      #per ogni elemento compreso tra 3 e n:
        if is_prime(i,P):       #usiamo la funzione 'is_prime' per controllare che sia un numero primo (sulla lista di fattori P):
            P.append(i)         #se primo lo aggiunge alla lista;
    return sum(P)               #infine restituisce la somma degli elementi di P


print(somma_primi(2000000))     #stampiamo la somma dei primi minori minori di 2.000.000
