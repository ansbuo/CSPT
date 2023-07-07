
def lpar ():                                  #funzione lunghezza delle parole 
        lb = list(range(n))
        for l in range (n):

                lb[l] = len(lista[l])

        print (lb)
        return n  


n = int (input("quante parole vuoi inserire?\n"))

lista = list(range(n))                          #inizializzazione lista

print ("inserisci le parole\n")

for l in range (n):
        lista[l] = input (" ")


print (lista)
lpar()


