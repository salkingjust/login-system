userData = {
    1: {"username": "Maryam", "password": "112211"},
    2: {"username": "Joseph", "password": "234432"},
    3: {"username": "Saleem", "password": "17966"},
    4: {"username": "Adnan", "password": "12345"}
}

def login_system():
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username in [user['username'] for user in userData.values()]:
            user_info = next((user for user in userData.values() if user['username'] == username), None)

            if user_info and user_info['password'] == password:
                print("Login successful!")
                break
            else:
                print("Incorrect password. Please try again.")
        else:
            print("Username not found. Please try again.")

login_system()
