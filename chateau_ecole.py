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
        print("Vous avez ajoute", objet,"a votre inventaire.")
        score += 5
    else:
        print(objet," est deja dans votre inventaire.")

def jeu():
    print("Bienvenue dans la maison du grand N...")
    print("")
    print("Vous vous reveillez dans votre lit, un objet metallique vous gratte le dos.")
    cl_francais()

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
    print("Fin de l'aventure")
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

def cl_latin():
    print("salle de latin")
    print("les sorties sont : 1. Couloir 2e 2. Examiner")
    commande = valider_reponse(2)
    if comande == "1":
        couloir2e()
    else:
        print("examiner")

def couloir2e():
    print("Couloir 2e etage")
    print("les sorties sont : 1.Classe Latin  2.Classe Sciences 3. Infirmerie 4.Escalier bas 5.Examiner")
    commande = valider_reponse(5)
    if comande == "1":
        cl_latin()
    elif commande == "2":
        cl_sciences()
    elif commande == "3":
        infirmerie()
    elif commande =="4":
        couloir1e()
    else:
        print("examiner")

def cl_sciences():
    print("classe sciences : ferme !")
    print("les sorties sont : 1. Couloir 2e 2. Examiner")
    commande = valider_reponse(2)
    if comande == "1":
        couloir2e()
    else:
        print("examiner")

def infirmerie():
    print("Infirmerie, infirmiere absente...")
    print("les sorties sont : 1. Couloir 2e 2. Examiner")
    commande = valider_reponse(2)
    if comande == "1":
        couloir2e()
    else:
        print("examiner")          

def couloir1e():
    print("Couloir 1er etage")
    print("les sorties sont : 1.Escalier haut 2.Escalier bas  3.Classe Maths 4. Classe Français 5. Classe Histoire 6.Toilettes")
    commande = valider_reponse(6)
    if comande == "1":
        couloir2e()
    elif commande == "2":
        couloir_rdc()
    elif commande == "3":
        cl_maths()
    elif commande =="4":
        cl_francais()
    elif commande =="5":
        cl_histoire()       
    else:
        toilettes()

def cl_maths():
    print("Classe de maths...")
    print("les sorties sont : 1. Couloir 2. Examiner")
    commande = valider_reponse(2)
    if comande == "1":
        couloir1e()
    else:
        print("examiner") 

def cl_francais():
    print("classe de francais: fermer !")
    print("les sorties sont : 1.couloir 2. Examiner")
    commande = valider_reponse(2)
    if commande == "1":
        couloir1e()
    else:
        print("Examiner")

def cl_histoire():
    print("classe d'histoire...")
    print("les sorties sont : 1.couloir 2.Examiner")
    commande = valider_reponse(2)
    if commande == "1":
        couloir1e()
    else:
        print("Examiner")

def toilette():
    print("les toilettes...")
    print("Les sorties sont : 1.couloir 2.Examiner")
    commande = valider_reponse(2)
    if commande == "1":
        couloir1e()
    else:
        print("Examiner")

def cour():
    print("la cour...")
    print("les sorties sont : 1.aumonerie 2.portail 3.gymnase 4.cantine 5.examiner")
    commande = valider_reponse(5)
    if commande == "1":
        aumonerie()
    elif commande == "2":
        portail()
    elif commande == "3":
        gymnase()
    elif commande == "4":
        cantine()
    else:
        print("Examiner")

def aumonerie():
    print("aumonerie...")
    print("les sorties sont : 1.couloir 2.Passage sous-terrain 3.examiner")
    commande = valider_reponse(3)
    if commande == "1":
        couloirRdc()
    elif commande == "2":
        passagesousterain()
    else:
        print("Examiner")

def portail():
    print("portail...")
    print("les sorties sont : 1.couloir 2.examiner")
    commande = valider_reponse(2)
    if commande == "1":
        couloirRdc()
    else:
        print("Examiner")

def gymnase():
    print("gymnase...")
    print("les sorties sont : 1.couloir 2.examiner")
    commande = valider_reponse(2)
    if commande == "1":
        couloirRdc()
    else:
        print("Examiner")

def couloirRdc():
    print("en cours")

jeu()
