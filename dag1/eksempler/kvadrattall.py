#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hva er det minste kvadrattallet som er større enn eller lik 1000?
kvadrattall n, n*n
"""

n = 0

while n*n < 100:
    n = n+1
    print(f"{n}*{n} = {n*n}")

print("Løkken er slutt!")