articol = "Tribunalul Alba a respins joi candidatura la Senat a primarului din Zlatna, Silviu Ponoran, aflat pe prima poziţie pe lista PNL pentru parlamentare, decizia instanţei putând fi atacată la Curtea de Apel Alba Iulia."
lungime = len(articol)
prima_pare = articol[:lungime // 2]
a_doua_parte = articol[lungime // 2:]
prima_pare = prima_pare.strip().upper()
a_doua_parte = a_doua_parte[ ::-1]
a_doua_parte = a_doua_parte.capitalize()
punctuatie = ['.' , ',' , '!' , '?']
for caracter in punctuatie: a_doua_parte = a_doua_parte.replace(caracter, ' ')
rezultat_final = prima_pare + ' ' + a_doua_parte
print(rezultat_final)