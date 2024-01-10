"""
I/A:
Autó  neve: Opel Corsa
Gyártási dátum: 2022
 
I/B:
Ez az Opel Corsa átlagos korú.

A.	Kérje be az alábbi adatokat a fenti mintának megfelelően:
    Autó  neve és gyártás éve!  (2p)
B.	A program az adatbekérés után írasson ki egy szöveget az alábbiak alapján!
    Amennyiben az autó gyártási éve ez évi, akkor írja ki, „friss gyártás”.
    Amennyiben 2000 előtt gyártották az autót, írja ki: „öreg autó”
    Minden más esetben: „átlagos korú”. (4p)
    A mintának megfelelően jelenítette meg az eredményt, és kérte be az adatokat. (1p)
"""

def bekeres():
    nev:str=str(input("Autó  neve: "))
    gy:int=int(input("Gyártási dátum: "))
    print("I/B:")
    if gy==2024:
        print(f"Ez a {nev} friss gyártás.")
    elif gy<2000:
        print(f"Ez a {nev} öreg autó")
    else:
        print(f"Ez a {nev} átlagos korú")