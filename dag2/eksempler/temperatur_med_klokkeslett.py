#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Vi ser på en liste med temperaturer. Klarer vi finne maksimum og gjennomsnitt?
"""


temperaturer = [-15.5,  -18.0,  -17.4,  -18.5,  -19.9,  -20.9,
                -21.5,  -22.0,  -20.5,  -18.6,  -15.6,  -13.5,
                -10.5,   -9.0,   -7.9,   -7.1,   -9.1,  -12.2,
                -14.8,  -16.5,  -16.8,  -15.3,  -17.6,  -19.7]
#temperaturen klokken XX.00 fra 00.00 til 23.00

maks_temperatur = temperaturer[0]
kl_når_maks = 0
gj_snitt = 0

for kl in range(24):
    print(f"Klokken {kl} er det {temperaturer[kl]} grader.")
    
    if temperaturer[kl] > maks_temperatur:
        maks_temperatur = temperaturer[kl]
        kl_når_maks = kl
    
    gj_snitt = gj_snitt + temperaturer[kl]

print(f"Gjennomsnittstemperaturen er {gj_snitt/len(temperaturer):.1f} grader.")

print(f"Klokken {kl_når_maks} var det varmest,\
      da var det {maks_temperatur} grader.")