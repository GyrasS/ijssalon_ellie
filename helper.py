def decoreer(tekst=""):
    lengte = len(tekst) + 4
    print()
    print(lengte * "*")
    print(f"* {tekst} *")
    print(lengte * "*")
    print()

def fooi_pp(bedrag, personen):
    bedrag_pp = bedrag / personen
    return f"Het bedrag per persoon is {bedrag_pp} euro."

def onderstreep(tekst = ""):
    uit = []
    a = "=" * len(tekst)
    uit.append(tekst)
    uit.append(a)
    return uit

def som(dict):
    s = 0
    for k in dict.values():
        s += k
    return s