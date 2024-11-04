import random
cuvinte = ["python", "programare", "calculator", "date", "algoritm"]
cuvant_de_ghicit = random.choice(cuvinte)
progres = ["_" for _ in cuvant_de_ghicit]
incercari_ramase = 6
litere_incercate = []
print(" ".join(progres))
print(f"Încercări rămase: {incercari_ramase}")
while incercari_ramase > 0 and "_" in progres:
    litera = input("Introdu o literă: ").lower()
    litera_valida = len(litera) == 1 and litera.isalpha()
    litera_neincercata = litera in litere_incercate
    if litera_valida is False:
        print("Eroare: Te rog introdu o singură literă validă.")
        continue
    if litera_neincercata:
        print("Ai încercat deja această literă. Încearcă alta.")
        continue
    litere_incercate.append(litera)
    if litera in cuvant_de_ghicit:
        for index, caracter in enumerate(cuvant_de_ghicit):
            if caracter == litera:
                progres[index] = litera
        print("Corect!")
    else:
        incercari_ramase -= 1
        print(f"Litera '{litera}' nu este în cuvânt.")

    print("Progres: " + " ".join(progres))
    print(f"Încercări rămase: {incercari_ramase}")
litere_complete = "_" in progres
if litere_complete is False:
    print(f"Felicitări! Ai ghicit cuvântul: {cuvant_de_ghicit}")
else:
    print(f"Ai pierdut! Cuvântul era: {cuvant_de_ghicit}")