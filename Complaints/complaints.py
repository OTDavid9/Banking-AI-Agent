import json 
question = input("Enter your query here : ")

def complaints(complaints_query=question):
    
    complaints_url = "www.wemabank.com/complaints"

    # Return the response from Azure Cognitive Search
    return  json.dumps(complaints_url)