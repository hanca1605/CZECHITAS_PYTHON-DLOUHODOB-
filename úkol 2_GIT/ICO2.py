import requests

def vyhledat_subjekty(nazev_subjektu):
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
    }
    data = '{"obchodniJmeno": "' + nazev_subjektu + '"}'
    res = requests.post("https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat", headers=headers, data=data)
    if res.status_code == 200:
        data = res.json()
        pocet_celkem = data.get('pocetCelkem', 0)
       
        subjekty = data.get('ekonomickeSubjekty', [])
        print(f"Nalezeno subjektů: {pocet_celkem}")
        for subjekt in subjekty:
            obchodni_jmeno = subjekt.get('obchodniJmeno', '')
            identifikacni_cislo = subjekt.get('ico', '')
            print(f"{obchodni_jmeno}, {identifikacni_cislo}")
    else:
        print("Chyba při komunikaci s API.")

def main():
    nazev_subjektu = input("Zadej název subjektu, který chceš vyhledat: ")
    vyhledat_subjekty(nazev_subjektu)

if __name__ == "__main__":
    main()

