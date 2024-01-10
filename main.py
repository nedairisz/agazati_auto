import bevezetes
import sorozat
import autom

"""
print("I/A:")
bevezetes.bekeres()

print("II/A, B, C:")
lista=sorozat.szamok()
print("II/D, E:")
gyujto=sorozat.egyjegyuek_szama(lista)
sorozat.konzol_kiir(gyujto)
print("II/F")
sorozat.file_kiir(gyujto)"""

lista=autom.beolvas()
print("III/Flotta:")
szamuk=autom.flotta(lista)
print(f"Autók száma: {(szamuk)}")
print("III/Legfiatalabb")
legf_index=autom.legfiatalabb(lista)
print(lista[legf_index].nev, lista[legf_index].gysz)
print("III/Átlag kor")