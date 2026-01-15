def hello():
    print("Hello World")

def execute(query):
    print(query)

name = input("Enter : ")
query = "SELECT * FROM users WHERE name = '" + name + "'"
execute(query)
hello()

