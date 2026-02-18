ukoly = []

def hlavni_menu():
    print()
    print("Správce úkolů - Hlavní menu")
    print("1. Přidat nový úkol")
    print("2. Zobrazit všechny úkoly")
    print("3. Odstranit úkol")
    print("4. Konec programu")
    print("Vyberte možnost (1-4): ", end="")


def pridat_ukol(ukoly):
    print()
    nazev = input("Zadejte název úkolu: ").strip()
    if nazev == "":
        print("Úkol nelze přidat — název je prázdný.")
        return
    popis = input("Zadejte popis úkolu: ").strip()
    if popis == "":
        print("Popis nelze přidat — popis je prázdný.")
        return    
    ukol = {
        "nazev": nazev,
        "popis": popis
    }

    ukoly.append(ukol)
    print(f"Úkol '{nazev}' byl přidán.")
    print()
    hlavni_menu()


def zobrazit_ukoly(ukoly):
    if not ukoly:
        print()
        print("Žádné úkoly nejsou uložené.") 
        return

    print("\nSeznam úkolů:")
    for i, ukol in enumerate(ukoly, start=1):
            print(f"{i}. {ukol['nazev']} - {ukol['popis']}")
        


def odstranit_ukol(ukoly):
    if not ukoly:
        print()
        print("Není co mazat — seznam je prázdný.")
        hlavni_menu()
        return
    print("\nSeznam úkolů:")
    for i, ukol in enumerate(ukoly, start=1):
            print(f"{i}. {ukol['nazev']} - {ukol['popis']}")
    try:
        print()
        cislo = int(input("Zadejte číslo úkolu, který chcete odstranit: ").strip())
        if 1 <= cislo <= len(ukoly):
            smazany = ukoly.pop(cislo - 1)
            print(f"Úkol '{smazany['nazev']}' byl odstraněn.")
            print()
            hlavni_menu()
        else:
            print("Neplatné číslo úkolu.")
            print()
            hlavni_menu()   
    except ValueError:
        print("Musíte zadat číslo.")
        hlavni_menu()


def main():
    hlavni_menu()
    while True:
        volba = input().strip()

        if volba == "1":
            pridat_ukol(ukoly)
        elif volba == "2":
            zobrazit_ukoly(ukoly)
            hlavni_menu()
        elif volba == "3":
            odstranit_ukol(ukoly)
        elif volba == "4":
            print()
            print("Konec programu.")
            break
        else:
            print("Neplatná volba, zkuste to znovu.")


if __name__ == "__main__":
    main()
