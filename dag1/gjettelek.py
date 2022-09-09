"""
Programmet velger et tilfeldig tall mellom 1 og 100.
Spilleren gjetter på et tall.
Spilleren får vite om gjettet er for lavt eller for høyt.
Man kan prøve flere ganger til man gjetter riktig.
Programmet teller antall forsøk. 
"""

from random import randint

fasit = randint(1,100)
gjett = int(input("Gjett på et tall mellom 1 og 100."))

forsøk = 1

while gjett != fasit:
    if gjett < fasit:
        print("Du har gjettet for lavt.")
    elif gjett > fasit:
        print("Du har gjettet for høyt.")
    gjett = int(input("Gjett en gang til: "))
    forsøk = forsøk + 1

print("Helt riktig!")
print(f"Du har gjettet {forsøk} ganger.")




