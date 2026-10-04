import json
import os
import base64

STORAGE_FILE = "credentials.json"

def encode_val(val):
    return base64.b64encode(val.encode()).decode()

def decode_val(encoded_val):
    return base64.b64decode(encoded_val.encode()).decode()

def load_data():
    if os.path.exists(STORAGE_FILE):
        with open(STORAGE_FILE, "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(STORAGE_FILE, "w") as f:
        json.dump(data, f, indent=4)

def create_credential(data):
    print("\n--- ADD NEW CREDENTIAL ---")
    platform = input("Enter platform name (e.g. Google): ").strip().lower()
    user_id = input("Enter username or email: ").strip()
    secret = input("Enter password: ").strip()
    
    secured_secret = encode_val(secret)
    data[platform] = {"username": user_id, "password": secured_secret}
    save_data(data)
    print("Information saved securely.")

def retrieve_credential(data):
    print("\n--- RETRIEVE CREDENTIAL ---")
    platform = input("Enter platform name to search: ").strip().lower()
    
    if platform in data:
        account = data[platform]
        original_secret = decode_val(account["password"])
        print("-" * 40)
        print(f"Platform : {platform.capitalize()}")
        print(f"Username : {account['username']}")
        print(f"Password : {original_secret}")
        print("-" * 40)
    else:
        print("No record found for this platform.")

def main():
    data = load_data()
    while True:
        print("\n*** PASSWORD MANAGER WORKSPACE ***")
        print("1. Store New Password")
        print("2. Search Existing Password")
        print("3. Exit System")
        
        option = input("Choose option (1/2/3): ").strip()
        
        if option == "1":
            create_credential(data)
        elif option == "2":
            retrieve_credential(data)
        elif option == "3":
            print("System closed safely.")
            break
        else:
            print("Invalid choice. Selection must be 1, 2, or 3.")

if __name__ == "__main__":
    main()