"""
III/Flotta:
         Autók száma: 7.
III/Legfiatalabb
         A legfiatalabb autó: Opel Corsa (2019).
III/Átlag kor
	Az autók átlagos kora: 15.14 év.

A.	Olvassa be osztály segítségével (utóbbit hozza létre külön modulban) a auto.txt fájlból a autók adatait, és tárolja el összetett adatszerkezetben, ami elősegíti a további feladatok könnyű megoldását! Ügyeljen arra, hogy az állomány első sora az adatok fejlécét tartalmazza! (7p)
B.	Készíts függvényt flotta néven, amely visszaadja az autók számát a mintának megfelelően, majd írasd ki  a konzolra a mintának megfelelően! (2p)
C.	Add meg a legfiatalabb autó nevét a mintának megfelelően a konzolra írva!! (4p)
D.	Írassa ki konzolra a mintának megfelelően az autók átlagos korát! (4p)
"""
from Auto import Auto

def beolvas():
    fajl=open("auto.txt", "r", encoding="utf-8")
    fajl.readline()
    nyers_lista=fajl.readlines()
    fajl.close

    lista=[]
    for i in range(0, len(nyers_lista), 1):
        sorok=nyers_lista[i]
        sor_adat=sorok.strip().split("$")
        nev=(sor_adat[0])
        gysz=(sor_adat[1])
        auto=Auto(nev, gysz)
        lista.append(auto)
        print(lista[i].nev, lista[i].gysz)
    return lista

def flotta(lista):
    szamuk=len(lista)
    return szamuk

def legfiatalabb(lista):
    legf_index=0
    for i in range(0,len(lista), 1):
        if lista[legf_index].gysz < lista[i].gysz:
            legf_index=i
    return legf_index

def atlag_kor():
    