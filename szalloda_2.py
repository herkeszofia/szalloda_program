'''
javítási feladatok:
- ne lehessen ugyanoda ugyanarra az időpontra többször is foglalni
- a foglalás törlésekor sorszámot kell megadni,de a foglalások lista objektumokat tárol,
de jobb lenne, ha a sorszámokat tárolna a lista, a foglalás osztálynak sorszám adattagja.
- a foglalások listázásakor adja is vissza ezt az azonosítót, hogy tudjuk, hogy
melyiket szeretnénk törölni
'''

from datetime import datetime

class Szoba:
    def __init__(self, ar, szobaszam):
        self.ar = ar
        self.szobaszam = szobaszam

class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(ar=6000, szobaszam=szobaszam)

class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(ar=8000, szobaszam=szobaszam)

class Foglalas:
    sorszam_counter = 1

    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum
        self.sorszam = Foglalas.sorszam_counter
        Foglalas.sorszam_counter += 1

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = []
        self.engedelyezett_idoszak = (datetime(2024, 9, 10), datetime(2024, 11, 20))

    def uj_szoba(self, szoba):
        self.szobak.append(szoba)

    def foglal(self, szobaszam, datum):
        if self.engedelyezett_idoszak[0] <= datum <= self.engedelyezett_idoszak[1]:
            for szoba in self.szobak:
                if szoba.szobaszam == szobaszam:
                    foglalas = Foglalas(szoba, datum)
                    if foglalas in self.foglalasok:
                        print("Ez az időpont már foglalt!")
                        return None
                    else:
                        self.foglalasok.append(foglalas)
                        return szoba.ar
            return None
        else:
            print("A megadott időpont nem esik az engedélyezett időszakba!")
            return None

    def foglalas_lemondasa(self, sorszam):
        for foglalas in self.foglalasok:
            if foglalas.sorszam == sorszam:
                self.foglalasok.remove(foglalas)
                print("Foglalás sikeresen törölve.")
                return
        print("Nincs ilyen sorszámú foglalás.")

    def osszes_foglalas_listazasa(self):
        for foglalas in self.foglalasok:
            print(f"Sorszám: {foglalas.sorszam}, Szobaszám: {foglalas.szoba.szobaszam}, Dátum: {foglalas.datum.strftime('%Y-%m-%d')}")

def rendszer_feltoltes(szalloda):
    egyagyas1 = EgyagyasSzoba(szobaszam=101)
    egyagyas2 = EgyagyasSzoba(szobaszam=102)
    ketagyas1 = KetagyasSzoba(szobaszam=103)
    szalloda.uj_szoba(egyagyas1)
    szalloda.uj_szoba(egyagyas2)
    szalloda.uj_szoba(ketagyas1)


def main():
    szalloda = Szalloda(nev="Alpesi Hotel")

    rendszer_feltoltes(szalloda)

    print("Szobák száma: 101,102,103")
    print(f"\nFoglalási időszak: {szalloda.engedelyezett_idoszak[0].strftime('%Y-%m-%d')} - {szalloda.engedelyezett_idoszak[1].strftime('%Y-%m-%d')}")

    while True:
        print("\nVálassz műveletet:")
        print("1. Szoba foglalása")
        print("2. Foglalás lemondása")
        print("3. Foglalások listázása")
        print("4. Kilépés")

        valasztas = input("Kérem válasszon: ")

        if valasztas == "1":
            szobaszam = int(input("Kérem adja meg a szobaszámot: "))
            datum_str = input("Kérem adja meg a foglalás dátumát (YYYY-MM-DD formátumban): ")
            datum = datetime.strptime(datum_str, "%Y-%m-%d")
            ar = szalloda.foglal(szobaszam, datum)
            if ar:
                print(f"Sikeres foglalás! Ár: {ar}")
            else:
                print("Nincs ilyen szoba, a megadott időpont nem engedélyezett, vagy már foglalt a szoba ezen a dátumon.")

        elif valasztas == "2":
            if szalloda.foglalasok:
                print("Jelenlegi foglalások:")
                szalloda.osszes_foglalas_listazasa()
                sorszam = int(input("Kérem adja meg a lemondani kívánt foglalás sorszámát: "))
                szalloda.foglalas_lemondasa(sorszam)
            else:
                print("Jelenleg nincs foglalás.")

        elif valasztas == "3":
            if szalloda.foglalasok:
                print("Jelenlegi foglalások:")
                szalloda.osszes_foglalas_listazasa()
            else:
                print("Jelenleg nincs foglalás.")

        elif valasztas == "4":
            print("Kilépés...")
            break

        else:
            print("Hibás választás! Kérem válasszon újra.")

if __name__ == "__main__":
    main()
