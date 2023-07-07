import random
import string

def generatorepassword ():

        scelta = input("vuoi che la password sia semplice o complessa?\n")

#qui manca il controllo delle risposte non previste

        if scelta == "semplice":

                lc = list(range(8))
                numero = 8
                for i in range (numero):

                        lc[i] = (random.choice(string.ascii_letters))

        if scelta == "complessa":

                lc = list(range(20))
                numero = 20
                for i in range (numero):

                        lc[i] = (random.choice(string.ascii_letters))

        password = "".join(lc)

        print (password)
        return password

generatorepassword()
