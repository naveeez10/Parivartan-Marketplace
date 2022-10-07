from requests import Request, Session
import json

url = "https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest"


currencies = ['ethereum','solana','polygon']

id = {
    'ethereum' : '1027',
    'solana' : '5426',
    'polygon' : '3890'
}

headers = {
    "Accepts" : "application/json",
    'X-CMC_PRO_API_KEY' : 'f65ee482-05fa-43ac-857b-a1d6b3590e68' 
}


for currency in currencies:
    
    session = Session()
    session.headers.update(headers)

    
    parameters = {
    'slug' : currency,
    'convert' : 'INR'
    }
    
    response = session.get(url,params=parameters)
    data = json.loads(response.text)
    
    # print(data)
    val = round(data['data'][id[currency]]['quote']['INR']['price'],2)
    print(f"{currency}'s price in INR : {val}")
