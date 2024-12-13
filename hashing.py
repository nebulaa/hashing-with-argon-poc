import json
from argon2 import PasswordHasher


def generate_password_hash(password):
    """
    The default values used by PasswordHasher are:
    time_cost=3, memory_cost=65536 KiB, parallelism=4, hash_len=32, salt_len=16
    The default vaules are chosen as per RFC 9106 recommendations.
    64 MiB of RAM is consumed by this hashing algorithm.
    The resulting hash is generated along with all relevant parameters and the salt.
    """
    return PasswordHasher().hash(password)

def write_to_file(username, hash):
    try:
        with open("dummy_data.json", "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}

    data[username] = hash

    with open("dummy_data.json", "w") as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":

    while True:
        register = input("Do you want to register? (y/n): ")
        if register.lower() != "y":
            break

        print("Adding User...\n")

        input_username = input("Enter your username: ")
        input_password = input("Enter your password: ")
        hash = generate_password_hash(input_password)
        write_to_file(input_username, hash)

        print("User infomation saved\n")

