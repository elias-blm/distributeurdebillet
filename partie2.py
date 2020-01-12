def essaicode (codejuste, essai):

    while essai!=0:
        
        code=int(input("Veuillez saisir votre code confidentiel "))
        
        if code!=codejuste:
            essai = essai-1
            print("Erreur, il vous reste", essai,"essais...")
        
        if code==codejuste:
            essai=0

    if essai==0 and code!=codejuste:
         print("Opération annulée!")

    elif code==codejuste:
        return codejuste



def retrait(essai):
    montant=-1
    while essai!=0 and montant>700 or montant<0 and essai!=0:
        montant=int(input("Quelle somme voulez vous retirer?"))

        if 700>montant and montant>0:
            print("Vous avez demandé",montant,"euros. Retirez vos billets")


        elif 0>montant or montant>700:
            essai=essai-1
            print("Le montant doit être compris entre 0 et 700. Il vous reste",essai,"essai(s).")

    if essai==0 and montant<0 or montant>700 and essai==0:
        print("Opération annulée")
	

codejuste= 1234
essai=4


codefinal=essaicode (codejuste,essai)

if codefinal==codejuste:
    retrait(essai)

