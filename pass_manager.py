from cryptography.fernet import Fernet
'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file: #wb = write in bytes
        key_file.write(key)
'''

def load_key():
    file = open("key.key", 'rb')
    key = file.read()
    file.close()
    return key


master_pwd = input("What is the master password? ")
key = load_key() + master_pwd.encode() #key is in bytes transform pwd to bytes using encode
fer = Fernet(key)

def view():
    with open('passwords.txt', 'r') as f: #a is append, with automatically closes the file
        for line in f.readlines():
            data = line.rstrip() #r.strip strings the \n
            user, passw = data.split(":")
            print("User:", user, ", Password:", fer.decrypt(passw.encode()).decode())

def add():
    name = input("account name: ")
    pwd = input("password: ")\
    # a = append, w = write will override other files, r = read file needs to exist 
    with open('passwords.txt', 'a') as f: #a is append, with automatically closes the file
        f.write(name + ": " + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input("Do you want to add a new passsword or view existing ones? VIEW/ADD ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()

    elif mode == "add":
        add()

    else:
        print("invalid")





