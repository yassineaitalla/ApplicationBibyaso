from tkinter import * #importer la bibliotheque tkinte
import tkinter as tk  #
from tkinter import ttk, messagebox #bibliotheque pour afficher nos message d'erreur dans l'application
from turtle import bgcolor, title #permetre de gerer les selections et les message derreur  afficher ou de securite
from tkcalendar import * #Bibliothéque pour importer les calendrier 
import pymysql #bibliotheque pour interagir avec la base de données
#import os #faire des actions diretement au niveau du systeme  
from subprocess import call   #bibliotheque pour pouvoir changer de page  


                    
class gestionprets:  # classe 
    def __init__(self,root):  #constructeur                  
        self.PageGestiondesprets = root #changer
        self.PageGestiondesprets.title("Gestion des Prets") #titre de la fenetre 
        self.PageGestiondesprets.geometry("1040x560+400+200")#pour gerer la taille de l'application
        self.PageGestiondesprets.config(bg="#784cd4")
        self.PageGestiondesprets.resizable(width=False, height=False)#Pour eviter d'agrandir notre application
        self.PageGestiondesprets.iconbitmap("bibliothequeBIBYASO/Images/bib.ico")  #pour gerer l'icone de notre application
       
        
        self.idEmprunt = StringVar()  
       
        self.var_iddelhadherent = StringVar()  
        self.var_nomEmprunteur = StringVar()

        self.var_dateemprunt = StringVar()  # on declare des variables pour ensuite les recuperer
        self.var_titreLivre = StringVar()
        self.var_dateretour = StringVar()

        self.recherche_par = StringVar()
        self.recherche = StringVar()
        self.nomdelhadherent_list=[]
        self.livre=[]
        

        
        self.Emprunteur=[]
        self.ListeEmprunteurEtLivre()

        
        


        self.Paneauvertdegestionlivres = Frame(self.PageGestiondesprets, bg="#bedb0d")
        self.Paneauvertdegestionlivres.place(x=190, y=0, width=1100, height=1000)

        Paneauorangedegestionlivres = Frame(self.PageGestiondesprets, bg="#ff7f00")
        Paneauorangedegestionlivres.place(x=0, y=0, width=190, height=1000)


        self.ImageGestionlivres = PhotoImage(file="bibliothequeBIBYASO/Images/Gestionlivre.png")
        self.BoutonPourAllerVersGestionLivres = Button(self.PageGestiondesprets,cursor="hand2",command=self.VersGestionLivres, text="",image=self.ImageGestionlivres, width=184,height=90, bg="#ff7f00",font="arial 12 bold")
        self.BoutonPourAllerVersGestionLivres.place(x=0 , y=0) 
        
        self.ImageAdherents = PhotoImage(file="bibliothequeBIBYASO/Images/Emprunteur.png")
        self.BoutonPourAllerVersAdherents = Button(self.PageGestiondesprets,cursor="hand2",command=self.VersAdherents, text="",image=self.ImageAdherents, width=184, height=90, bg="#ff7f00",font="arial 12 bold")
        self.BoutonPourAllerVersAdherents.place(x=0 , y=140) 

        self.ImageGestionDesprets = PhotoImage(file="bibliothequeBIBYASO/Images/Emprunter.png")
        self.BoutonPourAllerVersGestionDesprets = Button(self.PageGestiondesprets, cursor="hand2",text="",image=self.ImageGestionDesprets, width=184, height=90, bg="#ff7f00",font="arial 12 bold")
        self.BoutonPourAllerVersGestionDesprets.place(x=0 , y=280) 

        
        self.ImageSedeconnecter = PhotoImage(file="bibliothequeBIBYASO/Images/Sedeconnecter.png")
        self.BoutonPourSedeconnecter = Button(self.PageGestiondesprets,cursor="hand2", text="",command=self.PourSeDeConnecter,image=self.ImageSedeconnecter, width=184, height=90, bg="#ff7f00",font="arial 12 bold")
        self.BoutonPourSedeconnecter.place(x=0 , y=420) 

        

        #titres
        titreGestionprets = Label(self.PageGestiondesprets, text=" Gestion des Prêts ",font =("algarian", 20,"bold"), bg="#bedb0d", fg="black")
        titreGestionprets.place(x=350, y=20,width=500)
        
        titreGestionlivres = Label(self.PageGestiondesprets, text=" Livres ",font =("algarian", 15,"bold"), bg="#ff7f00", fg="black")
        titreGestionlivres.place(x=0, y=100,width=190)

        titreAdherents = Label(self.PageGestiondesprets, text=" Emprunteur ",font =("algarian", 15,"bold"), bg="#ff7f00", fg="black")
        titreAdherents.place(x=0, y=240,width=190)

        titreGestiondesprets = Label(self.PageGestiondesprets, text=" Prêts",font =("algarian", 15,"bold"), bg="#ff7f00", fg="black")
        titreGestiondesprets.place(x=0, y=380,width=190)

        titreSedeconnecter = Label(self.PageGestiondesprets, text=" Se déconnecter",font =("algarian", 15,"bold"), bg="#ff7f00", fg="black")
        titreSedeconnecter.place(x=0, y=520,width=190)

        titreRechercherlesemprunts= Label(self.PageGestiondesprets, text=" Rechercher les emprunts par :",font =("algarian", 12,"bold"), bg="#bedb0d", fg="black")
        titreRechercherlesemprunts.place(x=210, y=90,width=250)

        

        Question = ttk.Combobox(self.PageGestiondesprets,textvariable=self.recherche_par, font=("times new roman", 15), state="readonly")
        Question["values"]=("nomEmprunteur","titreLivre") # on recupere le soit l'idEmprunt ou soit le numAdheren
        Question.place(x=455, y=87, width=110) #.place pour la position du ttk.combobox 
        Question.current(0)


        


        self.ChampsDesaisiePourRechercherDeslivres= Entry(self.PageGestiondesprets,textvariable=self.recherche ,font= (5), bg="white")
        self.ChampsDesaisiePourRechercherDeslivres.place(x=570, y=90,width=150)

        BoutonPourRechercherUnEmprunt = Button(self.PageGestiondesprets,command=self.ClickBoutonRechercher, text="Rechercher  ",cursor="hand2", font=("times new roman",11), bd=0,bg="white",fg="black")
        BoutonPourRechercherUnEmprunt.place(x=730, y=90) # command est attribuer a un bouton pour pouvoir l'executer  

        BoutonActualiser = Button(self.PageGestiondesprets,command=self.ClickActualiser, text="Actualiser ",cursor="hand2", font=("times new roman",11), bd=0,bg="white",fg="black")
        BoutonActualiser.place(x=820, y=90) # command est attribuer a un bouton pour pouvoir l'executer  

        BoutonPourAjouterUnlivre = Button(self.PageGestiondesprets,command=self.PageEmprunt, text="Emprunter un livre",cursor="hand2", font=("times new roman",11), bd=0,bg="white",fg="black", )
        BoutonPourAjouterUnlivre.place(x=215, y=500)

        
        BoutonRetournerUnLivre = Button(self.PageGestiondesprets,command=self.RestituerUnEmprunt, text="Rendre un emprunt ",cursor="hand2", font=("times new roman",11), bd=0,bg="white",fg="black")
        BoutonRetournerUnLivre.place(x=890, y=500) 
        # cursor pour mettre la main quand on clique sur le bouton 
       

       
        

        CadreDuTableauGestiondesprets = Frame(self.PageGestiondesprets, bd=5,relief=GROOVE,bg="white") # Cela définit le style de la bordure à "GROOVE", qui est un effet de relief pour donner l'impression que le cadre est en relief par rapport à la page parente.
        CadreDuTableauGestiondesprets.place(x=215, y=130,width=800, height=350)

        barrededefilementX = Scrollbar(CadreDuTableauGestiondesprets,orient=HORIZONTAL)
        barrededefilementY = Scrollbar(CadreDuTableauGestiondesprets, orient=VERTICAL)
        
        self.tableauGestiondesprets = ttk.Treeview(CadreDuTableauGestiondesprets,columns=("titrelivre","nomemprunteur","dateemprunt","dateretour"),xscrollcommand=barrededefilementX.set, yscrollcommand=barrededefilementY.set)
        barrededefilementX.pack(side=BOTTOM, fill=X) #crée une barre de défilement horizontale (axe X) pour le widget et la positionne en bas du widget en utilisant l'option side=BOTTOM. L'option fill=X indique que la barre de défilement doit remplir tout l'espace disponible sur l'axe horizontal.
        barrededefilementY.pack(side=RIGHT, fill=Y) #rée une barre de défilement verticale (axe Y) pour le widget et la positionne sur le côté droit du widget en utilisant l'option side=RIGHT. L'option fill=Y indique que la barre de défilement doit remplir tout l'espace disponible sur l'axe vertical.

     
        self.tableauGestiondesprets.heading("nomemprunteur", text="nomEmprunteur")
     
        self.tableauGestiondesprets.heading("titrelivre", text="titrelivre")
        self.tableauGestiondesprets.heading("dateemprunt", text="dateEmprunt")
        self.tableauGestiondesprets.heading("dateretour", text="dateRetour")
        
        
        self.tableauGestiondesprets["show"]="headings" # la clé "show" est utilisée pour accéder à l'option d'affichage des colonnes. En définissant cette option à "headings", seules les en-têtes de colonnes sont affichées

       
        self.tableauGestiondesprets.column("nomemprunteur", width=80)
       
        self.tableauGestiondesprets.column("titrelivre", width=80)
        self.tableauGestiondesprets.column("dateemprunt", width=80)
        self.tableauGestiondesprets.column("dateretour", width=80)
       

        

        self.tableauGestiondesprets.pack(fill=BOTH, expand=1)  #La première ligne de code, "self.tableauGestiondesprets.pack(fill=BOTH, expand=1)", configure un widget d'interface utilisateur appelé "tableauGestiondesprets" pour qu'il prenne autant de place que possible dans la fenêtre principale de l'application.
        self.tableauGestiondesprets.bind("<ButtonRelease-1>",self.information) #Cela signifie que chaque fois que l'utilisateur relâche le bouton de la souris alors qu'il se trouve sur le tableau "tableauGestiondesprets", la fonction "information" sera exécutée pour traiter cet événement.
        self.ClickActualiser()

    

    def ClickActualiser(self):
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
        execut = connectionbdd.cursor()
        execut.execute(" select titreLivre,nomEmprunteur,dateEmprunt,dateRetour from emprunt ") #ligne sql pour récuperer la table ajoutlivres
        lignes= execut.fetchall()
        if len(lignes)!=0:
            self.tableauGestiondesprets.delete(*self.tableauGestiondesprets.get_children())
            for ligne in lignes:
                self.tableauGestiondesprets.insert("", END, values=ligne)
        connectionbdd.commit()
        connectionbdd.close()
    
    def ClickBoutonRechercher(self):
                

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
        execut = connectionbdd.cursor()
        



        execut.execute("SELECT titreLivre,nomEmprunteur,dateEmprunt,dateRetour FROM emprunt WHERE {} LIKE '%{}%'".format(self.recherche_par.get(), self.recherche.get()))
        lignes = execut.fetchall()
        if len(lignes)!=0:  # Vérifie si la liste "lignes" n'est pas vide
           self.tableauGestiondesprets.delete(*self.tableauGestiondesprets.get_children())
           for ligne in lignes: # Pour chaque élément "ligne" de la liste "lignes"
            self.tableauGestiondesprets.insert('', END, values=ligne)
        connectionbdd.commit()
        connectionbdd.close() #ferme la connexion à la base de données

    def information(self,ev):  # on recupere les informations pour ensuite les modifier ou supprimer, ev est un moyen pour la méthode "information" d'obtenir des informations
        ligneselectionner = self.tableauGestiondesprets.focus() # Récupère la ligne actuellement sélectionnée dans le widget "tableauGestiondesprets"
        recuperelesdonnesdelaligneselectionner = self.tableauGestiondesprets.item(ligneselectionner) # Récupère les données de la ligne sélectionnée
        ligne = recuperelesdonnesdelaligneselectionner["values"] # Extrait les valeurs de la ligne sélectionnée et les stocke dans la variable "ligne"
        
        self.var_nomEmprunteur.set(ligne[1]),
        
        self.var_titreLivre.set(ligne[2]), # Met à jour la variable "var_idlivre" avec la troisième valeur de la ligne sélectionnée
        self.var_dateemprunt.set(ligne[3]) # Met à jour la variable "var_dateemprunt" avec la quatrième valeur de la ligne sélectionnée
        self.var_dateretour.set(ligne[4]), # Met à jour la variable "var_dateretour" avec la cinquième valeur de la ligne sélectionnée
        


    def RestituerUnEmprunt(self):
        if self.var_nomEmprunteur.get() == "":
            messagebox.showerror("Erreur", "Veuillez sélectionner un emprunt", parent=self.PageGestiondesprets)
        else:
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
            execut = connectionbdd.cursor() #objet de curseur qui permet d'exécuter des requêtes SQL sur la base de données.
            
            # Récupérer l'idLivre de la ligne sélectionnée
            execut.execute("SELECT idLivre FROM emprunt WHERE nomEmprunteur = %s", self.var_nomEmprunteur.get())
            idLivre = execut.fetchone()[0]
            
            # Supprimer l'emprunt
            execut.execute("DELETE FROM emprunt WHERE nomEmprunteur = %s", self.var_nomEmprunteur.get())

            # Incrémenter la colonne nbrExemplaire de la table livre correspondant à l'idLivre récupéré
            execut.execute("UPDATE livre SET nbrExemplaire = nbrExemplaire + 1 WHERE idLivre = %s", idLivre)

            messagebox.showinfo("Succès", "L'emprunt a bien été rendu, merci.", parent=self.PageGestiondesprets)

            self.ClickActualiser()
            connectionbdd.commit()

            connectionbdd.close()
        






    
    
    
        
        

  

    def PourSeDeConnecter(self):
        messagePoursedeconnecter = messagebox.askyesno("Déconnexion","Voulez-vous vous déconnecter", parent=self.PageGestiondesprets)
        if messagePoursedeconnecter == YES:
         self.PageGestiondesprets.destroy()
         call(["python", "bibliothequeBIBYASO/Connexion.py"])

         
    def VersGestionLivres(self):
        self.PageGestiondesprets.destroy()
        call(["python", "bibliothequeBIBYASO/Gestionlivres.py"]) 
        
    def VersAdherents(self):
        self.PageGestiondesprets.destroy()
        call(["python", "bibliothequeBIBYASO/Emprunteur.py"])


    


    
    def ListeEmprunteurEtLivre(self):  #recuperer les nom et livres dispo dans la base de donnes 
            self.nomdelhadherent_list.append("Vide")
            self.livre.append("Vide")
            self.Emprunteur.append("Vide")
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
            execut = connectionbdd.cursor()
            try:
                

                execut.execute("select titreLivre from livre") #on appel la liste de nos livres
                four=execut.fetchall()
                if len(four)>0:
                    del self.livre[:]
                    self.livre.append("Selectionner un titrelivre")
                    for i in four:
                        self.livre.append(i[0])

                execut.execute("select nomEmprunteur from Emprunteur") #on appel la liste de nos livres
                four=execut.fetchall()
                if len(four)>0:
                    del self.Emprunteur[:]
                    self.Emprunteur.append("Selectionner un nomEmprunteur")
                    for i in four:
                        self.Emprunteur.append(i[0])
                
            except Exception as ex:
                messagebox.showerror("Erreur", f"Erreur de connexion {str(ex)}")

    


    #Fonction de la Page pour les emprunt
    def PageEmprunt(self):          
        self.PageEmprunt= Toplevel() # top level fenetre fille a la fenetre mere 
        self.PageEmprunt.title("Emprunter un livre") # titre de la frame
        self.PageEmprunt.config(bg="#ff7f00")  # background de la frame 
        self.PageEmprunt.geometry("1056x560+400+200") # la taille de la frame
        
        
        self.PageEmprunt.grab_set() # si on lance une fenetre on poura pas cliquer ailleurs 
        self.PageEmprunt.resizable(width=False, height=False) #eviter d'agrandir la fenetre
        self.PageEmprunt.iconbitmap("bibliothequeBIBYASO/Images/bib.ico") 


       

        
        

        
       

        
        #liste pour recuperer les livres
        self.titreComboboxLivre = ttk.Combobox(self.PageEmprunt,values= self.livre, textvariable=  self.var_titreLivre,font=("goudy old style",20), state="readonly", justify=CENTER)
        self.titreComboboxLivre.place(x=500, y=150, width=350)
        self.titreComboboxLivre.current(0)
        

        self.titreComboboxnomadherent = ttk.Combobox(self.PageEmprunt,values= self.Emprunteur, textvariable=self.var_nomEmprunteur,font=("goudy old style",20), state="readonly", justify=CENTER)
        self.titreComboboxnomadherent.place(x=500, y=100, width=385)
        self.titreComboboxnomadherent.current(0)
        
 
        #titres
        

        titrelivre = Label(self.PageEmprunt, text=" Titre du livre ",font =("algarian", 15,"bold"), bg="#ff7f00", fg="black")
        titrelivre.place(x=250, y=150)

        nomAdherent = Label(self.PageEmprunt, text=" Nom de l'emprunteur ",font =("algarian", 15,"bold"), bg="#ff7f00", fg="black")
        nomAdherent.place(x=250, y=100)

        self.date_emprunte = Label(self.PageEmprunt, text="Date d'emprunt ",font =("algarian", 15,"bold"), bg="#ff7f00", fg="black")
        self.date_emprunte.place(x=258, y=200)

        date_retour = Label(self.PageEmprunt, text="Date de eetour ",font =("algarian", 15,"bold"), bg="#ff7f00", fg="black")
        date_retour.place(x=258, y=250)
        


        #Dates
        self.txt_date_emprunte=DateEntry(self.PageEmprunt,font=("time new roman",15),bg="lightgray",textvariable=self.var_dateemprunt, date_pattern="yy/mm/dd")
        self.txt_date_emprunte.place(x=500, y=200, width=140)

        self.txt_date_retour=DateEntry(self.PageEmprunt,font=("time new roman",15),bg="lightgray", textvariable=self.var_dateretour,date_pattern="yy/mm/dd")#crée un objet DateEntry à l'intérieur de la fenêtre self.PageEmprunt. L'objet DateEntry est un widget de calendrier qui permet à l'utilisateur de sélectionner une date. Les options spécifiées pour le widget comprennent la police de caractère, la couleur de fond et le modèle de date. La variable self.var_dateretour est associée au widget pour stocker la date sélectionnée par l'utilisateur. La méthode place() est utilisée pour positionner le widget sur la fenêtre.
        self.txt_date_retour.place(x=500, y=250, width=140)
        #place le widget "txt_date_retour" sur la page de l'interface graphique à la position (200,250) avec une largeur de 140 pixels.

        #bouton
        BoutonSuivant = Button(self.PageEmprunt, command=self.ClickBoutonSuivant, text="Suivant",font=("times new roman", 20),cursor="hand2", bg="white").place(x=600, y=300, height=60, width=150)
        # crée un bouton "Suivant" sur la page d'emprunt. Lorsque l'utilisateur clique sur ce bouton, la méthode "ClickBoutonSuivant" est appelée. Le bouton est affiché avec une police de caractères "times new roman" de taille 20, un curseur de type "hand2" et une couleur de fond blanche. Les paramètres x et y déterminent la position du bouton sur la page, tandis que les paramètres height et width déterminent sa hauteur et sa largeur. La méthode place() est utilisée pour placer le bouton sur la page.

    

    #Fonction ClickBoutonSuivant qui va ajouter un emprunt dans la base de données
    def get_id_emprunteur(self, nom_emprunteur):

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
                
                id_emprunteur = None
                try:
                    self.execut.execute("SELECT idEmprunteur FROM Emprunteur WHERE nomEmprunteur = %s", (nom_emprunteur,))
                    row = self.execut.fetchone()
                    if row is not None:
                        id_emprunteur = row[0]
                except pymysql.Error as error:
                    print("Erreur de connexion: {}".format(error))
                return id_emprunteur
    

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
            
    
    
    def ClickBoutonSuivant(self):
            selected_livre = self.titreComboboxLivre.get()
            if selected_livre == "Selectionner un titre d'un livre":
                messagebox.showerror("Erreur", "Veuillez sélectionner un titre d'un livre", parent=self.PageEmprunt)
                return

            selected_nomAdherent = self.titreComboboxnomadherent.get()
            if selected_nomAdherent == "Selectionner un nomEmprunteur":
                messagebox.showerror("Erreur", "Veuillez sélectionner un nomEmprunteur", parent=self.PageEmprunt)
                return

            try:
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
                execut = connectionbdd.cursor()

                # Vérifier le nombre d'exemplaires disponibles pour le livre sélectionné
                execut.execute("SELECT nbrExemplaire FROM livre WHERE titreLivre=%s", selected_livre)
                result = execut.fetchone()

                if result is None or result[0] == 0:
                    messagebox.showerror("Erreur", "Tous les exemplaires de ce livre ont été empruntés", parent=self.PageEmprunt)
                    return

                # Vérifier si l'emprunteur a déjà emprunté un livre
                execut.execute("SELECT * FROM emprunt WHERE nomEmprunteur=%s", selected_nomAdherent)
                ligne = execut.fetchone()

                if ligne is not None:
                    messagebox.showerror("Erreur", "Cet emprunteur a déjà emprunté un livre", parent=self.PageEmprunt)
                    return

                # Insérer un nouvel enregistrement dans la table Emprunt
                id_emprunteur = self.get_id_emprunteur(selected_nomAdherent)
                id_livre = self.get_id_livre(selected_livre)
                execut.execute("INSERT INTO Emprunt (id, titreLivre, nomEmprunteur, dateEmprunt, dateRetour, idEmprunteur, idLivre) VALUES (null, %s, %s, %s, %s, %s, %s)", (
                    selected_livre,
                    selected_nomAdherent,
                    self.var_dateemprunt.get(),
                    self.var_dateretour.get(),
                    id_emprunteur,
                    id_livre
                ))

                execut.execute("UPDATE livre SET nbrExemplaire=nbrExemplaire-1 WHERE titreLivre=%s", selected_livre)


                messagebox.showinfo("Succes", "Votre livre à bien été emprunter", parent= self.PageEmprunt)#affiche une boîte de dialogue messagebox avec le message "Votre livre à bien été emprunter" et le titre "Succes". Elle est utilisée pour informer l'utilisateur que l'emprunt du livre a été effectué avec succès. La boîte de dialogue est liée à la fenêtre parent "self.PageEmprunt".
                 
                 
                
                 
                
                 
                 
                connectionbdd.commit() #La méthode commit() permet de valider les modifications apportées à la base de données.
                connectionbdd.close #connectionbdd.close() permet de fermer la connexion à la base de données. Cela permet de libérer les ressources utilisées par la connexion une fois que l'on a fini d'interagir avec la base de données.
            except Exception as es :#création d'une variable 'es' pour stocker l'erreur levée, utilisée généralement pour afficher des messages d'erreur détaillés aux utilisateurs en cas d'échec de l'exécution du bloc de code.
                messagebox.showerror("erreur",f"Erreur de connexionnnn{str(es)}",parent=self.PageEmprunt)
                #Affichage d'une boîte de dialogue d'erreur dans Tkinter à l'aide de la méthode 'showerror' de la classe messagebox pour informer l'utilisateur d'une erreur de connexion, en utilisant le contenu de la variable 'es' qui contient une description détaillée de l'erreur levée. Le paramètre 'parent' est utilisé pour spécifier la fenêtre parent de la boîte de dialogue.
        
        

    

root =Tk()#root = Tk() crée une instance de la classe Tk(). Cette classe fait partie du module tkinter de Python,
obj = gestionprets(root)
#crée un objet de la classe "gestionprets" en utilisant le constructeur de cette classe. L'objet créé est stocké dans une variable appelée "obj".
root.mainloop() #afficher la fenêtre Tkinter à l'aide de la méthode mainloop().
