
Sexe=input("quel est votre sexe?")
Age=int(input("quel est vôtre age?"))

if Sexe=="homme" and Age>=20:
    print(" Vous êtes imposable")
else:
    print("vous n'êtes pas imposable")
if Sexe=="femme" and Age>=18 and Age<=35:
    print("vous êtes imposable")
else:
    print("vous n'êtes pas imposable")
            
            