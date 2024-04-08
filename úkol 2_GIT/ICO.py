import requests


ico = input("Zadejte IČO subjektu: ")


url = f"https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/{ico}"


response = requests.get(url)


if response.status_code == 200:
   
    data = response.json()
    

    obchodni_jmeno = data["obchodniJmeno"]
    adresa_sidla = data["sidlo"]["textovaAdresa"]
    

    print(obchodni_jmeno)
    print(adresa_sidla)
else:
    print("Chyba při zpracování požadavku. Zkontrolujte, zda jste zadali správné IČO a zkuste to znovu.")

  