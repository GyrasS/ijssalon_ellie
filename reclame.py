from algemene_functies import mijn_functie_2


def aanbieding_1(smaak,prijs,korting):
    prijs_na_korting = prijs * (1 - korting)
    uitvoer = f"Vandaag in de aanbieding: Emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {prijs_na_korting} euro."
    return uitvoer
print("5. ",aanbieding_1("aardbei",4,0.1))

print("------------------------")

def inkomsten_totaal(inkomsten, btw):
    totaal = inkomsten[0]+inkomsten[1]+inkomsten[2]+inkomsten[3]+inkomsten[4]+inkomsten[5]+inkomsten[6]
    bedrag = totaal / 100 * btw
    return f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {bedrag} euro btw betaald dient te worden."
inkomsten_totaal([220, 430, 125, 160, 205, 90, 345], 0.09)
print("6-7. ", inkomsten_totaal([220, 430, 125, 160, 205, 90, 345], 0.09))

print("------------------------")

def laag_en_hoog(mijn_lijst):
    nieuwe_lijst = [min(mijn_lijst), max(mijn_lijst)]
    return nieuwe_lijst
print("8. ", laag_en_hoog([220, 430, 125, 160, 205, 90, 345]))

print("------------------------")

def gemiddelde(mijn_lijst):
    antwrd = mijn_lijst[0] + mijn_lijst[1] + mijn_lijst[2] + mijn_lijst[3] + mijn_lijst[4] + mijn_lijst[5] + mijn_lijst[6]
    return antwrd / 7
print("9-10. ", "De gemiddelde inkomsten deze week zijn", gemiddelde([220, 430, 125, 160, 205, 90, 345]), "euro.")

print("------------------------")

def meervoudig(invoer_lijst):
   global laag_en_hoog
   return laag_en_hoog(invoer_lijst)
print("11. ", meervoudig([10, 5, 3, 2, 1, 2, 9]))

print("------------------------")

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer
print("12. ", combinatie([10, 5, 3, 2, 1, 2, 9]))