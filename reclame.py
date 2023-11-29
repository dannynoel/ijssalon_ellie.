<<<<<<< HEAD
from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs , korting):
        berekening = prijs - (prijs * korting)
        uitvoer = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {berekening} euro."
        return uitvoer

def inkomsten_totaal(ma, di, wo, do, vr, za, zo):
        inkomsten = sum ((ma, di, wo, do, vr, za, zo))
        bedrag = inkomsten * 0.09
        uitvoer = f"Het bedrag van alle inkomsten van deze week is {inkomsten} euro waarover {bedrag} euro btw betaald dient te worden."
        return uitvoer

def laag_en_hoog(ma, di, wo, do, vr, za, zo):
       mijn_lijst = (ma, di, wo, do, vr, za, zo)
       hoog=max(mijn_lijst)
       laag=min(mijn_lijst)
       laag_en_hoog=[hoog, laag]
       return laag_en_hoog

def gemiddelde(ma, di, wo, do, vr, za, zo):
        mijn_lijst = (ma, di, wo, do, vr, za, zo)
        bedrag = sum(mijn_lijst) / len(mijn_lijst)
        return f"De gemiddelde inkomsten van deze week zijn {bedrag} euro."

def meervoudig (ma, di, wo, do, vr, za, zo):
        invoer_lijst = (ma, di, wo, do, vr, za, zo)
        hoog=max(invoer_lijst)
        laag=min(invoer_lijst)
        hoog_en_laag=[hoog, laag]
        return hoog_en_laag

def combinatie(invoer_lijst_2):
        korte_lijst= meervoudig (invoer_lijst_2)
        uitvoer = mijn_functie2(korte_lijst[0], korte_lijst [1])
        return uitvoer


print(aanbieding_1 ("aardbei", 4, 0.1))
print(inkomsten_totaal (220, 430, 125, 160, 205, 90, 345))
print(laag_en_hoog (220, 430, 125, 160, 205, 90, 345))
print(gemiddelde (220, 430, 125, 160, 205, 90, 345))
print(meervoudig (10,5,3,2,1,2,9))
=======
from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs , korting):
        berekening = prijs - (prijs * korting)
        uitvoer = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {berekening} euro."
        return uitvoer

def inkomsten_totaal(ma, di, wo, do, vr, za, zo):
        inkomsten = sum ((ma, di, wo, do, vr, za, zo))
        bedrag = inkomsten * 0.09
        uitvoer = f"Het bedrag van alle inkomsten van deze week is {inkomsten} euro waarover {bedrag} euro btw betaald dient te worden."
        return uitvoer

def laag_en_hoog(ma, di, wo, do, vr, za, zo):
       mijn_lijst = (ma, di, wo, do, vr, za, zo)
       hoog=max(mijn_lijst)
       laag=min(mijn_lijst)
       laag_en_hoog=[hoog, laag]
       return laag_en_hoog

def gemiddelde(ma, di, wo, do, vr, za, zo):
        mijn_lijst = (ma, di, wo, do, vr, za, zo)
        bedrag = sum(mijn_lijst) / len(mijn_lijst)
        return f"De gemiddelde inkomsten van deze week zijn {bedrag} euro."

def meervoudig (ma, di, wo, do, vr, za, zo):
        invoer_lijst = (ma, di, wo, do, vr, za, zo)
        hoog=max(invoer_lijst)
        laag=min(invoer_lijst)
        hoog_en_laag=[hoog, laag]
        return hoog_en_laag

def combinatie(invoer_lijst_2):
        korte_lijst= combinatie (invoer_lijst_2)
        uitvoer = mijn_functie2(korte_lijst[0], korte_lijst [1])
        return uitvoer


print(aanbieding_1 ("aardbei", 4, 0.1))
print(inkomsten_totaal (220, 430, 125, 160, 205, 90, 345))
print(laag_en_hoog (220, 430, 125, 160, 205, 90, 345))
print(gemiddelde (220, 430, 125, 160, 205, 90, 345))
print(meervoudig (10,5,3,2,1,2,9))
>>>>>>> ce2b61817447c1e7a7078c6f4bb502e797f08f9a
print(combinatie)