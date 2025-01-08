import secrets # números aleatórios mais seguros que o random.
import string # manipulação de caractéres.
from random import shuffle #Embaralha strings e números de uma lista.

result=[]

def menu():
    print("Developed by:")
    print(" __     ______           __ __               __ ")
    print("|  |--.|      |.--.--.--|  |__|.-----.-----.|__|")
    print("|     ||  --  ||  |  |  _  |  ||     |     ||  |")
    print("|__|__||______||_____|_____|__||__|__|__|__||__|")
    print('+' + '-'*24 +  '-'*24 + '+')
    print('https://github.com/h0udinni')

def password():
    for ps in range(100):
        ps=secrets.choice(string.punctuation) #Special caracters
        result.append(ps)
        ps=secrets.randbelow(9)
        result.append(ps)
        ps=secrets.choice(string.ascii_letters)
        result.append(ps)
        shuffle(result)

def shf_password():
        password()
        try:
            n2=int(input("What size list do you want (Enter a intery number)? "))
            if n2 >= 12:
                print("Your password as: ")
                result2=result[0:n2]
                for i in result2:
                    print(i, end = "")
                print('')
                result.clear()
            else:
                print("The minimum number allowed is 12.")
        except ValueError:
            input('Invalid option... Press enter to continue... ')

def options():
    while True:
        choice = input("Generate a password (s/n)? ")
        if choice == "s" or choice == "S":
            shf_password()
        elif choice == "n" or choice == "N":
            print('Thanks for use the software.')
            break
        else:
            input("Invalid option... Press enter to continue... ")

menu()
options()