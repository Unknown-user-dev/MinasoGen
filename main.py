import base64
import random
import colorama
import os 
from colorama import Fore, Back, Style
from colorama import init
os.system("cls || clear") 
init()
banner = Fore.RED + f"""
  __  __ _                        _____            
 |  \/  (_)                      / ____|           
 | \  / |_ _ __   __ _ ___  ___ | |  __  ___ _ __  
 | |\/| | | '_ \ / _` / __|/ _ \| | |_ |/ _ \ '_ \ 
 | |  | | | | | | (_| \__ \ (_) | |__| |  __/ | | |
 |_|  |_|_|_| |_|\__,_|___/\___/ \_____|\___|_| |_|                                                 
                                                                 
            By : @Unknown-user-dev 
        https://github.com/Unknown-user-dev
"""

print(banner)

def random_password():
    password = ""
    for i in range(16):
        password += chr(random.randint(33, 126))
    return password

def save_password_to_txt(filename, password):
    with open(filename, 'a') as file:  
        file.write(password + '\n') 
    print(f"Le mot de passe a été ajouté au fichier {filename}.")

def encode(password):
    password = password.encode()
    password = base64.b64encode(password)
    return password.decode()

def decode(password):
    password = password.encode()
    password = base64.b64decode(password)
    return password.decode()

def menu():
    print(Fore.GREEN + """
    [1] Générer un mot de passe aléatoire
    [2] Encoder un mot de passe
    [3] Décoder un mot de passe
    [4] Credits
    [5] Quitter
    """)
    choice = input(Fore.BLUE + "Choisissez une option : ")
    if choice == "1":
        password = random_password()
        save_password_to_txt("mdp.txt", password)
        print(Fore.YELLOW + f"Votre mot de passe est : {password}")
        menu()
    elif choice == "2":
        password = input(Fore.BLUE + "Saisissez le mot de passe : ")
        password = encode(password)
        save_password_to_txt("mdp.txt", password)
        print(Fore.YELLOW + f"Votre mot de passe encodé est : {password}")
        menu()
    elif choice == "3":
        password = input(Fore.BLUE + "Saisissez le mot de passe : ")
        password = decode(password)
        save_password_to_txt("mdp.txt", password)
        print(Fore.YELLOW + f"Votre mot de passe décoder est : {password}")
        menu()
    elif choice == "4":
        print(Fore.GREEN + "By : @Unknown-user-dev | github.com/Unknown-user-dev | >_Unknown User#8624 ")
    elif choice == "5":
        print(Fore.RED + "Bye !")
        exit()
    else:
        print(Fore.RED + "Erreur : Veuillez saisir une option valide !")
        menu()

if __name__ == "__main__":
    menu()

