import json
import getpass
import argon2

ph = argon2.PasswordHasher(memory_cost=134218)

input_username = input("Enter your username: ")
input_password = getpass.getpass("Enter your password: ")

with open("dummy_data.json", "r") as f:
    data = json.load(f)

if input_username in data:
    hash = data[input_username]
    try:
        ph.verify(hash, input_password)
        print("Password is correct")
        if ph.check_needs_rehash(hash):
            print("Password needs to be rehashed")
        else:
            print("Password is not rehashed")
    except Exception as e:
        print(e)
else:
    print("Username not found")