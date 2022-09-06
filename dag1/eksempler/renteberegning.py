#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Eksempel på en løkke hvor vi regner med årlige renter!
"""

saldo = 10000 #kr
rente = 2.8 #%
vekstfaktor = 1 + rente/100

år = 0

#Etter hvor mange år, har vi 20000 kr i saldo?

while saldo < 20000:
    saldo = saldo*vekstfaktor
    år = år + 1
    print(f"Etter {år} år har du {saldo} kr på konto.")