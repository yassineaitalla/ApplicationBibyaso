from ast import excepthandler
from cProfile import label
from email.mime import image
from logging import root            # pour importer la bibliotheque tkinter
from re import L
from tkinter import * 
from subprocess import call

 


from tkinter import ttk, messagebox
from turtle import bgcolor, title #permetre de gerer les selcetions et les message derrueeur  afficher ou de securite
  
import pymysql 
      
                    
class Emprunteur:  #classe formulaire:
    def __init__(self,root):                   
        self.PageEmprunteur = root
        self.PageEmprunteur.title("Emprunteur")
        self.PageEmprunteur.geometry("1040x560+400+200")
        self.PageEmprunteur.resizable(width=False, height=False)
        self.PageEmprunteur.iconbitmap("bibliothequeBIBYASO/Images/bib.ico") 
        
        self.idEmprunteur = StringVar()
        self.nom = StringVar()
        self.prenom = StringVar()
        self.codepostal= StringVar()
        self.ville = StringVar()
        self.recherche_par = StringVar()
        self.recherche = StringVar()


        self.Paneauvertdegestionlivres = Frame(self.PageEmprunteur, bg="#bedb0d")
        self.Paneauvertdegestionlivres.place(x=190, y=0, width=1100, height=1000)

        Paneauorangedegestionlivres = Frame(self.PageEmprunteur, bg="#ff7f00")
        Paneauorangedegestionlivres.place(x=0, y=0, width=190, height=1000)

        self.ImageGestionlivres = PhotoImage(file="bibliothequeBIBYASO/Images/Gestionlivre.png")
        self.BoutonGestionLivres = Button(self.PageEmprunteur,cursor="hand2", command=self.VersGestionsLivres,text="",image=self.ImageGestionlivres, width=184,height=90, bg="#ff7f00",font="arial 12 bold")
        self.BoutonGestionLivres.place(x=0 , y=0) 
        
        self.ImageEmprunteur = PhotoImage(file="bibliothequeBIBYASO/Images/Emprunteur.png")
        self.BoutonImageAdherent = Button(self.PageEmprunteur, text="",cursor="hand2",image=self.ImageEmprunteur, width=184, height=90, bg="#ff7f00",font="arial 12 bold")
        self.BoutonImageAdherent.place(x=0 , y=140) 

        self.ImageGestionDesPrets = PhotoImage(file="bibliothequeBIBYASO/Images/Emprunter.png") 
        self.BoutonImageGestionDesPrets = Button(self.PageEmprunteur,cursor="hand2", command=self.VersGestionsdesPrets,text="",image=self.ImageGestionDesPrets, width=184, height=90, bg="#ff7f00",font="arial 12 bold")
        self.BoutonImageGestionDesPrets.place(x=0 , y=280) 

        self.ImageSedeconnecter = PhotoImage(file="bibliothequeBIBYASO/Images/Sedeconnecter.png")
        self.BoutonImageSedeconnecter = Button(self.PageEmprunteur,cursor="hand2", text="",command=self.PourSeDeconnecter,image=self.ImageSedeconnecter, width=184, height=90, bg="#ff7f00",font="arial 12 bold")
        self.BoutonImageSedeconnecter.place(x=0 , y=420)

        # command  ------> Réecuperer la fontion qu'oncrée
         

        #Titres
        titreGestionEmprunteurDeLaPageEmprunteur = Label(self.PageEmprunteur, text=" Gestion Emprunteur ",font =("algarian", 20,"bold"), bg="#bedb0d", fg="black")
        titreGestionEmprunteurDeLaPageEmprunteur.place(x=350, y=20,width=500)
        
        titreGestionlivres = Label(self.PageEmprunteur, text=" Livres ",font =("algarian", 15,"bold"), bg="#ff7f00", fg="black")
        titreGestionlivres.place(x=0, y=100,width=190)

        titreGestionEmprunteurDeLaPageEmprunteur = Label(self.PageEmprunteur, text=" Emprunteur ",font =("algarian", 15,"bold"), bg="#ff7f00", fg="black")
        titreGestionEmprunteurDeLaPageEmprunteur.place(x=0, y=240,width=190)

        titreGestionDesPretsDeLaPageEmprunteur = Label(self.PageEmprunteur, text=" Prêts",font =("algarian", 15,"bold"), bg="#ff7f00", fg="black")
        titreGestionDesPretsDeLaPageEmprunteur.place(x=0, y=380,width=190)

        titreSedeconnecterDeLaPageEmprunteur = Label(self.PageEmprunteur, text=" Se déconnecter",font =("algarian", 15,"bold"), bg="#ff7f00", fg="black")
        titreSedeconnecterDeLaPageEmprunteur.place(x=0, y=520,width=190)

        titreRechercherlesEmprunteurpar = Label(self.PageEmprunteur, text=" Rechercher les emprunteur par :",font =("algarian", 12,"bold"), bg="#bedb0d", fg="black")
        titreRechercherlesEmprunteurpar.place(x=205, y=90,width=250)

        #Boutons
        BoutonAjouterunEmprunteurDeLaPageEmprunteur = Button(self.PageEmprunteur, text="Ajouter un emprunteur",command=self.AllerVersLaPagePourAjouterdesEmprunteur,cursor="hand2", font=("times new roman",11), bd=0,bg="white",fg="black")
        BoutonAjouterunEmprunteurDeLaPageEmprunteur.place(x=215, y=500)

        BoutonSupprimerEmprunteurDeLaPageEmprunteur = Button(self.PageEmprunteur, command=self.SupprimerunAdherent,text="Supprimer un emprunteur",cursor="hand2", font=("times new roman",11), bd=0,bg="white",fg="black")
        BoutonSupprimerEmprunteurDeLaPageEmprunteur.place(x=865, y=500)

        BoutonPourRechercherUnLivre = Button(self.PageEmprunteur,command=self.ClickBoutonRechercher, text=" Rechercher  ",cursor="hand2", font=("times new roman",11), bd=0,bg="white",fg="black")
        BoutonPourRechercherUnLivre.place(x=730, y=90) # command est attribuer a un bouton pour pouvoir l'executer

        BoutonActualiser = Button(self.PageEmprunteur,command=self.ClickBoutonActualiser, text="Actualiser ",cursor="hand2", font=("times new roman",11), bd=0,bg="white",fg="black")
        BoutonActualiser.place(x=830, y=90) # command est attribuer a un bouton pour pouvoir l'executer  

        #Champs de saisie
        self.ChampsDesaisiePourRechercherDesEmprunteur= Entry(self.PageEmprunteur,textvariable=self.recherche ,font= (5), bg="white")
        self.ChampsDesaisiePourRechercherDesEmprunteur.place(x=570, y=90,width=150)

        
        ListeEmprunteur = ttk.Combobox(self.PageEmprunteur,textvariable=self.recherche_par, font=("times new roman", 15), state="readonly")
        ListeEmprunteur["values"]=( "nomEmprunteur") # on recupere le soit l'idEmprunt ou soit le numAdheren
        ListeEmprunteur.place(x=455, y=87, width=110) #.place pour la position du ttk.combobox 
        ListeEmprunteur.current(0)



        #Cadre

        CadretableauGestionEmprunteur = Frame(self.PageEmprunteur, bd=5,relief=GROOVE,bg="white")
        CadretableauGestionEmprunteur.place(x=215, y=130,width=800, height=350)

        barededefilementX = Scrollbar(CadretableauGestionEmprunteur,orient=HORIZONTAL)
        barededefilemenyY = Scrollbar(CadretableauGestionEmprunteur, orient=VERTICAL)
        
        self.tableauGestionEmprunteur = ttk.Treeview(CadretableauGestionEmprunteur,columns=("nomemprunteur", "prenomemprunteur", "codepostalemprunteur","villeemprunteur"),xscrollcommand=barededefilementX.set, yscrollcommand=barededefilemenyY.set)
        barededefilementX.pack(side=BOTTOM, fill=X)
        barededefilemenyY.pack(side=RIGHT, fill=Y) 
        self.tableauGestionEmprunteur.selection
        

        self.tableauGestionEmprunteur.heading("nomemprunteur", text="nomEmprunteur")
        self.tableauGestionEmprunteur.heading("prenomemprunteur", text="prenomEmprunteur")
        
        self.tableauGestionEmprunteur.heading("codepostalemprunteur", text="codepostalEmprunteur")
        self.tableauGestionEmprunteur.heading("villeemprunteur", text="villeEmprunteur")

        self.tableauGestionEmprunteur["show"]="headings"

      
        self.tableauGestionEmprunteur.column("nomemprunteur",width=80)
        self.tableauGestionEmprunteur.column("prenomemprunteur",width=80)
        self.tableauGestionEmprunteur.column("codepostalemprunteur",width=80)
        self.tableauGestionEmprunteur.column("villeemprunteur", width=80)

        self.tableauGestionEmprunteur.pack(side=TOP, fill=X,)
        self.tableauGestionEmprunteur.pack(fill=BOTH, expand=1)
        
        
        self.tableauGestionEmprunteur.bind("<ButtonRelease-1>",self.information) # le self information est important si on souhaite faire la meme vhose ailleurs
        self.ClickBoutonActualiser()
    
    def AllerVersLaPagePourAjouterdesEmprunteur(self):
        self.PageEmprunteur.destroy()
        call(["python", "bibliothequeBIBYASO/ajouterdesEmprunteur.py"]) 
    
    
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
        execut.execute("select nomEmprunteur,prenomEmprunteur,codepostalEmprunteur,villeEmprunteur from Emprunteur  where "+str(self.recherche_par.get())+" LIKE '%"+str(self.recherche.get())+"%'")
        ligne = execut.fetchall()
        if len(ligne)!=0:
           self.tableauGestionEmprunteur.delete(*self.tableauGestionEmprunteur.get_children())
           for row in ligne:
            self.tableauGestionEmprunteur.insert('', END, values=row)
        connectionbdd.commit()
        connectionbdd.close()

        

    def VersGestionsLivres(self):
        self.PageEmprunteur.destroy()
        call(["python", "bibliothequeBIBYASO/Gestionlivres.py"]) 

    
    def VersGestionsdesPrets(self):
        self.PageEmprunteur.destroy()
        call(["python", "bibliothequeBIBYASO/GestionDesprets.py"]) 

    
    def PourSeDeconnecter(self):
        
        lemessagebox = messagebox.askyesno("Déconnexion","Voulez-vous vous déconnecter", parent=self.PageEmprunteur)
        if lemessagebox == YES:
         self.PageEmprunteur.destroy()                           
         call(["python", "bibliothequeBIBYASO/Connexion.py"])
        
        
      

    def information(self,ev):
        cursor_row = self.tableauGestionEmprunteur.focus()
        contents = self.tableauGestionEmprunteur.item(cursor_row)
        row = contents["values"]
        
    
        self.nom.set(row[0]),
        self.prenom.set(row[1]),
        self.codepostal.set(row[2]),
        self.ville.set(row[3]),
    
    def ClickBoutonActualiser(self):
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
        
        execut=connectionbdd.cursor() #Cursor permet d'éxecuter une operation SQL   
        execut.execute("SELECT nomEmprunteur ,prenomEmprunteur ,codepostalEmprunteur ,villeEmprunteur FROM emprunteur") #requette sql pour récuperer les adherents
        
        ligne= execut.fetchall() #fetchall récupère toutes les lignes d'un résultat de requête
        if len(ligne)!=0:
            self.tableauGestionEmprunteur.delete(*self.tableauGestionEmprunteur.get_children())
            for ligne in ligne:
                self.tableauGestionEmprunteur.insert("", END, values=ligne)
                
        connectionbdd.commit() #valide la transaction
        connectionbdd.close() #ferme la connexion a la bdd



        
    def SupprimerunAdherent(self):

        if self.nom.get()=="":
            messagebox.showerror("Erreur", "Veuillez, sélectionner un emprunteur", parent=self.PageEmprunteur)
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
            execut = connectionbdd.cursor()

            # Vérifier si l'emprunteur a des livres en cours d'emprunt
            execut.execute("SELECT COUNT(*) FROM emprunt WHERE nomEmprunteur = %s", self.nom.get())
            count = execut.fetchone()[0]

            if count > 0:
                messagebox.showerror("Erreur", "Impossible de supprimer l'emprunteur. Des emprunts sont en cours pour cet emprunteur. Veuillez supprimer les emprunts avant de supprimer l'emprunteur.", parent=self.PageEmprunteur)
            else:
                # Supprimer l'emprunteur s'il n'a aucun livre en cours d'emprunt
                execut.execute("DELETE FROM emprunteur WHERE nomEmprunteur = %s", self.nom.get())
                connectionbdd.commit()
                messagebox.showinfo("Succés", "L'emprunteur a bien été supprimé", parent=self.PageEmprunteur)
                self.ClickBoutonActualiser()
                connectionbdd.close()

          

root = Tk()
obj = Emprunteur(root)
root.mainloop() #root est la fenetre racine