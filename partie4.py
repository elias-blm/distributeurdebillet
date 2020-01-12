def identification(utilisateur, compte):
        print( "Bonjour", utilisateur," , vous disposez de", compte, "euros . Quelle montant désirez vous retirer ?")

def retrait(compte):
    essai=4
    montant=-1
    
    while essai!=0 and montant>700 or montant<0 and essai!=0:
        montant=int(input("Quelle somme voulez vous retirer?"))

        if 700>montant and montant>0 and montant!=compte:
            print("Il vous reste",compte-montant,"euros. Retirez vos billets")

        elif montant==compte:
            print("Opération effectuée, il ne vous reste plus d'argent.")


        elif 0>montant or montant>700:
            essai=essai-1
            print("Le montant doit être compris entre 0 et 700. Il vous reste",essai,"essai(s).")

    if essai==0 and montant<0 or montant>700 and essai==0:
        print("Opération annulée")


def essaicode (code1, code2, essai):

    while essai!=0:
        code=int(input("Veuillez saisir votre code confidentiel "))
        
        if code!=code1 and code!=code2:
            essai = essai-1
            print("Erreur, il vous reste", essai,"essais...")

        elif code==code1 or code==code2:
            essai=0

    if essai==0 and code!=code1 and code!=code2:
        print("Opération annulée!")

    elif code==code1:
        return utilisateur1

    elif code== code2:
        return utilisateur2

essai= 4
utilisateur1="Trucmuche" ; code1=1234;compte1=500 ;
utilisateur2="Bidule";code2=4321;compte2=300

while 1>0: 
    user=essaicode (code1,code2,essai)

    if user== utilisateur1:
        identification(utilisateur1,compte1)
        retrait(compte1)

    if user== utilisateur2:
        identification(utilisateur2,compte2)
        retrait(compte2)
