#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sjekke alder på kino!
"""

alder = int(input("Hei! Hvor gammel er du? "))


if alder >= 15:
    print("Velkommen på kino!")
    
elif alder >= 12:
    er_voksen_med = input("Har du med en voksen? (ja/nei) ")
    if er_voksen_med == "ja":
        print("Velkommen på kino med voksen!")
    else:
        print("Du er ikke gammel nok, kom tilbake om ", 15 - alder, "år!")
else:
    print("Du er ikke gammel nok! Kom tilbake om", 15 - alder, "år!")


