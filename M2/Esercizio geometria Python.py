print ("oggi calcoliamo il perimetro di diverse figure geometriche")

print ("iniziamo con il quadrato")

lato = int (input ("inserisci la misura del lato di un quadrato: "))

print ("calcoliamo il perimetro un cerchio")

raggio = int (input ("inserisci la misura del raggio: "))

print ("infine il perimetro di un rettangolo")

base = int (input ("inserisci la base: "))
altezza = int (input ("inserisci l'altezza: "))

pq = lato*4
circ = ((2*3.14)*raggio)
pr = (base*2)+(altezza*2)

print ("il perimetro del quadrato è: " + str(pq)) 

print ("la circonferenza del cerchio è: " + str(circ)) 

print ("il perimetro del rettangolo è: " + str(pr)) 
