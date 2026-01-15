import sqlite3
def hello():
    print("Hello World")


def get_user(user_id):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # ❌ SQL Injection vulnerability
    query = "SELECT * FROM users WHERE id = " + user_id
    cursor.execute(query)

get_user("1 OR 1=1")

hello()
eval("2 + 2")

