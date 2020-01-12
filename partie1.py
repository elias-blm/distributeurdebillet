code= 1234
essai=int(input("Veuillez saisir votre code confidentiel "))
montant=0

if essai== code:
    montant= int(input("Quelle somme desirez vous retirer? "))
    print("Vous avez demandé", montant , " euros, veuillez retirer vos billets.")
else:
    print("Opération annulée!")