import pygame

pygame.init()
pygame.mixer.init()

son_latin = pygame.mixer.Sound("son_latin.wav")

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
                return  

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

def cl_latin(option=None):
    print("")
    if option == None:
        print("salle de latin")
        sound = pygame.mixer.Sound(son_latin)
        sound.play()
    print("les sorties sont : 1. Couloir 2e 2. Examiner")
    commande = valider_reponse(2)
    if commande == "1":
        couloir2e()
    else:
        print("examiner la classe de latin")
        print("attention lire 2 fois un livre peut faire mourir d'ennui")
        cl_latin(1)

def couloir2e(option=None):
    print("")
    if option == None:
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
        print("Vous examinez le couloir... tiens une photo...")
        print("")
        couloir2e(1)

def cl_sciences(option=None):
    print("")
    if option == None:
        print("classe sciences : ferme !")
    print("les sorties sont : 1. Couloir 2e 2. Examiner")
    commande = valider_reponse(2)
    if commande == "1":
        couloir2e()
    else:
        print("examiner, trouver masque a gaz")
        print("")
        cl_sciences(1)

def infirmerie(option=None):
    print("")
    if option == None:
        print("Infirmerie, infirmiere absente...")
    print("les sorties sont : 1. Couloir 2e 2. Examiner")
    commande = valider_reponse(2)
    if commande == "1":
        couloir2e()
    else:
        print("Des bandages a trouver...")
        infirmerie(1)

def couloir1e(option=None):
    print("")
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

def cl_maths(option=None):
    print("")
    if option == None:
        print("Classe de maths...")
    print("les sorties sont : 1. Couloir 2. Examiner")
    commande = valider_reponse(2)
    if commande == "1":
        couloir1e()
    else:
        print("Indice pour ouvrir la classe de Sciences")
        cl_maths(1)

def cl_francais(option=None):
    print("")
    if option == None:
        print("classe de francais: fermee !")
    print("les sorties sont : 1.couloir 2. Examiner")
    commande = valider_reponse(2)
    if commande == "1":
        couloir1e()
    else:
        print("Vous examinez la classe de francais")
        print("faire un passage secret vers classe Histoire")
        print("")
        cl_francais(1)

def cl_histoire(option=None):
    print("")
    if option == None:
        print("classe d'histoire...")
    print("les sorties sont : 1.couloir 2.Examiner")
    commande = valider_reponse(2)
    if commande == "1":
        couloir1e()
    else:
        print("Examiner")
        print("Histoire sur le lycée, salle de torture ?! en sous-sol, aumonerie ?")
        cl_histoire(1)

def toilettes(option=None):
    print("")
    if option == None:
        print("les toilettes...")
    print("Les sorties sont : 1.couloir 2.Examiner")
    commande = valider_reponse(2)
    if commande == "1":
        couloir1e()
    else:
        print("Examiner")
        print("Masque a gaz sinon mort en regardant les wc")
        print("une clef dans les wc")
        toilettes(1)

def couloir_rdc(option=None):
    print("")
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

def cl_techno(option=None):
    print("")
    if option == None:
        print("Classe de Techno")
    print("Les sorties sont : 1.couloir 2.Examiner")
    commande = valider_reponse(2)
    if commande == "1":
        couloir_rdc()
    else:
        print("Examiner")
        print("Chargeur de telephone!")
        cl_techno(1)

def sous_sol(option=None):
    print("")
    print("Sous-sol de l'ecole")
    print("Les sorties sont : 1.Escaliers 2.Classe Anglais 3.Classe Musique")
    commande = valider_reponse(3)
    if commande == "1":
        couloir_rdc()
    elif commande == "2":
        cl_english()
    else:
        cl_musique()    

def cl_english(option=None):
    print("")
    if option == None:
        print("Classe d'Anglais")
    print("Les sorties sont : 1.couloir 2.Examiner")
    commande = valider_reponse(2)
    if commande == "1":
        sous_sol()
    else:
        print("Examiner")
        print("obtention d'un cours d'anglais.. tue le prof de sport")
        cl_english(1)

def cl_musique(option=None):
    print("")
    if option == None:
        print("Classe de musique")
    print("Les sorties sont : 1.couloir 2.Examiner")
    commande = valider_reponse(2)
    if commande == "1":
        sous_sol()
    else:
        print("Examiner")
        print("recuperer partition de musique et medaillon")
        cl_musique(1)

def cl_6e(option=None):
    print("")
    if option == None:
        print("Classe 6eme")
    print("Les sorties sont : 1.couloir 2.Examiner")
    commande = valider_reponse(2)
    if commande == "1":
        couloir_rdc()
    else:
        print("Examiner")
        print("horde de zombies.. a voir...")
        cl_6e(1)

def salleprofs(option=None):
    print("")
    if option == None:
        print("Salle des profs")
    print("Les sorties sont : 1.couloir 2.Bureau Proviseur 3.Examiner")
    commande = valider_reponse(3)
    if commande == "1":
        couloir_rdc()
    elif commande =="2":
        bureaupro()
    else:    
        print("Examiner")
        print("Un surveillant a amadouer avec de la nourriture")
        salleprofs(1)

def bureaupro(option=None):
    print("")
    if option == None:
        print("Bureau du Proviseur")
    print("Les sorties sont : 1.Salle des profs 2.Examiner")
    commande = valider_reponse(2)
    if commande == "1":
        salleprofs()
    else:
        print("Examiner")
        print("Une photo avec un indice sur le passage sous-terrain et la musique a trouver")
        bureaupro(1)


def cour(option=None):
    print("")
    if option == None:
        print("la cour...description")
    print("les sorties sont : 1.Aumonerie 2.Portail 3.Gymnase 4.Cantine 5.Couloir RDC 6.Examiner")
    commande = valider_reponse(6)
    if commande == "1":
        aumonerie()
    elif commande == "2":
        portail()
    elif commande == "3":
        gymnase()
    elif commande == "4":
        cantine()
    elif commande == "5":
        couloir_rdc()
    else:
        print("Examiner")
        print("peut etre des trucs sur une statue ou un arbre")
        cour(1)
        
def aumonerie(option=None):
    print("")
    if option == None:
        print("aumonerie...")
    print("les sorties sont : 1.cour exterieure 2.Passage sous-terrain 3.examiner")
    commande = valider_reponse(3)
    if commande == "1":
        cour()
    elif commande == "2":
        passagesousterrain()
    else:
        print("Examiner, des blagues avec M Perrier")
        aumonerie(1)        

def portail(option=None):
    print("")
    if option == None:
        print("portail...")
    print("les sorties sont : 1.Cour 2.examiner")
    commande = valider_reponse(2)
    if commande == "1":
        cour()
    else:
        print("Examiner")
        portail(1)

def gymnase(option=None):
    print("")
    if option ==  None:
        print("gymnase...")
    print("les sorties sont : 1.Cour 2.examiner")
    commande = valider_reponse(2)
    if commande == "1":
        cour()
    else:
        print("Examiner")
        print("un prof de sport à faire fuir, anglais...")
        print("trouver des armes et des balles de tennis")
        gymnase(1)


def passagesousterrain(option=None):
    print("")
    print("Passage dans le noir, sous-terrain")
    print("les sorties sont : 1.Eglise 2.Aumonerie")
    commande = valider_reponse(2)
    if commande == "1":
        eglise()
    else:
        aumonerie()
        

def eglise(option=None):
    print("")
    if option == None:
        print("Eglise St Leger")
    print("les sorties sont : 1.Passage sous-terrain 2.Examiner")
    commande = valider_reponse(2)
    if commande == "1":
        passagesousterrain()
    else:
        print("Examiner")
        print("un orgue avec une musique, un medaillon peut etre...")
        eglise(1)

jeu()
