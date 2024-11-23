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
    print("Vous vous reveillez sur votre bureau de classe")
    print("")
    print("Il n'y a plus personne dans la salle, les lumières sont éteintes...")
    print("")
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
    commande = valider_reponse(2,"Voulez vous rejouer ? 1. Oui  2.Non")
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
    
    choix_valides = [str(i) for i in range(1, max_choix + 1)]
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
    if commande == "1":
        couloir2e()
    else:
        print("examiner")

def couloir2e():
    print("Couloir 2e etage")
    print("les sorties sont : 1.Classe Latin  2.Classe Sciences 3. Infirmerie 4.Escalier bas 5.Examiner")
    commande = valider_reponse(5)
    if commande == "1":
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
    if commande == "1":
        couloir2e()
    else:
        print("examiner")

def infirmerie():
    print("Infirmerie, infirmiere absente...")
    print("les sorties sont : 1. Couloir 2e 2. Examiner")
    commande = valider_reponse(2)
    if commande == "1":
        couloir2e()
    else:
        print("examiner")          

def couloir1e():
    print("Couloir 1er etage")
    print("les sorties sont : 1.Escalier haut 2.Escalier bas  3.Classe Maths 4. Classe Français 5. Classe Histoire 6.Toilettes")
    commande = valider_reponse(6)
    if commande == "1":
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
    if commande == "1":
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

def toilettes():
    print("les toilettes...")
    print("Les sorties sont : 1.couloir 2.Examiner")
    commande = valider_reponse(2)
    if commande == "1":
        couloir1e()
    else:
        print("Examiner")

def couloir_rdc():
    print("Couloir RDC")
    print("Les sorties sont : 1.Escaliers 2.Classe 6e 3.Salle des profs 4. Salle Techno 5.Sous-sol 6.Cour extérieure")    
    commande = valider_reponse(6)
    if commande == "1":
        couloir1e()
    elif commande == "2":
        cl_6e()
    elif commande == "3":
        salleprofs()
    elif commande =="4":
        cl_techno()
    elif commande =="5":
        sous_sol()       
    else:
        cour()    

def sous_sol():
    print("Sous-sol de l'ecole")
    print("Les sorties sont : 1.Escaliers 2.Classe Anglais 3.Classe Musique")
    commande = valider_reponse(3)
    if commande == "1":
        couloir_rdc()
    elif commande == "2":
        cl_english()
    else:
        cl_musique()    

def cl_english():
    print("Classe d'Anglais")
    print("Les sorties sont : 1.couloir 2.Examiner")
    commande = valider_reponse(2)
    if commande == "1":
        sous_sol()
    else:
        print("Examiner")    

def cl_musique():
    print("Classe de musique")
    print("Les sorties sont : 1.couloir 2.Examiner")
    commande = valider_reponse(2)
    if commande == "1":
        sous_sol()
    else:
        print("Examiner")   

def cl_6e():
    print("Classe 6eme")
    print("Les sorties sont : 1.couloir 2.Examiner")
    commande = valider_reponse(2)
    if commande == "1":
        couloir_rdc()
    else:
        print("Examiner")

def salleprofs():
    print("Salle des profs")
    print("Les sorties sont : 1.couloir 2.Bureau Proviseur 3.Examiner")
    commande = valider_reponse(3)
    if commande == "1":
        couloir_rdc()
    elif commande =="2":
        bureaupro()
    else:    
        print("Examiner")

def bureaupro():
    print("Bureau du Proviseur")
    print("Les sorties sont : 1.Salle des profs 2.Examiner")
    commande = valider_reponse(2)
    if commande == "1":
        salleprofs()
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
        couloir_rdc()
    elif commande == "2":
        passagesousterrain()
    else:
        print("Examiner")

def portail():
    print("portail...")
    print("les sorties sont : 1.Cour 2.examiner")
    commande = valider_reponse(2)
    if commande == "1":
        cour()
    else:
        print("Examiner")

def gymnase():
    print("gymnase...")
    print("les sorties sont : 1.Cour 2.examiner")
    commande = valider_reponse(2)
    if commande == "1":
        cour()
    else:
        print("Examiner")

def passagesousterrain():
    print("Passage dans le noir, sous-terrain")

def eglise():
    print("Eglise St Leger")

jeu()
