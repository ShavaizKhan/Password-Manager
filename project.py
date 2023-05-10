from cryptography.fernet import Fernet

def main():
    # menu loop
    while True:
        menu = input("Please enter command: \n1. add password \n2. view passwords \n3. exit system\n")

        if menu == "1":
            name = input("Username: ")
            password = input("Password: ")
            add(name, password)

        elif menu == "2":
            view()

        elif menu == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid Mode\n")
            continue

# loading key
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

# encryption
key = load_key()
fer = Fernet(key)

# add function
def add(name, password):
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(password.encode()).decode() + "\n")

# view function
def view():
    with open('passwords.txt', 'r') as file:
        for line in file.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode())

if __name__ == "__main__":
    main()