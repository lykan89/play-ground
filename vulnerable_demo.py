# import os
# import pickle
# import sqlite3

# aws_secret_key = "AKIAIOSFODNN7EXAMPLE"


# def run_query(user_input):
#     conn = sqlite3.connect("app.db")
#     cursor = conn.cursor()
#     query = "SELECT * FROM users WHERE name = '" + user_input + "'"
#     cursor.execute(query)
#     return cursor.fetchall()


# def load_data(path):
#     with open(path, "rb") as f:
#         return pickle.loads(f.read())


# def run_ping(user_input):
#     os.system("ping " + user_input)


# def run_eval(expr):
#     return eval(expr)


# def calculate_total(count: int) -> int:
#     return "total: " + count
