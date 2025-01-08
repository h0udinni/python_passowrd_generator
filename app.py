import secrets # números aleatórios mais seguros que o random.
import string # manipulação de caractéres.
result=[]

print("by:")
print(" __     ______           __ __               __ ")
print("|  |--.|      |.--.--.--|  |__|.-----.-----.|__|")
print("|     ||  --  ||  |  |  _  |  ||     |     ||  |")
print("|__|__||______||_____|_____|__||__|__|__|__||__|")

def password():
    for ps in range(5):
        ps=secrets.choice(string.punctuation) #Special caracters
        result.append(ps)
        ps=secrets.randbelow(11)
        result.append(ps)
        ps=secrets.choice(string.ascii_letters)
        result.append(ps)
    print("Your password as: ")
    for i in result:
        print(i, end = "") # end = "" Remove quebra de linha automática.
password()

while True:
    result.clear()
    choice = input("\nGenerate another password (s/n)?  ")
    if choice == "s" or choice == "S":
        password()
    elif choice == "n" or choice == "N":
        break
    else:
        input("Invalid option... Press enter to continue... ")