#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Stortingsvalg: hvert 4. år og sist gang var i 2021. Kan vi finne 
de andre årene det er og kommer til å være stortingsvalg?
"""

print("Bakover i tid:")
for år in range(2021,1960,-4):
    print(år)

print("Framover i tid:")
for år in range(2021,2051,4):
    print(år)