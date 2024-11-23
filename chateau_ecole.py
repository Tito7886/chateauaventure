inventaire = []
suivi_aventure = []
score = 0

def afficher_inventaire():
    if inventaire:
        print("Vous avez dans votre inventaire :")
        for objet in inventaire:
            print("-",objet)
    else:
        print("Votre inventaire est vide.")


def ajouter_inventaire(objet):
    global score

    tshirts = ["tshirt jaune", "tshirt orange"]
    if objet in tshirts:
        # Vérifier si un autre t-shirt est déjà dans l'inventaire
        for tshirt in tshirts:
            if tshirt in inventaire:
                # Remplacer l'ancien t-shirt par le nouveau
                inventaire.remove(tshirt)
                inventaire.append(objet)
                print("Vous avez remplace", tshirt," par ",objet)
                return  # Pas d'ajout de points, on sort de la fonction

    if objet not in inventaire:
        inventaire.append(objet)
        print("\033[32mVous avez ajoute", objet,"a votre inventaire.\033[0m")
        score += 5
    else:
        print(objet," est deja dans votre inventaire.")

def jeu():
    print("Bienvenue dans la maison du grand N...")
    print("")
    print("Vous vous reveillez dans votre lit, un objet metallique vous gratte le dos.")
    chambre_cha()

def finpartie():
    global score
    print("desole c'est la fin.. quelle negligence")
    print("essaye de faire mieux la prochaine fois")
    print("ton score :", score," pts")  
    print("")
    rejouer()

def victoire():
    global score
    score += 20
    print("")
    print("\033[32mVous vous reveillez dans votre lit\033[0m")
    print("tout transpirant...")
    print("Votre mere vous appelle pour aller a l'ecole.")
    print("")
    print("Encore un mauvais reve")
    print("Une peluche... un diablotin vert... est contre votre oreille...")
    print("Tandis que votre peluche preferee, Mr Nounours, est au sol")
    print("")
    print("\033[32mFin de l'aventure\033[0m")
    print("ton score :", score," pts") 
    print("") 
    rejouer()

def rejouer():
    global inventaire, suivi_aventure, score
    commande = valider_reponse(2,"Voulez vous rejouer ? 1. Oui  2.Non )
    if commande == "1":
        inventaire = []
        suivi_aventure = []
        score = 0
        for _ in range(40):
            print("")
        jeu()
    else:
        print("Au revoir.... macaque !")


def valider_reponse(max_choix, message="Que voulez-vous faire ? "):
    global score
    
    # Génération de la liste des choix valides
    choix_valides = [str(i) for i in range(1, max_choix + 1)]
    
    # Validation de la réponse utilisateur
    while True:
        reponse = input(message).strip()
        if reponse in choix_valides:
            return reponse
        else:
            score -= 2
            print("Entree invalide.... macaque !")

jeu()
