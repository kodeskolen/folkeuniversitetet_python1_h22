#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Programmet tildeler tilgjengelige drakter til spillerene i listen.
"""

from random import shuffle

personer = ["Terje", "Anna", "Jonas", "Johan", "Maja", "Oliwia", "Silje"]
draktnummere = [8, 11, 27, 29, 40, 67, 71, 83, 90, 98]


shuffle(personer)
shuffle(draktnummere)

print(personer)
print(draktnummere)

index = 0
while index < len(personer):
    print(f"{personer[index]} skal få draktnummer {draktnummere[index]}.")
    index = index + 1

print()
print("De resterende draktnummerene er:")
while index < len(draktnummere):
    print(f"Draktnummer {draktnummere[index]}.")
    index = index + 1