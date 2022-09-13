#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Vi ser på for-løkker og tallrekker!

Tallrekker med while:
tall = 1

while tall <= 10:
    print(tall)
    tall = tall + 1
"""

print("tallrekke fra 1 til og med 10")
for tall in range(1,11):
    print(tall)

print("Tallrekke fra 5 til 10")
for tall in range(5,11):
    print(tall)

print("Oddetallene i rekkken")
for tall in range(1,11,2):
    print(tall)

summen = 0
for tall in range(1,11):
    print(f"I denne iterasjonen er tall={tall} og \
          summen={summen}, og \
              summen settes til {summen+tall}")
    summen = summen + tall

print(f"Summen av tallene fra 1 til 10 er {summen}.")
    
print(list(range(1,11)))
    
    
    
    