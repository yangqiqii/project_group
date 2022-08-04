# Import modules to run code
import requests
import json

# Assign api key to the variable "api_key"
api_key = "RGC6YA5ZJFKM6OPR"
# Use f-string to insert api key into the url
# Assign the url to "url"
url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=demo{api_key}"
# Use requests.get() to read "url" and assign it to "response"
response = requests.get(url)
# Use .json() to retrieve data from response and save it as data
data = response.json()
# Use data.keys() to retrieve the keys of the dictionary
# Use json.dumps(data["Realtime Currency Exchange Rate"], indent = 4) to read the dictionary in a more readable format
# Extract the exchange rate, convert it into a float and assign it to "forex"
forex = float(data["Realtime Currency Exchange Rate"]["5. Exchange Rate"])

# Define the function api()
def api():
    # Documentation of the function api()
    """
    Function does not require parameter 
    Function returns real time currency conversion rate from USD to SGD
    """
<<<<<<< HEAD
    # Assign api key to the variaable "api_key"
    api_key = "RGC6YA5ZJFKM6OPR"
    # Use f-string to insert api key into the url
    # Assign the url to "url"
    url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=demo{api_key}"
    # Use requests.get() to read "url" ans assign it to "response"
=======
    # Assign api key to the variable "api_key"
    api_key = "RGC6YA5ZJFKM6OPR"
    # Use f-string to insert api key into the url
    # Assign the url to "url
    url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=demo{api_key}"
    # Use requests.get() to read "url" and assign it to "response"
>>>>>>> 0d475fd20a385b6d1a625fd0cb0c669e63fa66c5
    response = requests.get(url)
    # Use .json() to retrieve data from response and save it as data
    data = response.json()
    # Use data.keys() to retrieve the keys of the dictionary
<<<<<<< HEAD
    # Use json.dumps(data["Realtime Currency Exchange Rate"], indent = 4) to read the dictionary in a more readable format
=======
    # Use json.dumps(data["Realtime Currency Exchange Rate"], indent = 4) to read the disctionary in a more readable format
>>>>>>> 0d475fd20a385b6d1a625fd0cb0c669e63fa66c5
    # Extract the exchange rate, convert it into a float and assign it to "forex"
    forex = float(data["Realtime Currency Exchange Rate"]["5. Exchange Rate"])
    # Return summary statement for currency exchange rate
    return f"[REAL TIME CURRENCY CONVERSION RATE] USD1 = SGD{forex}"
# Execute the function
<<<<<<< HEAD
print(api())
=======
print(api())
>>>>>>> 0d475fd20a385b6d1a625fd0cb0c669e63fa66c5
