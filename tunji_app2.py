from flask import Flask, render_template, request, jsonify
from openai import AzureOpenAI
import sqlite3
import json
import requests
from tools import tools_listing
from prompts import system_message

app = Flask(__name__)

azure_openai_endpoint = "https://tunji-service.openai.azure.com/openai/deployments/tunji-model/chat/completions?api-version=2023-07-01-preview"
azure_openai_api_key = "1c5f09b472cd44cf8d28542f9ae25c03"
azure_openai_api_version = "2023-05-15"

client = AzureOpenAI(
    azure_endpoint="https://tunji-service.openai.azure.com",
    api_key="1c5f09b472cd44cf8d28542f9ae25c03",
    api_version="2023-07-01-preview"
)

# Initialize an empty list to store chat history
chat_history = []

@app.route('/')
def index():
    return render_template('index2.html', chat_history=chat_history)

@app.route('/chat', methods=['POST'])
def chat():
    question = request.form.get('question')

    def Check_balance(email=question):
        # Connect to the SQLite database
        conn = sqlite3.connect('bank_database.db')
        cursor = conn.cursor()

        cursor.execute("SELECT account_balance FROM customers WHERE email = ?", (email,))
        balance = cursor.fetchone()

        if balance is not None:
            return json.dumps(f"Account Balance for {email}: ${balance[0]}")
        else:
            return json.dumps(f"Invalid email: {email}")

    def complaints(complaints_query=question):
        complaints_url = "https://drive.google.com/file/d/1AlUXgJoRmNqQJr9tLE0mr5DazH5Bp7ez/view?usp=drive_link"
        return json.dumps({"Lodge your complaint using this link": complaints_url, "complaints_query": complaints_query})

    def knowledge_base(enquiry_query=question):
        search_service_name = "tunji-ai-search-3"
        search_api_key = "nsWEQDTKDiP9ZTXpt3z6Z2nm7IAtcvCyhKOk6Fgh5YAzSeDNAPiy"
        index_name = "yes"
        api_version = "2023-07-01-preview"

        search_url = f"https://{search_service_name}.search.windows.net/indexes/{index_name}/docs?api-version={api_version}"
        headers = {"Content-Type": "application/json", "api-key": search_api_key}

        response = requests.get(search_url, headers=headers, params={"search": enquiry_query})

        return json.dumps(response.json()['value'][0]['content'])

    def top_up_airtime(service_provider=question, amount=question):
        service_provider_list = ['MTN', 'AIRTEL', 'GLO', 'ETISALAT']
        service_provider = service_provider.upper()
        service_provider_flag = 0
        amount = amount

        if service_provider.upper() in service_provider_list:
            service_provider_flag = 1
            return json.dumps("The transaction request was successful")
        else:
            return json.dumps("The Service provider you chose is not available")

    def handle_unknown_query(unknown_query=question):
        return json.dumps({'unknown': str("'I CAN'T ANSWER")})

    def run_conversation():
        messages = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": question}
        ]
        tools = tools_listing
        response = client.chat.completions.create(
            model="tunji-model",
            messages=messages,
            tools=tools,
            tool_choice="auto",  # auto is default, but we'll be explicit
        )
        response_message = response.choices[0].message
        tool_calls = response_message.tool_calls

        print(tool_calls, "\n")

        if tool_calls:
            available_functions = {
                "complaints": complaints,
                "Check_balance": Check_balance,
                "knowledge_base": knowledge_base,
                "top_up_airtime": top_up_airtime,
                None: handle_unknown_query
            }

            messages.append(response_message)

            for tool_call in tool_calls:
                function_name = tool_call.function.name
                function_to_call = available_functions[function_name]
                function_args = json.loads(tool_call.function.arguments)

                if function_name == "knowledge_base":
                    function_response = function_to_call(
                        enquiry_query=function_args.get("enquiry_query"),
                    )
                elif function_name == "Check_balance":
                    function_response = function_to_call(
                        email=function_args.get("email"),
                    )
                elif function_name == "complaints":
                    function_response = function_to_call(
                        complaints_query=function_args.get("complaints_query"),
                    )
                elif function_name == "top_up_airtime":
                    function_response = function_to_call(
                        service_provider=function_args.get("service_provider"),
                        amount=function_args.get("amount"),
                    )
                elif function_name == None:
                    function_response = function_to_call(
                        unknown_query=function_args.get("unknown_query"),
                    )

                messages.append(
                    {
                        "tool_call_id": tool_call.id,
                        "role": "tool",
                        "name": function_name,
                        "content": function_response,
                    }
                )

            second_response = client.chat.completions.create(
                model="tunji-model",
                messages=messages,
            )
            print(second_response)

            return second_response.choices[0].message.content

    response = run_conversation()

    # Append the current conversation to the chat history
    chat_history.append({'question': question, 'response': response})

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
