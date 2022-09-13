#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Vi regner på renter med en for-løkke:
"""

saldo = 10000
rente = 2.8 #% per år
vekstfaktor = 1 + rente/100

for år in range(10):
    saldo =  saldo*vekstfaktor
    print(f"Etter {år+1} år er saldoen {saldo:.2f} kroner.")