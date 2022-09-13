#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hvordan legge til elementer i listen med "append".
"""



personer = []

#print(len(personer))

navn = input("Skriv inn et navn: (eller 'slutt' for å slutte)")

while navn.lower() != "slutt":
    personer.append(navn)
    navn = input("Skriv inn et navn: (eller 'slutt' for å slutte)")


person = "Georg"

print(f"Personen {person} er i listen: {person in personer}")

if person in personer:
    print("Heia, Georg!")