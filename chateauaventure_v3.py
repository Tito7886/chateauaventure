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

def chambre_cha ():
    print("")
    print("Vous etes dans une chambre en bazar")
    print("Les sorties sont : 1. le couloir, 2. examiner")
    commande = valider_reponse(2, "Que voulez-vous faire ? ")
    if commande == "1":
        print("")
        palier()
    elif commande == "2":
        print("")
        print("Voici ce qu'il y a")
        examiner_chcha = ["1.chambre","2.lit","3.bureau","4.tapis","5.tas de chaussettes","6.tas de t-shirts","7.fenetre"]
        for i, element in enumerate(examiner_chcha, start=1):
            print(element)
    
        commande2 = valider_reponse(7, "Que voulez-vous faire ? ")
        if commande2 == "1":
            print("Vous etes sur un lit, vous voyez un bureau,")
            print("des tas d'habits et un tapis. Il y a aussi une fenetre")
            if "sacrifice_mrnounours" not in suivi_aventure:
                print("et un gentil nounours.")
                ajouter_inventaire("Mr_nounours")
                print("")
                afficher_inventaire()
            else:
                print("\033[32mMr Nounours a deja heroiquement... affronte un dragon pour vous\033[0m")
            chambre_cha()
        elif commande2 == "2":
            print("Ce lit est un vrai champ de bataille.")
            print("Vous vous rappelez vous etre endormi dessus.")
            print("Vous trouvez une clef... Vous la prenez !")
            ajouter_inventaire("clef")
            print("")
            afficher_inventaire()
            chambre_cha()
        elif commande2 == "3":
            print("Vous trouvez du parfum, une photo et quelques bricoles sans interet.")
            print("Wahou, vous trouvez une photo de votre mere avec 2 grandes oreilles")
            print("vertes qui depassent en bas a droite, \033[32mil est ecrit : Pixiebis love...\033[0m")
            ajouter_inventaire("photo_pixiebis")
            #ajouter_inventaire("parfum")
            afficher_inventaire()
            chambre_cha()
        elif commande2 == "4":
            print("")
            print("Vous etes fous ! Fouiller tapis et puis quoi encore ?")
            chambre_cha()
        elif commande2 == "5":
            print("")
            print("\033[31mUn petit monstre tout vert a grandes oreilles surgit et vous tue.\033[0m")
            finpartie()
        elif commande2 == "6":
            print("Quel bazar cette chambre !")
            print("2 couleurs vous attirent : 1.jaune 2.orange 3.aucun")
            choixcouleur = valider_reponse(3, "Quelle couleur voulez-vous mettre ? ")
            if choixcouleur == "1":
                ajouter_inventaire("tshirt jaune")
                afficher_inventaire()
            elif choixcouleur == "2":
                ajouter_inventaire("tshirt orange")
                afficher_inventaire()
            chambre_cha()
        elif commande2 == "7":
            print("Vous voyez au travers de la fenetre, wahouuu!")
            print("Vous voyez un dragon tout vert crachant des flammes")
            print("et prononcant tchou tchou en boucle... ....")
            chambre_cha()

def palier():
    print("")
    print("C'est un couloir, ni plus ni moins.")
    print("Les sorties sont : 1. Chambre de Charlotte, 2. Chambre d'Alix, 3. Chambre Parents, 4. Salon")
    
    # Utilisation de valider_reponse pour valider l'entrée utilisateur
    commande = valider_reponse(4, "Que voulez-vous faire ? ")
    
    if commande == "1":
        chambre_cha()
    elif commande == "2":
        chambre_alix()
    elif commande == "3":
        chambre_parents()
    else:
        petitsalon()
 
def chambre_parents():
    global score
    # Vérification si un t-shirt a été donné et ajouté à suivi_aventure
    if "tshirt_donne" in suivi_aventure and "petitsalon" not in suivi_aventure:
        print("")
        print("Votre mere dort paisiblement, il n'y a plus rien a faire ici.")
        print("")
        palier()  
        return

    print("")
    print("Vous arrivez dans une grande piece.")
    print("Il y a un grand lit, une etagere, une fenetre et votre mere est assise sur le lit.")
    if "petitsalon" in suivi_aventure:
        print("votre pere grommelle a cote de votre delicieuse mere")
        print("cela a du la reveiller...")
    print("")
    print("Les sorties sont : 1. le couloir, 2. examiner.")
  
    commande = valider_reponse(2, "Que voulez-vous faire ? ")

    if commande == "1":
        palier()
    else:
        print("")
        print("Voici ce qu'il y a :")
        print("1. Etagere")
        print("2. Lit")
        print("3. Fenetre")
        if "petitsalon" in suivi_aventure:
            commande2 = valider_reponse(3, "Que voulez-vous faire ? ")
        else:
            print("4. Parler a maman")
            commande2 = valider_reponse(4, "Que voulez-vous faire ? ")
    
        if commande2 == "1":
            if "sacrifice_mrnounours" in suivi_aventure:
                print("")
                print("Il n'y a plus rien ici")
                chambre_parents()
            else:
                print("")
                print("Vous apercevez un petit dragon qui couve un oeuf.")
                print("\033[31mCela semble dangereux comme situation !\033[0m")
                print("")
                if "Mr_nounours" in inventaire:
                    print("")
                    print("\033[31mVous etes sauve par votre Mr Nounours qui se sacrifie en se jetant sur le dragon.\033[0m")
                    inventaire.remove("Mr_nounours")
                    suivi_aventure.append("sacrifice_mrnounours")
                    ajouter_inventaire("oeuf_dragon")
                    score += 50
                    afficher_inventaire()
                    chambre_parents()
                else:
                    finpartie()

        elif commande2 == "2":
            print("Il a l'air tres moelleux !")
            chambre_parents()

        elif commande2 == "3":
            print("\033[31Ooooh non, un diablotin tout vert !!!!\033[0m")
            print("Ses griffes surgissent et vous transpercent.")
            print("Au son de : c'est qui le plus fort, c'est Nestor !")
            finpartie()

        else:
            print("")
            print("Je cherche un t-shirt pour dormir...")
            if "tshirt jaune" in inventaire or "tshirt orange" in inventaire:
                # Validation avec valider_reponse pour donner un t-shirt
                commande = valider_reponse(2, "Voulez-vous donner un t-shirt ? 1. Oui 2. Non : ")

                if commande == "2":
                    chambre_parents()
                else:
                    if "tshirt jaune" in inventaire:
                        print("")
                        print("Votre mere dit : 'Oh non, ce jaune me donnerait l'air d'une banane !'")
                        chambre_parents()  # Retour à la même pièce si le t-shirt jaune est donné

                    elif "tshirt orange" in inventaire:
                        print("")
                        print("\033[32mMerci, je vais pouvoir me reposer maintenant, bonne nuit !\033[0m")
                        inventaire.remove("tshirt orange")
                        # Ajout dans suivi_aventure pour indiquer que le t-shirt a été donné
                        suivi_aventure.append("tshirt_donne")
                        score += 20
                        chambre_parents()

            else:
                print("")
                print("Vous n'avez pas de t-shirt.")
                print("")
                chambre_parents()

def chambre_alix():
    global score
    print("")
    
    if "oeuf_dragon_donne" in suivi_aventure:
        print("Vous arrivez dans une petite chambre tout mignonne.")
        print("Alix est en train de regarder son oeuf de dragon avec emerveillement, assise pres de son lit.")
    else:
        print("Vous arrivez dans une petite chambre tout mignonne.")
        print("Alix est a cote de son lit et il y a une etagere.")
    
    print("Les sorties sont : 1. le couloir, 2. examiner.")

    commande = valider_reponse(2, "Que voulez-vous faire ? ")

    if commande == "1":
        palier()
    else:
        print("")
        print("Voici ce qu'il y a :")
        print("1. Parler avec Alix")
        print("2. Examiner la chambre")
        print("3. Examiner l'etagere")
        
        commande2 = valider_reponse(3, "Que voulez-vous faire ? ")

        if commande2 == "1":
            print("")
            print("Oh comme je voudrais avoir un animal de compagnie...")
            
  
            if "oeuf_dragon" in inventaire and "oeuf_dragon_donne" not in suivi_aventure:
                commande3 = valider_reponse(2, "Voulez-vous donner l'oeuf de dragon ? 1. Oui 2. Non : ")
                if commande3 == "1":
                    print("")
                    print("\033[32mMerci, tu es la meilleure personne que je connaisse!!!!\033[0m")
                    inventaire.remove("oeuf_dragon")
                    score += 20
                    print("\033[32mPour te remercier je te donne cette clef trop belle\033[0m")
                    ajouter_inventaire("clef_alix")
                    suivi_aventure.append("oeuf_dragon_donne")  
                    chambre_alix()
                else:
                    chambre_alix()
            elif "oeuf_dragon_donne" in suivi_aventure:
                print("Tu as deja donne l'oeuf a Alix.")
                chambre_alix()
            else:
                print("")
                chambre_alix()

        elif commande2 == "2":
            print("")
            print("Vous voyez un lit vide, un ours en peluche qui fait des acrobaties")
            if "oeuf_dragon_donne" in suivi_aventure:
                print("Alix est assise pres de son lit, en train de regarder son oeuf de dragon")
            else:
                print("Alix est debout pres de son etagere a Picsou")
            
            chambre_alix()

        else: 
            print("")
            print("Un livre retient votre attention il est ecrit :")
            print("Voir les choses que l'on ne voit pas")
            commande4 = valider_reponse(3, "Que voulez-vous faire : 1. prendre le livre 2. le lire 3. rien")

            if commande4 == "1":
                ajouter_inventaire("livre")
                afficher_inventaire()
                chambre_alix()
            elif commande4 == "2":
                suivi_aventure.append("livre_lu")
                print("")
                print("\033[32mVous ne comprenez pas tres bien ce livre...\033[0m")
                print("")
                chambre_alix()
            else:
                chambre_alix()

def petitsalon():
    global score
    print("")
    
    # Vérification si la pièce a déjà été découverte
    if "petitsalon" in suivi_aventure:
        print("Vous etes de retour dans le petit salon.")
        print("Votre pere n'est plus la, la tele est eteinte")
        print("Les sorties sont : 1. le palier, 2. entree")
        commande = valider_reponse(2)
        
        if commande == "1":
            palier()
        elif commande == "2":
            lentree()
    else:
        print("Vous entrez dans le petit salon, il y a votre BG de pere")
        print("qui est assis sur le canape et qui joue a la Switch")
        print("Il y a une grande bibliotheque a gauche")
        print("Les sorties sont : 1. le palier, 2. entree, 3. examiner")
        
        commande = valider_reponse(3)

        if commande == "1":
            palier()
        elif commande == "2":
            lentree()
        else:
            print("")
            print("Voici ce que l'on peut faire :")

            print("1. S asseoir sur le canape")
            print("2. Examiner la bibliotheque")
            print("3. Examiner la tele")

            commande2 = valider_reponse(3)

            if commande2 == "2":
                print("\033[31mNoooonnn des oreilles vertes sortent\033[0m")
                print("de l obscurite et vous chatouillent jusqu'a la mort!!!")
                finpartie()
            
            if commande2 == "3":
                print("Votre BG de pere est en train de faire un massacre")
                print("quel bon joueur!")
                print("")
                petitsalon()

            elif commande2 == "1":
                print("Votre installation pleine de grace")
                print("destabilise votre BG de pere")
                print("il perd sa partie et part en grommelant")
                suivi_aventure.append("petitsalon")  
                print("une piece est coincee dans les coussins...")

                commande4 = valider_reponse(2,"Que voulez vous faire ? 1.Prendre  2.Rien")
                if commande4 == "2":
                    lentree()
                else:
                    print("")
                    print("Incroyable une 20F Coq en etat SUP!!!")
                    print("")
                    ajouter_inventaire("20F")
                    afficher_inventaire()
                    petitsalon()  

def lentree ():
   print("")
   print("Cette entree est un simple couloir... un peu triste")
   print("il y a une porte pour aller a la salle de bain")
   print("et la porte des wc qui est fermee a clef...")
   print("les sorties sont : 1.WC 2.Petit Salon 3. Salle de bain")
 
   commande = valider_reponse(3)   

   if commande == "2":
        petitsalon()
   elif commande == "1":
        wc()
   else:
        sallebain()

def sallebain():
    print("")
    print("Vous arrivez dans la salle de bain")
    print("une sensation bizzare de danger vous envahie")
    print("la lumiere gresille et s eteint parfois")
    print("les sorties sont : 1.Sortir 2.Examiner")

    # Utilisation de valider_reponse avec 2 options
    commande = valider_reponse(2)

    if commande == "1":
        lentree()
    else:
        print("")
        print("Voici ce que l on peut faire :")
        
        # Utilisation de valider_reponse avec 5 options pour les actions à choisir
        print("1. Examiner la salle de bain")
        print("2. Examiner le lavabo")
        print("3. Examiner la baignoire")
        print("4. Examiner la pile de vetements")
        print("5. Sortir")

        commande2 = valider_reponse(5)

        if commande2 == "5":
            lentree()
        elif commande2 == "2":
            print("")
            print("Vous trouvez un parfum... etrange...")
            print("il est ecrit dessus : votre protection si")
            print("ca pue vraiment mais vraiment...")
            ajouter_inventaire("parfum")
            afficher_inventaire()
            sallebain()
        else:
            print("")
            print("\033[31mUne main (verte encore..) sort de l'eau\033[0m")
            print("et vous fait manger des radis empoisonnes")
            finpartie()

def wc():
    global score
    print("")
        
    if "clef" not in inventaire:
        print("")
        print("cette porte est fermee a clef...")
        print("\033[32mu... et vous n'avez pas cette clef...\033[0m")
        print("")
        lentree()
    else:
        print("Mais... vous aviez la clef des wc ... dans votre lit...")
        print("Vous entrez dans les WC, ca sent tres fort,")
        print("un tableau est accroche au mur. Une petite porte")
        print("est fermee dans le fond de la piece.")
        print("les sorties sont : 1.Sortir 2.Examiner")
        
        # Utilisation de valider_reponse avec 2 options
        commande = valider_reponse(2)

        if commande == "1":
            lentree()
        else:
            print("")
            print("Voici ce que l'on peut faire :")
            
            # Utilisation de valider_reponse avec 4 options pour les actions à choisir
            print("1. Examiner le tableau")
            print("2. Examiner les wc")
            print("3. Ouvrir la petite porte")
            print("4. Sortir")
            
            commande2 = valider_reponse(4)

            if commande2 == "4":
                lentree()
            elif commande2 == "2":
                print("")
                print("ca pue!")
                if "parfum" in inventaire:
                    print("vous avez failli vous empoisonner mais...")
                    print("votre etrange parfum vous a sauve !!!")
                    print("")
                    wc()
                else:
                    print("Mais.... quelle idee d'aller voir les wc!!!")
                    print("cette odeur est inqualifiable...ou des radis moisis")
                    print("\033[31mvotre nez se met a saigner... vous mourrez...\033[0m")
                    finpartie()
             
            
            elif commande2 == "1":
                print("")
                print("\033[32mun diablotin y est represente, il est vert\033[0m")
                print("et a des grandes oreilles, il vous regarde")
                if "livre_lu" not in suivi_aventure:
                    print("mechamment... brrr...")
                    print("")
                    wc()
                else:
                    print("en souriant, une femme est a cote de lui.")
                    print("il est ecrit en dessous : Moi et Pixiebis")
                    print("")
                    wc()
            
            else:
                if "clef_alix" in inventaire:
                    print("la clef d'Alix ouvre la porte secrete...")
                    score += 5
                    jardin()
                else:
                    print("Vous n'avez pas la clef...")
                    wc()


def jardin():
    print("")
    print("Un immense diablotin vert a grandes oreilles")
    print("est au milieu du jardin")
    print("un tapis de radis est a ses pieds")
    print("la porte se referme derriere vous bruyamment...")
    print("les sorties sont : 1. Courir 2. Manger des radis 3. Se battre 4. Sourire 5. Prendre un objet 6. Crier tres fort")
    
    commande = valider_reponse(6)

    if commande == "5":

        if not inventaire:
            print("Votre inventaire est vide ! Vous ne pouvez rien utiliser.")
            print("Ce magnifique diablotin vous ... ecrabouille")
            finpartie()
        else:
            print("")
            print("Voici votre inventaire :")
            for i in range(len(inventaire)):
                print(str(i + 1) + ". " + inventaire[i])
            

            choix_objet = valider_reponse(len(inventaire), message="Choisissez un objet a utiliser : ")
            objet_choisi = inventaire[int(choix_objet) - 1]
            

            if objet_choisi == "photo_pixiebis":
                victoire()
            else:
                print("\033[31mCe magnifique diablotin vous ... ecrabouille\033[0m")
                finpartie()
    else:
        print("\033[31mCe magnifique diablotin vous ... ecrabouille\033[0m")
        finpartie()


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
