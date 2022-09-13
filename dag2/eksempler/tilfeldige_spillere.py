#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Her lager vi en liste med navn på spillere på et fotballag, som vi først 
skriver i tilfeldig rekkefølge.

Deretter gir vi et spiller-nummer til hver spiller.
"""

from random import shuffle

personer = ["Terje", "Anna", "Jonas", "Johan", "Maja", "Oliwia", "Silje"]


personer.sort()

print(f"Spillerene i alfabetisk rekkefølge: {personer}")

shuffle(personer)

print(f"Spillerene i tilfeldig rekkefølge: {personer}")

index = 0

while index < len(personer):
    print(f"Spiller nummer {index+1} er { personer[index] }.")
    index = index + 1