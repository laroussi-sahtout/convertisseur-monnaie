import requests 

from_currency = str(
    input("Quelle est la monnaie que vous souhaitez convertir  : ")).upper()

to_currency = str(
    input("En quelle vous souhaitez convertir : ")).upper()

montant = float(input("montant :"))

response = requests.get(
    f"https://api.frankfurter.app/latest?amount={montant}&from={from_currency}&to={to_currency}")


print (
    f"{montant} {from_currency} is {response.json()['rates'][to_currency]}{to_currency}")
