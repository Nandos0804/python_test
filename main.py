###############################
# APPUNTI
###############################

# MAIN
from ast import Str, literal_eval
from lib2to3.pgen2.token import NEWLINE
from pickle import NONE
from re import A, S
from turtle import clear
from typing import NoReturn

from numpy import iterable


print("Ciao Mondo")

# NUMERI interi
tipo_intero = 3

# NUMERI REALI
tipo_floating = 4.6
# OCCHIO! 0.1-0.2+0.3 NON FA 0, VEDERE COME PYTHON TRATTA I NUMERI

# STRINGA OVVIAMENTE
tipo_stringa = 'Pino'

# ORDINATA
tipo_lista = [10, 'Ciao', 50.5]

# COPPIA INFORMAZIONI
tipo_dizionario = {"nome": "Peppe"}

# SEQUENZA ORDINATA E IMMUTABILE
tipo_tupletta = ("Pino", 24, 'Maschio')

# COLLEZIONE NON ORDINATA DI OGGETTI UNICI
tipo_set = {"Moto", "Auto"}

# LOGICI BOOLEAN
# True False

tipo_boolean = True
maggiore = 1 > 2
uguale = 1 == 2

# NULLA, NESSUN VALORE, COME RETURN 0
nulla = None # si usa anche per assegnare dopo

#LISTA
nuovo_lista = [1,2,3]
nuova_lista_2 = [0] * 3
#DIZIONARIO
nuovo_dizionario = {'Nomi':['Giuseppe', 'Gaspare', 'Daneiele'],'Valore':1}
#TUPLE
nuovo_tuple = ('Chitarra', 'Violino','Chitarra')
#SET
nuovo_set = {1,2,3}

# ADDIZIONI
1 + 1
# SOTTRAZIONI
2 - 4
# MOLTIPLICAZIONI
3 * 6
# DIVISIONI
4 / 2
# MODULO (IL RESTO DELLA DIVISIONE PER ARRIVARE AL DIVIDENDO)
5 % 2
# POTENZA
2 ** 3

# ESEMPIO TASSE
stipendio =  1480
tasse_percentuale =  0.01
mie_tasse =  tasse_percentuale * stipendio

# ESEMPI STRINGHE SONO INDEXATE
scambio_primo = 'o " cosi'
scambio_secondo = "o ' cosi"
index_stringa =  "CIAO"

#INDEXING FUNZIONA ANCHE CON IL CONTO ALLA ROVESCI [-1] ULTIMO [-2] PENUTLIMO
stringa_esercizio = 'abcdefghijkl'
# [INIZIO: FINE], vuoto vuol dire fino a ultimo o dal primo
print(stringa_esercizio[3:])
# FINO A MA NON INCLUSIVO
print(stringa_esercizio[:4])
print(stringa_esercizio[3:6])
# DI QUANTI LETTERE DEVE ANDARE AVANTI A VOLTA
print(stringa_esercizio[::2])
print(stringa_esercizio[::4])

# REVERSE
print(stringa_esercizio[::-1])

# LE STRINGHE NON SONO MUTABILI
mio_nome = "Peppe"

# mio_nome[0] = 'B'
# questo da errore!!

# CONCATENAZIONE
x = 'Hello World'
y = x + " domani piove"
print(y)

# TRUNCATE AND CONCATE
no_iniziale = mio_nome[1:]
print(no_iniziale)
nome_swap = 'B' + no_iniziale
print(nome_swap)

# MOLTIPLICAZIONI STRINGHE
stella = 'x'
print(stella * 30)

# PRINT FORMATTATO
print("Prova {} e {} prova ".format(nome_swap, nome_swap), "INSERIRE")
print("Stagioni {1}{2}{3}{0}".format("Inverno","Estate","Primavera","Autunno"))
print("Stagioni {nome}{cognome}".format(cognome="Ernandez",nome="Giuseppe"))
print("Stagioni {nome}{nome}".format(cognome="Ernandez",nome="Giuseppe"))

# DIVISIONE CON CONTROLLO NUMERI 
# VARIABILE:NUMERODINUMERI.NUMERIDOPOLAVIRGOLA
divisione = 100 / 777
print("Risultato{r:1.5f}".format(r=divisione))

# STRINGHE LETTERARI PYTHON >3.6
print(f"Prova{divisione:1.5f}")

# LISTE
nomi = ['Jack', 'Ceccio', 'Michele', 'Sandro', 'Tommy', 'Giovanni', 'Pietro',
         'Giorgio', 'Master', 'Mirko', 'Alessio', 'Luigi', 'Betto',
         'Dario','Peppe']
cognomi = ['Calcara', 'Di Stefano', 'Ingrassia', 'Angileri', 'Fanara', 'Ernandez']
# LE LISTE POSSONO ESSERE MISTE, MA ALCUNI METODI POTREBBERO NON FUNZIONARE

# LUNGHEZZA
print(len(nomi))
# METODI
# STAMPA DA ELEMENTO X:Y:Z A ELEMENTO Y PROGREDENDO DI Z
print(nomi[1:])
nome_intero = nomi + cognomi
# LE LISTE SONO MUTABILI
nomi[0] = "Gaspare"
# AGGIUNGERE ALLA FINE
nomi.append('Ettore')
# POP RIMUOVE E MANDA IN OUT L'OGGETTO RIMOSSO
non_nome = nomi.pop()
# POP ACCETTA INDEX 
non_nome = nomi.pop(0)

# ORDINARE FUNZIONA SOLO COSI, POICHE RITORNA IL TIPO Null
nomi.sort()
nomi_ordinati = nomi
nomi.reverse()

# DIZIONARI 
# sono comodi quando è utile sapere un valore senza sapere la sua posizione
# come le liste ma non ordinate (senza indez)
# non si può riorganizzare (sort o simili)
listino_prezzi = {'Banane': 0.45, 'Mele': 0.60}
prezzo_banana = listino_prezzi['Banane']
print(prezzo_banana)

rubrica = {'Nomi':['Giuseppe', 'Gaspare', 'Daneiele'],
            'Cognomi':['Ernandez', 'Fanara', 'Giurlanda']}
cerca_nome =  rubrica['Nomi']

print(rubrica['Nomi'][1].upper())

# AGGIUNGERE VALORE CHIAVE
rubrica['Numero'] = 3387767141

print(rubrica)

# METODI UTILI
rubrica.keys()  # chiama chiavi
rubrica.values()    #chiama valori
rubrica.items() #chiama tutto

# TUPLE
# possono essere miste
# non sono mutabili, però metodi e applicazioni sono simili a liste

strumenti = ('Chitarra', 'Violino','Chitarra')
batteria = {'Cassa', 'Rullante'} #lista

strumenti.count('Chitarra') #quante volte compare
strumenti.index('Chitarra') #prima volta che compare
# sono utili perchè non si possono modificare, e quindi sono controllabili 
# più facilmente

# SET
# non è possibile avere duplicati

il_mio_set = set()
nuovo_set = {1,2,3}
il_mio_set.add(1)
il_mio_set.add(2)
il_mio_set.add(3)
# non si possono aggiungere doppioni

# per esempio fare diventare una lista un set permette di vedere solo i valori 
# non duplicati

nomi_non_duplicati_da_lista = set(nomi)

# OPERATORI DI COMPARAZIONE
# VERIFICA UGUAGLIANZA
2 == 2
# VERIFICA DIVERSITà
2 == 3
# VERIFICA MAGGIORE DI
2 > 1
# INCLUSIVO DI UGUGALIANZA
2 >= 1
# VERIFICA MINORE DI 
2 < 1
# INCLUSIVO DI UGUGALIANZA
2 <= 1

# OPERATORI LOGICI
# AND devono essere tutte le condizioni vere per ritornare True
1 < 2 < 3   # si può usare questo
(1 < 2) and (2 < 3)
# OR ne basta una vera
1 < 2 or 2
# NOT ritorna il negativo di quello che chiediamo
not (1 == 1)

localita = "Paceco"
# IF RISPETTARE LIVELLI
if (localita == "Trapani"): # la condizione deve essere vera per entrare nell'if
    print("Non mi piace!")
    #il codice va indendanto!
# ELIF RISPETTARE LIVELLI
elif (localita == "Paceco"):
    print("Casa")
    #il codice va indendanto!
# ELSE RISPETTARE LIVELLI
else:
    print("Dove sono?!")
    #il codice va indendanto!

# CICLI FOR (su ogetti iterabili)
# VARIABILE CHE ASSEGNO ALL'OGGETTO ITERABILE CORRENTE
#               ELEMENTO ITERABILE IN CUI CONTROLLO GLI ELEMENTI
for persona in nomi:
    print("Elemento iterabile: {tag_nome}".format(tag_nome = persona))

for cur_numb  in range(1,101):
    if (cur_numb % 2 == 0):
        print("Numero {attuale}: Pari!".format(attuale = cur_numb))
    else:
        print("Numero {attuale}: Dispari!".format(attuale = cur_numb))

# SE DOVESSE SERVIRE UN CICLO FOR SENZA LA VARIABILE PRE **IN**
for _ in "USIAMOSTRINGAPERITERARE":
    print("Conto", end= " ")
print()

# LISTA DI TUPLE
lista_di_tuple = [(1,2),(3,4),(5,6),(7,8)]
# COSI STAMPO SOLO LE TUPLE
for elements in lista_di_tuple:
    print(elements)
# POSSO SCENDERE ANCHE DI LIVELLO e fare TUPLE UNPACKING
for tupla_var_a, tupla_var_b in lista_di_tuple:
    print(tupla_var_a)
    print(tupla_var_b)

lista_di_tuple_b = [(1.,2.,3.),(4.,5.,6.),(7.,8.,9.)]
for var_a, var_b, var_c in lista_di_tuple_b:
    print(var_a)
    print(var_b)
    print(var_c)

# NEI DIZIONARI SI ITERA SOLO FRA LE CHIAVI, PER ANDARE AL VALUE DI UNA CHIAVE
for key in nuovo_dizionario:
    print(key)

for item in nuovo_dizionario.items(): #cosi ottengo key e value
    print(item)

for value in nuovo_dizionario.values(): #cosi ottengo key e value
    print(value)

# CICLI WHILE
count = 0
while(count < 5): # condizione booleana
    print("Il valore di count è {valore}".format(valore=count))
    count += 1
else:
    print(f"Uscito dal ciclo while con count a {count}")

# BREAK scappa dal ciclo completamente
stringa_test =  "Peppe"
for lettere in stringa_test:
    if lettere == "p":
        break
    print(lettere)


# CONTINUE salta fino a fine ciclo
for lettere in stringa_test:
    if lettere == "e":
        continue
    print(lettere)

# PASS volendo si può usare come place holder
x = [1,2,3]
for item in x:
    pass
