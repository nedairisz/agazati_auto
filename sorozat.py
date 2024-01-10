"""
II/A, B, C:
           	23; 46; 10; 1; 6
II/D, E:
           	Az egyjegyűek száma : 2.  	
            A szamok.txt tartalma:
II/F:
            Az egyjegyűek száma : 2. 	
 
A.	Írasson ki a konzolra pontosvesszővel (;) elválasztva 5 lottószámot véletlen számsorozat alapján a mintának megfelelően 
    (ismétlődést nem kell kizárni)! (4p)
B.	A generált értékeket tárolja lista adatszerkezetben! (1p)
C.	A „;” jel csak az értékek között szerepeljen (a végén ne)! (2p)
D.	Írjon függvényt egyjegyuek_szama néven, amiben számolja meg, hogy hány olyan elem van, ami egyjegyű. 
    A visszatérési érték legyen egy egész szám! (3p)
E.	A egyjegyuek _szama függvény eredményét írassa ki a mintának megfelelően a konzolra, amit 
    konzol_kiir nevű metódusban fogalmazzon meg! (2p)
F.	A egyjegyuek _szama függvény eredményét írassa ki a mintának megfelelően a szamok.txt nevű fájlba, 
    amit file_kiir nevű metódusban fogalmazzon meg! (2p)

"""
import random

def szamok():
    lista=[]
    print(f"\t", end="")
    for i in range(0, 5, 1):
        szam=random.randint(1,90)
        lista.append(szam)

        if i == 4:
            print(szam)
        else:
            print(szam, end="; ")
        
    return lista

def egyjegyuek_szama(lista):
    gyujto=0
    print(f"\t", end="")
    for i in range(0, len(lista), 1):
        if lista[i]<10:
            gyujto+=1
    return gyujto

def konzol_kiir(gyujto):
    print(f"Az egyjegyűek száma: {gyujto}")

def file_kiir(gyujto):
    fajl=open("szamok.txt", "w", encoding="utf-8")
    fajl.write(f"II/F:\n\tAz egyjegyuek száma: {gyujto}")
    fajl.close()