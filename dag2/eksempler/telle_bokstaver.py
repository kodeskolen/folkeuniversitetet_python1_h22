#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Behandle litt tekst med for-løkker. 
"""

#Eks 1: løkke gjennom en og en bokstav
navn = "Andreas"
for bokstav in navn:
    print(bokstav)
    
#Eks 2: Telle antall i navnet (teller alt som ikke er mellomrom)
navn = "Johan Emil"
#print(f"Det er {len(navn)} bokstaver i '{navn}'") #teller alt
antall = 0
for tegn in navn:
    if tegn != " ":
        antall += 1 #antall = antall + 1

print(f"Det er {antall} bokstaver i navnet {navn}.")


#Eks 3: Telle kun bokstaver
navn = "Johan-Emil"
bokstaver = "ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ"

antall = 0
for tegn in navn:
    if tegn.upper() in bokstaver:
        antall += 1

print(f"Det er {antall} bokstaver i navnet {navn}.")
