#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Introduksjon til lister - min første liste!
"""

#En ordnet liste med ulike elementer i en bestemt rekkefølge.
personer = ["Terje", "Anna", "Jonas", "Johan", "Maja", "Oliwia", "Silje"]

print(f"Dette er min første liste: {personer}")

print(f"Type: {type(personer)}")

print(f"Denne listen har {len(personer)} elementer.")


#indeksering av listen for å hente ut elementer
første_person = personer[0]
andre_person = personer[1]
siste_person = personer[-1]

print(f"Første person i listen er {første_person}.")
print(f"Andre person er {andre_person}.")
print(f"Siste element i listen er {siste_person}")