import requests

brew = input("Select city ")

response = requests.get(f"https://api.openbrewerydb.org/breweries?by_city={brew}")

if (response.status_code != requests.codes.ok):
    print("Something went wrong!")
else:
    print(response.json())


