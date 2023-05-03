from ast import excepthandler
from cProfile import label  #importe la fonction label du module cProfile.
from distutils.cmd import Command
from email.mime import image
from logging import root
import operator 
from re import L  #importe la constante L du module re pour activer le mode « localisation » des expressions régulières.     
from tkinter import * # pour importer la bibliotheque tkinter
from subprocess import call  #importe la fonction call du module subprocess.
from tkinter import ttk, messagebox #importe la sous-bibliothèque ttk et le module messagebox du module tkinter. 
from turtle import bgcolor, title  #importe les fonctions bgcolor et title du module turtle.
 #permetre de gerer les selcetions et les message derrueeur  afficher ou de securite
import pymysql #pour récuperer la bibliotheque de la base de donnée
  
                    
class gestionlivres:  #classe formulaire
    def __init__(self,root):                   
        self.Pagegestionlivres = root  
        self.Pagegestionlivres.title("Gestion des livres")#Titre de l'application gestion livres
        self.Pagegestionlivres.geometry("1040x560+400+200")#Taille de notre Application    

        self.Pagegestionlivres.resizable(width=False, height=False) #eviter d'agrandir la fenetre  
        self.Pagegestionlivres.iconbitmap("bibliothequeBIBYASO/Images/bib.ico") #Icone de l'application 
        

        #Déclarer des variables pour ensuite les récuperer
        self.id = StringVar()
        self.titre = StringVar()
        self.auteurs = StringVar()
        self.collections = StringVar()
        self.nbrExemplaire = StringVar()
        self.recherche_par= StringVar()
        self.recherche = StringVar()


        
        #Container 
        self.Paneauvertdegestionlivres = Frame(self.Pagegestionlivres, bg="#bedb0d") 
        self.Paneauvertdegestionlivres.place(x=190, y=0, width=1100, height=1000)

        self.Paneauorangedegestionlivres = Frame(self.Pagegestionlivres, bg="#ff7f00")
        self.Paneauorangedegestionlivres.place(x=0, y=0, width=190, height=1000)

        
        #Boutons Images
        self.ImageGestionLivresDeLaPageGestionlivres = PhotoImage(file="bibliothequeBIBYASO/Images/Gestionlivre.png")
        self.BoutonGestionLivresDeLaPageGestionlivres = Button(self.Pagegestionlivres,cursor="hand2",image=self.ImageGestionLivresDeLaPageGestionlivres, width=184,height=90, bg="#ff7f00",font="arial 12 bold")
        self.BoutonGestionLivresDeLaPageGestionlivres.place(x=0 , y=0) 
       

        self.ImageAdherentDeLaPageGestionlivres = PhotoImage(file="bibliothequeBIBYASO/Images/Emprunteur.png")
        self.BoutonGestionLivresDeLaPageGestionlivres = Button(self.Pagegestionlivres,cursor="hand2",command=self.VersPageAdherents, text="",image=self.ImageAdherentDeLaPageGestionlivres, width=184, height=90, bg="#ff7f00",font="arial 12 bold")
        self.BoutonGestionLivresDeLaPageGestionlivres.place(x=0 , y=140) 

        self.ImageGestionDesPretsDeLaPageGestionlivres = PhotoImage(file="bibliothequeBIBYASO/Images/Emprunter.png")
        self.BoutonGestionDesPretsDeLaPageGestionlivres = Button(self.Pagegestionlivres,cursor="hand2",command=self.VersPageGestionDesPrets, text="",image=self.ImageGestionDesPretsDeLaPageGestionlivres, width=184, height=90, bg="#ff7f00",font="arial 12 bold")
        self.BoutonGestionDesPretsDeLaPageGestionlivres.place(x=0 , y=280) 

        self.ImageSeDeconnecterDeLaPageGestionlivres = PhotoImage(file="bibliothequeBIBYASO/Images/Sedeconnecter.png")
        self.BoutonSeDeconnecterDeLaPageGestionlivres = Button(self.Pagegestionlivres,cursor="hand2", text="",command=self.BoutonDeconnexion,image=self.ImageSeDeconnecterDeLaPageGestionlivres, width=184, height=90, bg="#ff7f00",font="arial 12 bold")
        self.BoutonSeDeconnecterDeLaPageGestionlivres.place(x=0 , y=420) 
        
        
        
        #les titres
        titreGestionlivre = Label(self.Pagegestionlivres, text=" Gestion des livres ",font =("algarian", 20,"bold"), bg="#bedb0d", fg="black")
        titreGestionlivre.place(x=350, y=20,width=500)
        
        titreGestionlivres = Label(self.Pagegestionlivres, text="Livres", font =("algarian", 15,"bold"), bg="#ff7f00", fg="black")
        titreGestionlivres.place(x=0, y=100,width=190)

        titreAdherents = Label(self.Pagegestionlivres, text=" Emprunteur",font =("algarian", 15,"bold"), bg="#ff7f00", fg="black")
        titreAdherents.place(x=0, y=240,width=190)
        
        titreGestionprets = Label(self.Pagegestionlivres, text=" Prêts", font =("algarian", 15,"bold"), bg="#ff7f00", fg="black")
        titreGestionprets.place(x=0, y=380,width=190)

        titreSedeconnecter = Label(self.Pagegestionlivres, text=" Se déconnecter",font =("algarian", 15,"bold"), bg="#ff7f00", fg="black")
        titreSedeconnecter.place(x=0, y=520,width=190)
        
        titreGestionprets = Label(self.Pagegestionlivres, text="Rechercher les livres disponible par:",font =("algarian", 12,"bold"), bg="#bedb0d", fg="black")
        titreGestionprets.place(x=210, y=90,width=300)



        #champs de saisie pour rechercherun livre
        self.rechercherlivres= Entry(self.Pagegestionlivres,textvariable=self.recherche, font= (5), bg="white")
        self.rechercherlivres.place(x=640, y=90,width=150)


        #Boutons
        BoutonRechercherUnLivre = Button(self.Pagegestionlivres,command=self.ClickBoutonRechercher ,text=" Rechercher ",cursor="hand2", font=("times new roman",11), bd=0,bg="white",fg="black")
        BoutonRechercherUnLivre.place(x=830, y=90)

        BoutonActualiser = Button(self.Pagegestionlivres,command=self.actualiser, text=" Actualiser ",cursor="hand2", font=("times new roman",11), bd=0,bg="white",fg="black")
        BoutonActualiser.place(x=920, y=90)

        BoutonAjouterlivre = Button(self.Pagegestionlivres,command=self.BoutonAjouterUnlivre, text="  Ajouter un livre ",cursor="hand2", font=("times new roman",11), bd=0,bg="white",fg="black")
        BoutonAjouterlivre.place(x=215, y=500)
        
        BoutonSupprimerUnlivre = Button(self.Pagegestionlivres, command=self.SupprimerDesLivres, text=" Supprimer un livre ",cursor="hand2", font=("times new roman",11), bd=0,bg="white",fg="black")
        BoutonSupprimerUnlivre.place(x=910, y=500)
        #cursor="hand2" pour mettre en mode cliquer sur un lien   
        

        #liste pour rechercher un livre
        Listepourcherchercherunlivre = ttk.Combobox(self.Pagegestionlivres,textvariable=self.recherche_par, font=("times new roman", 15), state="readonly")
        Listepourcherchercherunlivre["values"]=("titreLivre") 
        Listepourcherchercherunlivre.place(x=510, y=90, width=110)
        Listepourcherchercherunlivre.current(0)
       

       

        """
        style = ttk.Style()
        style.configure("green.TFrame", background="#4c9294")
        style="green.TFrame"
        """
        #Cadre pour le tableau "self.gestion livres"

        CadrePourTbaleauGestionlivres = Frame(self.Pagegestionlivres, bd=5,relief=GROOVE,bg="green")
        CadrePourTbaleauGestionlivres.place(x=215, y=130,width=800, height=350) 

        #barre de defilement
        barrededefilementX= Scrollbar(CadrePourTbaleauGestionlivres,orient=HORIZONTAL)
        barrededefilemenY = Scrollbar(CadrePourTbaleauGestionlivres, orient=VERTICAL) 
        
        
       # Création d'un tableau avec plusieurs colonnes pour gérer les livres
        self.TableauGestionlivres = ttk.Treeview(CadrePourTbaleauGestionlivres, columns=("titre", "auteur", "collection","nbrexemplaire"), xscrollcommand=barrededefilementX.set, yscrollcommand=barrededefilemenY.set)
        
        # Ajout de la barre de défilement horizontale en bas du tableau
        barrededefilementX.pack(side=BOTTOM, fill=X)

        # Ajout de la barre de défilement verticale à droite du tableau
        barrededefilemenY.pack(side=RIGHT, fill=Y) 


        # Création du tag "ligne" avec une couleur de fond verte
        self.TableauGestionlivres.tag_configure("ligne", background="#4c9294")

        # Ajout des données à chaque ligne
        for i in range(10):
            self.TableauGestionlivres.insert("", "end", values=( "titreLivre", "nomAuteur", "nomCollection", "nbrExemplaire"))

            # Appliquer le tag "ligne" à chaque ligne
            self.TableauGestionlivres.tag_bind(i, "<1>", lambda event, tag="ligne": self.TableauGestionlivres.item(event.widget.focus(), tags=(tag)))

        

        # Ajout des titres de chaque colonne
     
        self.TableauGestionlivres.heading("titre", text="titreLivre")
        self.TableauGestionlivres.heading("auteur", text="nomAuteur")
        self.TableauGestionlivres.heading("collection", text="nomCollection")
        self.TableauGestionlivres.heading("nbrexemplaire", text="nbrExemplaire")
        
        
        
        

        # Affichage seulement des titres de chaque colonne (pas les données)
        self.TableauGestionlivres["show"] = "headings"
        

        # Définition de la largeur de chaque colonne
      
        self.TableauGestionlivres.column("titre", width=80)
        self.TableauGestionlivres.column("auteur", width=80)
        self.TableauGestionlivres.column("collection", width=80)
        self.TableauGestionlivres.column("nbrexemplaire", width=80)
        
        
        

        # Ajout du tableau au cadre et remplissage de l'espace disponible
        self.TableauGestionlivres.pack(side=TOP, fill=X)
        self.TableauGestionlivres.pack(fill=BOTH, expand=1)

        # Ajout d'un événement pour récupérer les informations d'une ligne lorsque l'utilisateur clique dessus
        self.TableauGestionlivres.bind("<ButtonRelease-1>",self.RecupereInformation)

        # Actualisation de la page pour afficher les nouvelles lignes ajoutées
        self.actualiser()
    
    
    #Fonction ClickBoutonRechercher pour afficher les livres
    def ClickBoutonRechercher(self):
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



                execut.execute("SELECT titreLivre,nomAuteur,nomCollection,nbrExemplaire from livre WHERE "+str(self.recherche_par.get())+" LIKE '%"+str(self.recherche.get())+"%' HAVING livre.titreLivre LIKE '%{}%';".format(self.recherche.get()))
                lignes = execut.fetchall()
                if len(lignes)!=0:
                 self.TableauGestionlivres.delete(*self.TableauGestionlivres.get_children())
                for ligne in lignes:
                    self.TableauGestionlivres.insert('', END, values=ligne)
                connectionbdd.commit()
                connectionbdd.close()

    #Fonction VersPageAdherents pour aller vers la page adhérent
    def VersPageAdherents(self):
        self.Pagegestionlivres.destroy()
        call(["python", "bibliothequeBIBYASO/Emprunteur.py"]) 

    #Fonction VersPageAdherents pour aller vers la page gestion des prets
    def VersPageGestionDesPrets(self):
        self.Pagegestionlivres.destroy()
        call(["python", "bibliothequeBIBYASO/Gestiondesprets.py"]) 

    #Fonction BoutonAjouterUnlivre pour aller vers la page qui permet d'ajouter des nouveaux livres
    def BoutonAjouterUnlivre(self):
        self.Pagegestionlivres.destroy()
        call(["python", "bibliothequeBIBYASO/Ajouterdeslivres.py"]) 
    
    #Fonction BoutonDeconnexion qui permet de se deconnecter
    def BoutonDeconnexion(self): #fonction deconexion pour pouvoir se deconecter qui prend pour parametre self
        lemessagebox = messagebox.askyesno("Déconnexion","Voulez-vous vous déconnecter", parent=self.Pagegestionlivres) #message box pour pouvoir se deconnecter
        if lemessagebox == YES: #si le la colonne yes a était selectionner  
         self.Pagegestionlivres.destroy() # fermer la fenetre                             
         call(["python", "bibliothequeBIBYASO/Connexion.py"]) #appeler la page connexion 
         

    #Fonction Actualiser qui permet d'actaliser notre page
    def actualiser(self):
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
                execut.execute("SELECT titreLivre,nomAuteur,nomCollection,nbrExemplaire from livre") #ligne sql pour récuperer la table ajoutlivres
                lignes= execut.fetchall()
                if len(lignes)!= 0: #si la liste est vide 
                    self.TableauGestionlivres.delete(*self.TableauGestionlivres.get_children())
                    for ligne in lignes:
                        self.TableauGestionlivres.insert("", END, values=ligne)
                connectionbdd.commit()#
                connectionbdd.close()#ferme la connexion à la base de données

    
    #Fonction RecupereInformation 
    def RecupereInformation(self,ev): 
        cursor_row = self.TableauGestionlivres.focus()
        contents = self.TableauGestionlivres.item(cursor_row)
        row = contents["values"]
   
        self.titre.set(row[0]),
        self.auteurs.set(row[1]),
        self.collections.set(row[2]),
        self.nbrExemplaire.set(row[3]),

    
    def SupprimerDesLivres(self): #fonction supprimer pour supprimer des livres
        if self.titre.get()=="":
            messagebox.showerror("Erreur", "Veuillez, sélectionner un livre à supprimer", parent=self.Pagegestionlivres) #si tout les champs ne sont pas rempli alors affiche un message box pour dire que les champs ne sont pas rempli
        else:
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

            # Vérifier s'il y a des emprunts en cours pour le livre à supprimer
            execut.execute("SELECT COUNT(*) FROM emprunt WHERE titreLivre = %s", self.titre.get())
            count = execut.fetchone()[0]

            if count > 0:
                messagebox.showerror("Erreur", "Impossible de supprimer le livre. Des emprunts sont en cours pour ce livre. Veuillez supprimer les emprunts avant de supprimer le livre.", parent=self.Pagegestionlivres)
            else:
                # Supprimer les lignes enfants dans la table "exemplaire" qui référencent le livre à supprimer
            

                # Supprimer la ligne parente dans la table "livre"
                execut.execute("DELETE FROM livre WHERE titreLivre = %s", self.titre.get())

                connectionbdd.commit()
                messagebox.showinfo("Succes","le livre à bien été supprimé", parent=self.Pagegestionlivres)
                self.actualiser()
                connectionbdd.close() #elle permet de fermer une connexion à une base de données



root =Tk()
obj = gestionlivres(root)
root.mainloop()

