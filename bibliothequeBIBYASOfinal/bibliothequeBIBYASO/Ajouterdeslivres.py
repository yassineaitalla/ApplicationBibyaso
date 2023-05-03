from ast import Delete, excepthandler
from cProfile import label
from email.mime import image
from logging import root
from re import L
from tkinter import * #pour importer la bibliotheque tkinter
from subprocess import call #Bibliotheque qui permet de faire appel au page sur les quelles on clique
from tkinter import ttk, messagebox #permetre de gerer les selcetions et les message derrueeur  afficher ou de securite
from turtle import bgcolor, title #permet d'importer les background et les titres
import pymysql #bibliotheque pour faire des requettes vers la base de donnes
     

class AjoutLivres:  # 
    def __init__(self,root):                   
        self.PageAjouterDesLivres = root
        self.PageAjouterDesLivres.title("Ajouter des livres") #titre Ajouter un livre
        self.PageAjouterDesLivres.geometry("1040x560+400+200") #taille de l'application
        self.PageAjouterDesLivres.resizable(width=False, height=False)# eviter d'agrandir la fenetre
        self.PageAjouterDesLivres.iconbitmap("bibliothequeBIBYASO/Images/bib.ico") 



        #On déclare des variables pour ensuite les récuperer
        self.TitreLivre = StringVar()
        self.Auteurs = StringVar()
        self.AuteursPrenom = StringVar()
        self.Collections = StringVar()
        self.nbrExemplaire = StringVar()
        
        
        #Panneau vert gestion livres
        self.Paneauvertdegestionlivres = Frame(self.PageAjouterDesLivres, bg="#bedb0d")
        self.Paneauvertdegestionlivres.place(x=190, y=0, width=1100, height=1000)

        #Panneau orange gestion livres
        Paneauorangedegestionlivres = Frame(self.PageAjouterDesLivres, bg="#ff7f00")
        Paneauorangedegestionlivres.place(x=0, y=0, width=190, height=1000)

        #PhotoBoutons
        self.ImageGestionlivres = PhotoImage(file="bibliothequeBIBYASO/Images/Gestionlivre.png")
        self.BoutonImagesGestionlivre = Button(self.PageAjouterDesLivres,cursor="hand2",command=self.VersGestionlivres, text="",image=self.ImageGestionlivres, width=184,height=90, bg="#ff7f00",font="arial 12 bold")
        self.BoutonImagesGestionlivre.place(x=0 , y=0) 
        
        self.ImageAdherents = PhotoImage(file="bibliothequeBIBYASO/Images/Emprunteur.png")
        self.BoutonImageAdherents = Button(self.PageAjouterDesLivres,cursor="hand2",command=self.VersAdherents ,text="",image=self.ImageAdherents, width=184, height=90, bg="#ff7f00",font="arial 12 bold")
        self.BoutonImageAdherents.place(x=0 , y=140) 

        self.ImageEmprunter = PhotoImage(file="bibliothequeBIBYASO/Images/Emprunter.png")
        self.BoutonImageEmprunter = Button(self.PageAjouterDesLivres,cursor="hand2",command=self.VersGestiondesprets, text="",image=self.ImageEmprunter, width=184, height=90, bg="#ff7f00",font="arial 12 bold")
        self.BoutonImageEmprunter.place(x=0 , y=280) 

        self.ImageSedeconnecter = PhotoImage(file="bibliothequeBIBYASO/Images/Sedeconnecter.png")
        self.BoutonImageSedeconnecter = Button(self.PageAjouterDesLivres,cursor="hand2", text="",command=self.PourSedeconnecter,image=self.ImageSedeconnecter, width=184, height=90, bg="#ff7f00",font="arial 12 bold")
        self.BoutonImageSedeconnecter.place(x=0 , y=420)


        #Titres
        titregestionlivres = Label(self.PageAjouterDesLivres, text=" Livres ",font =("algarian", 15,"bold"), bg="#ff7f00", fg="black")
        titregestionlivres.place(x=0, y=100,width=190)

        titreadherents = Label(self.PageAjouterDesLivres, text=" Emprunteur",font =("algarian", 15,"bold"), bg="#ff7f00", fg="black")
        titreadherents.place(x=0, y=240,width=190)

        titregestionprets = Label(self.PageAjouterDesLivres, text=" Prêts",font =("algarian", 15,"bold"), bg="#ff7f00", fg="black")
        titregestionprets.place(x=0, y=380,width=190)

        titresedeconnecter = Label(self.PageAjouterDesLivres, text=" Se déconnecter",font =("algarian", 15,"bold"), bg="#ff7f00", fg="black")
        titresedeconnecter.place(x=0, y=520,width=190) 

        titregestionlivretitre = Label(self.PageAjouterDesLivres, text=" Ajout de livres ",font =("algarian", 20,"bold"), bg="#bedb0d", fg="black")
        titregestionlivretitre.place(x=350, y=20,width=500)

        titre = Label(self.PageAjouterDesLivres, text=" Titre du livre ",font =("algarian", 12,"bold"), bg="#bedb0d", fg="black")
        titre.place(x=253, y=150,width=200)

        auteur = Label(self.PageAjouterDesLivres, text=" Nom de l'auteur ",font =("algarian", 12,"bold"), bg="#bedb0d", fg="black")
        auteur.place(x=270, y=200,width=200)

        prenomauteur = Label(self.PageAjouterDesLivres, text=" Prénom de l'auteur ",font =("algarian", 12,"bold"), bg="#bedb0d", fg="black")
        prenomauteur.place(x=282, y=250,width=200)

        collections = Label(self.PageAjouterDesLivres, text=" Nom de collection ",font =("algarian", 12,"bold"), bg="#bedb0d", fg="black")
        collections.place(x=280, y=300,width=200)

        nombreExemplaire = Label(self.PageAjouterDesLivres, text=" Nombre d'exemplaire ",font =("algarian", 12,"bold"), bg="#bedb0d", fg="black")
        nombreExemplaire.place(x=292, y=350,width=200)

        


        
        #Bouton "Ajouter un livre"
        BoutonAjouterUnlivre = Button(self.PageAjouterDesLivres,command=self.ClickAjouterUnLivre, text="Ajouter ",cursor="hand2", font=("times new roman",11), bd=0,bg="white",fg="black")
        BoutonAjouterUnlivre.place(x=640, y=380)

        
        #Champs de saisie
        self.champsdesaisietitreLivre= Entry(self.PageAjouterDesLivres,textvariable=self.TitreLivre, font= (5), bg="white")
        self.champsdesaisietitreLivre.place(x=500, y=150,width=150)

        self.champsdesaisieauteurs= Entry(self.PageAjouterDesLivres, textvariable=self.Auteurs,font= (5), bg="white")
        self.champsdesaisieauteurs.place(x=500, y=200,width=150)

        self.champsdesaisiePrenomauteurs= Entry(self.PageAjouterDesLivres, textvariable=self.AuteursPrenom,font= (5), bg="white")
        self.champsdesaisiePrenomauteurs.place(x=500, y=250,width=150)


        self.champsdesaisiecollections= Entry(self.PageAjouterDesLivres,textvariable=self.Collections, font= (5), bg="white")
        self.champsdesaisiecollections.place(x=500, y=300,width=150)

        self.champsdesaisieNombrexemplaire= Entry(self.PageAjouterDesLivres,textvariable=self.nbrExemplaire, font= (5), bg="white")
        self.champsdesaisieNombrexemplaire.place(x=500, y=350,width=150)

        

    #Fonction Supprimer les champs de saisie
    def SupprimerChampsDeSaisieAjouterDesLivres(self): #On déclare la fonction pour effacer les champs de saisie apres avoir saisie un livre
        self.champsdesaisietitreLivre.delete(0, END)
        self.champsdesaisieauteurs.delete(0, END)
        self.champsdesaisiecollections.delete(0, END)
        
    def get_id_livre(self, nom_livre):

                import configparser
                import pymysql

                # Créer un objet ConfigParser pour lire le fichier de configuration
                config = configparser.ConfigParser()
                config.read('bibliothequeBIBYASO/config.ini')

                # Lire les informations de connexion depuis la section 'database' du fichier
                host = config.get('database', 'host', fallback='localhost')
                user = config.get('database', 'user', fallback='root')
                password = config.get('database', 'password', fallback='')
                database = config.get('database', 'database', fallback='')

                # Se connecter à la base de données
                connectionbdd = pymysql.connect(host=host, user=user, password=password, database=database)
                self.connectionbdd = pymysql.connect(host=host, user=user, password=password, database=database)
                 
                self.execut = self.connectionbdd.cursor()

                """
                Récupère l'ID de l'emprunteur à partir de son nom dans la base de données
                :param nom_emprunteur: Nom de l'emprunteur dont on veut récupérer l'ID
                :return: ID de l'emprunteur, ou None si l'emprunteur n'existe pas dans la base de données
                """
                
                id_livre = None
                try:
                    self.execut.execute("SELECT idLivre FROM livre WHERE titreLivre = %s", (nom_livre,))
                    row = self.execut.fetchone()
                    if row is not None:
                        id_livre = row[0]
                except pymysql.Error as error:
                    print("Erreur de connexion: {}".format(error))
                return id_livre
            

    #Fonction ClickAjouterUnLivre pour inserer une livre dans la bse de données
    def ClickAjouterUnLivre(self):
    # Fonction appelée lorsque le bouton "Ajouter un livre" est cliqué dans l'interface utilisateur.
    
        # Vérifie que tous les champs obligatoires sont remplis
        if self.TitreLivre.get()=="" or self.Auteurs.get()=="" or self.AuteursPrenom.get()=="" or self.Collections.get()=="" or self.champsdesaisieNombrexemplaire.get()=="":
            # Affiche une boîte de dialogue avec un message d'erreur si un champ obligatoire est vide
            messagebox.showerror("Erreur", "Veuillez remplir tout les champs", parent=self.PageAjouterDesLivres)
        else:
            try:
                # Établit une connexion à la base de données MySQL
                import configparser
                import pymysql

                # Créer un objet ConfigParser pour lire le fichier de configuration
                config = configparser.ConfigParser()
                config.read('bibliothequeBIBYASO/config.ini')

                # Lire les informations de connexion depuis la section 'database' du fichier
                host = config['database']['host']
                user = config['database']['user']
                password = config['database']['password']
                database = config['database']['database']

                connectionbdd = pymysql.connect(host=host, user=user, password=password, database=database)

                # Crée un curseur pour exécuter des requêtes sur la base de données
                execut = connectionbdd.cursor()

                
                # Exécute une requête pour vérifier si le livre est déjà dans la base de données
                execut.execute("select * from livre where titreLivre=%s",self.TitreLivre.get())
                ligne= execut.fetchone()

                # Si le livre est déjà présent dans la base de données, affiche une boîte de dialogue avec un message d'erreur
                if ligne != None:
                    messagebox.showerror("Erreur", "Ce livre existe deja", parent=self.PageAjouterDesLivres)
                else:
                    id_livre = self.get_id_livre(self.TitreLivre.get())
                    # Exécute une requête pour ajouter le livre dans la base de données en utilisant les identifiants de l'auteur et de la collection
                    execut.execute("INSERT INTO livre (idLivre,titreLivre,nomAuteur,prenomAuteur,nomCollection,nbrExemplaire) VALUES (null,%s,%s,%s,%s,%s)", 
                        (
                        self.TitreLivre.get(),
                        self.Auteurs.get(),
                        self.AuteursPrenom.get(),
                        self.Collections.get(),
                        self.nbrExemplaire.get()
                        
                        ))
                  

                
                    # Affiche une boîte de dialogue avec un message de succès
                    messagebox.showinfo("Succes", "Le livre à bien était ajouté", parent=self.PageAjouterDesLivres) 
                    
                    # Efface les champs de saisie dans l'interface utilisateur
                    self.SupprimerChampsDeSaisieAjouterDesLivres 
                    
                # Enregistre les modifications dans la base de données
                connectionbdd.commit()
                
                # Ferme la connexion à la base de données
                connectionbdd.close
                
            except Exception as es :
                # Si une erreur se produit lors de la connexion à la base de données ou lors de l'exécution des requêtes, affiche une boîte de dialogue avec un message d'erreur
                messagebox.showerror("erreur",f"Erreur de connexion{str(es)}",parent=self.PageAjouterDesLivres)


            

    
    #Fonctions VersAdherents pour aller vers la page adhérent
    def VersAdherents(self):
        self.PageAjouterDesLivres.destroy() 
        call(["python", "bibliothequeBIBYASO/Emprunteur.py"])

    #Fonctions VersGestiondesprets pour aller vers la page gestiondesprets
    def VersGestiondesprets(self):
        self.PageAjouterDesLivres.destroy()
        call(["python", "bibliothequeBIBYASO/Gestiondesprets.py"])

    #Fonctions VersGestionLivres pour aller vers la page gestonLivres    
    def VersGestionlivres(self):
        self.PageAjouterDesLivres.destroy()
        call(["python", "bibliothequeBIBYASO/Gestionlivres.py"])

    #Fonctions PourSedeconnecter 
    def PourSedeconnecter(self):
        lemessagebox = messagebox.askyesno("Déconnexion","Voulez-vous vous déconnecter", parent=self.PageAjouterDesLivres)
        if lemessagebox == YES:
         self.PageAjouterDesLivres.destroy()
         call(["python", "bibliothequeBIBYASO/Connexion.py"])

    
    

root =Tk()
obj = AjoutLivres(root)
root.mainloop()