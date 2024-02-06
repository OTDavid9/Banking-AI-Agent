import sqlite3
import json
import requests
import os
from dotenv import load_dotenv
load_dotenv()


def Check_balance(email):
    # Connect to the SQLite database
    conn = sqlite3.connect('bank_database2.db')

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Fetch the account balance based on the email
    cursor.execute("SELECT account_balance FROM customers WHERE email = ?", (email,))
    balance = cursor.fetchone()

    # Check if the email exists in the database
    if balance is not None:
        return json.dumps(f"Account Balance for {email}: ${balance[0]}")
    else:
        return json.dumps(f"Invalid email: {email}")


def complaints(complaints_query):
    
    complaints_url = "https://wemabank.com/complaints"

    # Return the response from Azure Cognitive Search
    return  json.dumps({"Lodge your complaint using this link":complaints_url, "complaints_query": complaints_query})

def knowledge_base(enquiry_query):
    
     # Azure Cognitive Search configuration
    search_service_name = os.getenv('search_service_name')
    search_api_key = os.getenv('search_api_key')
    index_name = os.getenv('index_name')
    # api_version = "2023-11-01"
    api_version = "2023-07-01-preview"

    search_url = f"https://{search_service_name}.search.windows.net/indexes/{index_name}/docs?api-version={api_version}"
    headers = {"Content-Type": "application/json", "api-key": search_api_key}

    # Make a request to Azure Cognitive Search
    response = requests.get(search_url, headers=headers, params={"search": enquiry_query})

    # Return the response from Azure Cognitive Search
    return  json.dumps(response.json()['value'][0]['content'])

def top_up_airtime(service_provider, amount):
    service_provider_list= ['MTN','AIRTEL','GLO','ETISALAT']
    service_provider= service_provider.upper()
    service_provider_flag = 0
    amount = amount

    if service_provider.upper() in service_provider_list:
        service_provider_flag = 1
        return json.dumps("The transaction request was successful")
    else:
        return json.dumps("The Service provider you chose is not available")
    


def handle_unknown_query(unknown_query):
    """
    This function handles unknown user queries.
    The user's query that is not recognized as coginitive or url"
    """
    
    # return json.dumps(f"Sorry, I don't understand the query: {unknown_query}")
    return json.dumps({'unknown': str("'I CAN'T ANSWER")})


def check_token(email,token):
     # Connect to the SQLite database
    conn = sqlite3.connect('bank_database2.db')

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Fetch the account balance based on the email
    cursor.execute("SELECT token FROM customers WHERE email = ?", (email,))
    user = cursor.fetchone()

    # Check if the email exists in the database
    if user is not None:
        print(user)
        token2 = user[0]
        if token2 == int(token):
            return json.dumps(f"The authentication was successful")
        else:
            return json.dumps(f"The authentication was not successful maybe your token is incorrect")
    else:
        return json.dumps(f"Invalid email: {email}")
    


