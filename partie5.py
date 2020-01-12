nom=['']*10 
code=['']*10 
compte=['']*10 
essai=4

nom[0] = "Alice" ; code[0] = "0606" ; compte[0]=1000 
nom[1] = "Bob" ;  code[1] = "0607" ; compte[1]=1000 
nom[2] = "Charles" ; code[2] = "0608" ; compte[2]=1000 
nom[3] = "Djamel" ;code[3] = "0609" ; compte[3]=1000 
nom[4] = "Etienne"; code[4] = "0610" ; compte[4]=1000 
nom[5] = "Frederique" ; code[5] = "0611" ; compte[5]=1000 
nom[6] = "Guillaume" ; code[6] = "0612" ; compte[6]=1000 
nom[7] = "Hector" ; code[7] = "0613" ; compte[7]=1000 
nom[8] = "Isabelle" ; code[8] = "0614" ; compte[8]=1000 
nom[9] = "Jerome" ; code[9] = "0615" ; compte[9]=1000 


def essaicode (code, essai):

    while essai!=0:
        codeessai=str(input("Veuillez saisir votre code confidentiel "))
        
        if codeessai in code:
            essai = 0
            

        elif codeessai not in code:
            essai=essai-1
            print("Erreur, il vous reste", essai,"essais...")
        

    if essai==0 and codeessai not in code:
        print("Opération annulée!")
        return False

    elif codeessai in code:
        identifiant=code.index(codeessai)
        return identifiant

def identification(utilisateur, compte):
        print( "Bonjour", utilisateur," ,vous disposez de", compte, "euros . Quel montant désirez vous retirer ?")

def retrait(compte):
    essai=4
    montant=-1
    
    while essai!=0 and montant>700 or montant<0 and essai!=0:
        montant=int(input("Quelle somme voulez vous retirer? "))

        if 700>montant and montant>0 and montant!=compte:
            print("Il vous reste",compte-montant,"euros. Retirez vos billets")

        elif montant==compte:
            print("Opération effectuée, il ne vous reste plus d'argent.")


        elif 0>montant or montant>700:
            essai=essai-1
            print("Le montant doit être compris entre 0 et 700. Il vous reste",essai,"essai(s).")

    if essai==0 and montant<0 or montant>700 and essai==0:
        print("Opération annulée")

while 1>0:
    identifiant= essaicode (code, essai)

    if identifiant!= False:
        identification(nom[identifiant], compte[identifiant])
        retrait(compte[identifiant])

