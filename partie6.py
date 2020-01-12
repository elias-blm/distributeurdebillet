fichier_lu=open(r"livre_compte.txt",'r')
liste_lignes=fichier_lu.readlines()
fichier_lu.close()

essai=4
compteur=0

while compteur!=len(liste_lignes):
    liste_lignes[compteur]=liste_lignes[compteur].rstrip('\n')
    compteur=compteur+1

def essaicode (repertoire, essai):

    while essai!=0:
        codeessai=str(input("Veuillez saisir votre code confidentiel "))
        
        if codeessai in repertoire:
            essai = 0
            

        elif codeessai not in repertoire and codeessai!='new':
            essai=essai-1
            print("Erreur, il vous reste", essai,"essais...")

        elif codeessai=='new':
            essai=0


    if essai==0 and codeessai not in repertoire and codeessai != 'new':
        print("Opération annulée!")
        return False

    elif codeessai in repertoire:
        identifiant=repertoire.index(codeessai)
        return identifiant
    
    elif codeessai=='new':
        return 'new'

def identification(utilisateur, compte):
        print( "Bonjour", utilisateur, ",vous disposez de", compte, "euros . Quel montant désirez vous retirer ?")

def nouvelutilisateur(liste_lignes):
    newid=str(input('Entrez le nom du nouvel utilisateur '))
    newcode=str(input('Entrez le code du nouvel utilisateur '))
    newcompte=str(input("Entrez le montant dont l'utilisateur dispose "))

    nouvelledata=[newid,newcode,newcompte]
    liste_lignes=liste_lignes+nouvelledata
    liste_lignes='\n'.join(liste_lignes)
    fichier_ecrit=open(r"livre_compte.txt",'w')
    fichier_ecrit.write(liste_lignes) 
    fichier_ecrit.close()
    print("Votre nouvel utilisateur a bien été enregistré.")

def nouveaumontant(identifiant,somme,liste_lignes):
    liste_lignes[identifiant+1]=str(int(liste_lignes[identifiant+1])-somme)
    liste_lignes='\n'.join(liste_lignes)
    fichier_ecrit=open(r"livre_compte.txt",'w')
    fichier_ecrit.write(liste_lignes) 
    fichier_ecrit.close()
    print("Le montant dont vous disposez a été mis à jour")


def retrait(compte):
    essai=4
    montant=-1
    
    while essai!=0 and montant>700 or montant<0 and essai!=0:
        montant=int(input("Quelle somme voulez vous retirer? "))

        if 700>montant and montant>0 and montant!=compte:
            print("Il vous reste",compte-montant,"euros. Retirez vos billets")
            return montant

        elif montant==compte:
            print("Opération effectuée, il ne vous reste plus d'argent.")
            return montant

        elif 0>montant or montant>700:
            essai=essai-1
            print("Le montant doit être compris entre 0 et 700. Il vous reste",essai,"essai(s).")

    if essai==0 and montant<0 or montant>700 and essai==0:
        print("Opération annulée")

while 1>0:
    identifiant=essaicode(liste_lignes,essai)
    
    if identifiant=='new':
        nouvelledata= nouvelutilisateur(liste_lignes)
    
    elif identifiant !='new' and identifiant != False:
        identification(liste_lignes[identifiant-1],liste_lignes[identifiant+1])
        somme=retrait(int(liste_lignes[identifiant+1]))
        nouveaumontant(identifiant,somme,liste_lignes)