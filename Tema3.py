meniu = ['papanasi'] * 10 + ['ceafa'] * 3 + ["guias"] * 6
preturi = [["papanasi", 7], ["ceafa", 10], ["guias", 5]]
studenti = ["Liviu", "Ion", "George", "Ana", "Florica"]
comenzi = ["guias", "ceafa", "ceafa", "papanasi", "ceafa"]
tavi = ["tava"] * 7
istoric_comenzi = []
print("COMENZI:")
for student in list(studenti):
    comanda = comenzi.pop(0)
    tavi.pop()
    meniu.remove(comanda)
    istoric_comenzi.append(comanda)
    print(f"{student} a comandat {comanda}.")
print("INVENTAR:")
numar_guias = istoric_comenzi.count("guias")
numar_ceafa = istoric_comenzi.count("ceafa")
numar_papanasi = istoric_comenzi.count("papanasi")
print(f"Sau comandat {numar_guias} guias, {numar_ceafa} cefe si {numar_papanasi} papanasi")
print(f"Mai sunt {len(tavi)} tavi.")
print(f"A mai ramas ceafa: {'ceafa' in meniu} ")
print(f"Au mai ramas papanasi: {'papanasi' in meniu} ")
print(f"A mai ramas guias: {'guias' in meniu} ")
print("FINANTE:")
incasari = sum([pret for comanda in istoric_comenzi for produs, pret in preturi if comanda == produs])
print(f"Cantina a încasat: {incasari} lei.")
produse_ieftine = [produs for produs in preturi if produs[1] <= 7]
print(f"Produse care costă cel mult 7 lei: {produse_ieftine}")