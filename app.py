def hello():
    print("Hello World")

def execute(query):
    print(query)

name = input("Enter name: ")
query = "SELECT * FROM users WHERE name = '" + name + "'"
execute(query)
hello()
eval("2 + 2")

#
#
# def add():
#     return eval("10 + 20")
# add()
#
#
# def execute(query):
#     print(query)
#
# name = "admin"
# query = "SELECT * FROM users WHERE name = '" + name + "'"
# execute(query)
