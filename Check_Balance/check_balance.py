import sqlite3

def Check_balance(email, password):
    # Connect to the SQLite database
    conn = sqlite3.connect('bank_database.db')

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Fetch the account balance based on the email and password
    cursor.execute("SELECT account_balance FROM customers WHERE email = ? AND password = ?", (email, password))
    balance = cursor.fetchone()

    # Check if the email and password combination exists in the database
    if balance:
        return print(f"Account Balance for {email}: ${balance[0]}")
    else:
        return (f"Invalid email or password for {email}.")

    # Close the database connection
    conn.close()

# Example usage
Check_balance('jane.smith@email.com', 'janeSmith@123')
Check_balance("john.doe@email.com",'johnDoe@123')














# import sqlite3

# def Check_balance(email, password):
#     # Connect to the SQLite database
#     conn = sqlite3.connect('bank_database.db')

#     # Create a cursor object to execute SQL queries
#     cursor = conn.cursor()

#     # Fetch the account balance based on the email and password
#     cursor.execute("SELECT account_balance FROM customers WHERE email = ? AND password = ?", (email, password))
#     balance = cursor.fetchone()

#     # Check if the email and password combination exists in the database
#     if balance:
#         return print(f"Account Balance for {email}: ${balance[0]}")
#     else:
#         return (f"Invalid email or password for {email}.")

#     # Close the database connection
#     conn.close()

# # Example usage
# Check_balance('jane.smith@email.com', 'janeSmith@123')
# Check_balance("john.doe@email.com",'johnDoe@123')

