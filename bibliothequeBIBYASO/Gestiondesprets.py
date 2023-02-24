from tkinter import * #importer la bibliotheque tkinte
import tkinter as tk  #
from tkinter import ttk, messagebox #bibliotheque pour afficher nos message d'erreur dans l'application
from turtle import bgcolor, title #permetre de gerer les selections et les message derreur  afficher ou de securite
from tkcalendar import * #Bibliothéque pour importer les calendrier 
import pymysql #bibliotheque pour interagir avec la base de données
#import os #faire des actions diretement au niveau du systeme  
from subprocess import call   #bibliotheque pour pouvoir changer de page  


                    
class gestionprets:  # classe gestionprets
    def __init__(self,root):  #constructeur                  
        self.PageGestiondesprets = root #changer
        self.PageGestiondesprets.title("Gestionprets") #titre de la fenetre 
        self.PageGestiondesprets.geometry("1040x560+400+200")#pour gerer la taille de l'application
        
        self.PageGestiondesprets.resizable(width=False, height=False)#Pour eviter d'agrandir notre application
        self.PageGestiondesprets.iconbitmap("Images/bib.ico")  #pour gerer l'icone de notre application
       
        
        self.idEmprunt = StringVar() 
        self.var_dateemprunt = StringVar()  # on declare des variables pour ensuite les recuperer
        self.var_iddelhadherent = StringVar()  # Mémorise une chaîne de caractères; sa valeur par défaut est ''
        self.var_idlivre = StringVar()
        self.var_dateretour = StringVar()
        self.recherche_par = StringVar()
        self.recherche = StringVar()
        self.nomdelhadherent_list=[]
        self.livre=[]
        self.Recuperelenomdeladhereneetletitredulivre()

        
        


        self.Paneauvertdegestionlivres = Frame(self.PageGestiondesprets, bg="#bedb0d")
        self.Paneauvertdegestionlivres.place(x=190, y=0, width=1100, height=1000)

        Paneauorangedegestionlivres = Frame(self.PageGestiondesprets, bg="#ff7f00")
        Paneauorangedegestionlivres.place(x=0, y=0, width=190, height=1000)


        self.ImageGestionlivres = PhotoImage(file="Images/Gestionlivre.png")
        self.BoutonPourAllerVersGestionLivres = Button(self.PageGestiondesprets,command=self.VersGestionLivres, text="",image=self.ImageGestionlivres, width=184,height=90, bg="#ff7f00",font="arial 12 bold")
        self.BoutonPourAllerVersGestionLivres.place(x=0 , y=0) 
        
        self.ImageAdherents = PhotoImage(file="Images/Adherents.png")
        self.BoutonPourAllerVersAdherents = Button(self.PageGestiondesprets,command=self.VersAdherents, text="",image=self.ImageAdherents, width=184, height=90, bg="#ff7f00",font="arial 12 bold")
        self.BoutonPourAllerVersAdherents.place(x=0 , y=140) 

        self.ImageGestionDesprets = PhotoImage(file="Images/Emprunter.png")
        self.BoutonPourAllerVersGestionDesprets = Button(self.PageGestiondesprets, text="",image=self.ImageGestionDesprets, width=184, height=90, bg="#ff7f00",font="arial 12 bold")
        self.BoutonPourAllerVersGestionDesprets.place(x=0 , y=280) 

        
        self.ImageSedeconnecter = PhotoImage(file="Images/Sedeconnecter.png")
        self.BoutonPourSedeconnecter = Button(self.PageGestiondesprets, text="",command=self.PourSeDeConnecter,image=self.ImageSedeconnecter, width=184, height=90, bg="#ff7f00",font="arial 12 bold")
        self.BoutonPourSedeconnecter.place(x=0 , y=420) 

        

        #titres
        titreGestionprets = Label(self.PageGestiondesprets, text=" Gestion Prêts ",font =("algarian", 20,"bold"), bg="#bedb0d", fg="black")
        titreGestionprets.place(x=350, y=20,width=500)
        
        titreGestionlivres = Label(self.PageGestiondesprets, text=" Livres ",font =("algarian", 15,"bold"), bg="#ff7f00", fg="black")
        titreGestionlivres.place(x=0, y=100,width=190)

        titreAdherents = Label(self.PageGestiondesprets, text=" Adhérents ",font =("algarian", 15,"bold"), bg="#ff7f00", fg="black")
        titreAdherents.place(x=0, y=240,width=190)

        titreGestiondesprets = Label(self.PageGestiondesprets, text=" Prêts",font =("algarian", 15,"bold"), bg="#ff7f00", fg="black")
        titreGestiondesprets.place(x=0, y=380,width=190)

        titreSedeconnecter = Label(self.PageGestiondesprets, text=" Se déconnecter",font =("algarian", 15,"bold"), bg="#ff7f00", fg="black")
        titreSedeconnecter.place(x=0, y=520,width=190)

        titreRechercherlesemprunts= Label(self.PageGestiondesprets, text=" Rechercher les emprunts par :",font =("algarian", 12,"bold"), bg="#bedb0d", fg="black")
        titreRechercherlesemprunts.place(x=210, y=90,width=250)

        

        Question = ttk.Combobox(self.PageGestiondesprets,textvariable=self.recherche_par, font=("times new roman", 15), state="readonly")
        Question["values"]=("idEmprunt", "idAdherent") # on recupere le soit l'idEmprunt ou soit le numAdheren
        Question.place(x=455, y=87, width=110) #.place pour la position du ttk.combobox 
        Question.current(0)


        


        self.ChampsDesaisiePourRechercherDeslivres= Entry(self.PageGestiondesprets,textvariable=self.recherche ,font= (5), bg="white")
        self.ChampsDesaisiePourRechercherDeslivres.place(x=570, y=90,width=150)

        BoutonPourRechercherUnEmprunt = Button(self.PageGestiondesprets,command=self.ClickBoutonRechercher, text="Rechercher  ",cursor="hand2", font=("times new roman",11), bd=0,bg="white",fg="black")
        BoutonPourRechercherUnEmprunt.place(x=730, y=90) # command est attribuer a un bouton pour pouvoir l'executer  

        BoutonActualiser = Button(self.PageGestiondesprets,command=self.ClickActualiser, text="Actualiser ",cursor="hand2", font=("times new roman",11), bd=0,bg="white",fg="black")
        BoutonActualiser.place(x=820, y=90) # command est attribuer a un bouton pour pouvoir l'executer  

        BoutonPourAjouterUnlivre = Button(self.PageGestiondesprets,command=self.PageEmprunt, text="Cliquer pour emprunter un livre",cursor="hand2", font=("times new roman",11), bd=0,bg="white",fg="black", )
        BoutonPourAjouterUnlivre.place(x=215, y=500)

        
        BoutonRetournerUnLivre = Button(self.PageGestiondesprets,command=self.RestituerUnEmprunt, text="Restituer un emprunt",cursor="hand2", font=("times new roman",11), bd=0,bg="white",fg="black")
        BoutonRetournerUnLivre.place(x=890, y=500) 
        # cursor pour mettre la main quand on clique sur le bouton 
       

       
        

        CadreDuTableauGestiondesprets = Frame(self.PageGestiondesprets, bd=5,relief=GROOVE,bg="white") #self.root pour mettre le table sur cette frame la 
        CadreDuTableauGestiondesprets.place(x=215, y=130,width=800, height=350)

        barrededefilementX = Scrollbar(CadreDuTableauGestiondesprets,orient=HORIZONTAL)
        barrededefilementY = Scrollbar(CadreDuTableauGestiondesprets, orient=VERTICAL)
        
        self.tableauGestiondesprets = ttk.Treeview(CadreDuTableauGestiondesprets,columns=("idemprunt", "idadherent", "idlivre","dateemprunt","dateretour"),xscrollcommand=barrededefilementX.set, yscrollcommand=barrededefilementY.set)
        barrededefilementX.pack(side=BOTTOM, fill=X)
        barrededefilementY.pack(side=RIGHT, fill=Y) 

        self.tableauGestiondesprets.heading("idemprunt", text="idEmprunt")
        self.tableauGestiondesprets.heading("idadherent", text="idAdherent")
        self.tableauGestiondesprets.heading("idlivre", text="idLivre")
     
        self.tableauGestiondesprets.heading("dateemprunt", text="dateEmprunt")
        self.tableauGestiondesprets.heading("dateretour", text="dateRetour")
        
        self.tableauGestiondesprets["show"]="headings"

        self.tableauGestiondesprets.column("idemprunt",  width=80)
        self.tableauGestiondesprets.column("idadherent", width=80)
        self.tableauGestiondesprets.column("idlivre", width=80)
        self.tableauGestiondesprets.column("idlivre", width=80)
        self.tableauGestiondesprets.column("dateemprunt", width=80)
        self.tableauGestiondesprets.column("dateretour", width=80)
        

        self.tableauGestiondesprets.pack(fill=BOTH, expand=1)  # La première ligne de code, "self.tableauGestiondesprets.pack(fill=BOTH, expand=1)", configure un widget d'interface utilisateur appelé "tableauGestiondesprets" pour qu'il prenne autant de place que possible dans la fenêtre principale de l'application.
        self.tableauGestiondesprets.bind("<ButtonRelease-1>",self.information)
        self.ClickActualiser()

    

    def ClickActualiser(self):
        con= pymysql.connect(host="localhost", user="root", password="", database="bddcomptes") #
        cur=con.cursor()
        cur.execute("select  * from emprunter ") #ligne sql pour récuperer la table ajoutlivres
        rows= cur.fetchall()
        if len(rows)!=0:
            self.tableauGestiondesprets.delete(*self.tableauGestiondesprets.get_children())
            for row in rows:
                self.tableauGestiondesprets.insert("", END, values=row)
        con.commit()
        con.close()
    
    def ClickBoutonRechercher(self):
        connectionbdd= pymysql.connect(host="localhost", user="root", password="", database="bddcomptes") # connexion a la base de donnes
        execut=connectionbdd.cursor()        
        execut.execute("select * from emprunter where "+str(self.recherche_par.get())+" LIKE '%"+str(self.recherche.get())+"%'")
        lignes = execut.fetchall()
        if len(lignes)!=0:  # Vérifie si la liste "lignes" n'est pas vide
           self.tableauGestiondesprets.delete(*self.tableauGestiondesprets.get_children())
           for ligne in lignes: # Pour chaque élément "ligne" de la liste "lignes"
            self.tableauGestiondesprets.insert('', END, values=ligne)
        connectionbdd.commit()
        connectionbdd.close() #ferme la connexion à la base de données




    def RestituerUnEmprunt(self): # fonction supprimerlivre qui prendra pour parametre self

        if self.idEmprunt.get()=="":
         messagebox.showerror("Erreur", "Veuillez, sélectionner un emprunt", parent=self.PageGestiondesprets) #si tout les champs ne sont pas rempli alors affiche un message box pour dire que les champs ne sont pas rempli        
        
        else:
            connectionbdd= pymysql.connect(host="localhost", user="root", password="", database="bddcomptes") # connexion a la base de donnes 
            execut=connectionbdd.cursor()
            execut.execute("delete from emprunter where idEmprunt = %s", self.idEmprunt.get()) #supprimer la ligne 
            execut.execute(" update livre set etatLivre = 'Disponible' where idLivre=%s",self.var_idlivre.get()),

            
            connectionbdd.commit()
            messagebox.showinfo("Succes", "L'emprunt à bien était restituer, Merci", parent=self.PageGestiondesprets)  
            self.ClickActualiser()
            connectionbdd.close()
        

    def information(self,ev):  # on recupere les informations pour ensuite les modifier ou supprimer, ev est un moyen pour la méthode "information" d'obtenir des informations
        cursor_row = self.tableauGestiondesprets.focus() # Récupère la ligne actuellement sélectionnée dans le widget "tableauGestiondesprets"
        contents = self.tableauGestiondesprets.item(cursor_row) # Récupère les données de la ligne sélectionnée
        ligne = contents["values"] # Extrait les valeurs de la ligne sélectionnée et les stocke dans la variable "ligne"
        
        self.idEmprunt.set(ligne[0])   # Met à jour la variable "idEmprunt" avec la première valeur de la ligne sélectionnée
        self.var_iddelhadherent.set(ligne[1]),   # Met à jour la variable "var_iddelhadherent" avec la deuxième valeur de la ligne sélectionnée
        
        self.var_idlivre.set(ligne[2]), # Met à jour la variable "var_idlivre" avec la troisième valeur de la ligne sélectionnée
        self.var_dateemprunt.set(ligne[3]) # Met à jour la variable "var_dateemprunt" avec la quatrième valeur de la ligne sélectionnée
        self.var_dateretour.set(ligne[4]), # Met à jour la variable "var_dateretour" avec la cinquième valeur de la ligne sélectionnée
        

    def PourSeDeConnecter(self):
        messagePoursedeconnecter = messagebox.askyesno("Déconnexion","Voulez-vous vous déconnecter", parent=self.PageGestiondesprets)
        if messagePoursedeconnecter == YES:
         self.PageGestiondesprets.destroy()
         call(["python", "Connexion.py"])

         
    def VersGestionLivres(self):
        self.PageGestiondesprets.destroy()
        call(["python", "Gestionlivres.py"]) 
        
    def VersAdherents(self):
        self.PageGestiondesprets.destroy()
        call(["python", "Adherents.py"])
       


    
    def Recuperelenomdeladhereneetletitredulivre(self):  #recuperer les nom et livres dispo dans la base de donnes 
            self.nomdelhadherent_list.append("Vide")
            self.livre.append("Vide")
            con= pymysql.connect(host="localhost", user="root", password="", database="bddcomptes")
            cur=con.cursor()
            try:
                cur.execute("select idAdherent from adherent")
                nomdelhadherent=cur.fetchall()
                if len(nomdelhadherent)>0:
                    del self.nomdelhadherent_list[:]
                    self.nomdelhadherent_list.append("Selectionner un idAdhérent") #on appel la liste de nos adherents
                    for i in nomdelhadherent:
                        self.nomdelhadherent_list.append(i[0])

                cur.execute("select idLivre from livre") #on appel la liste de nos livres
                four=cur.fetchall()
                if len(four)>0:
                    del self.livre[:]
                    self.livre.append("Selectionner un idlivre")
                    for i in four:
                        self.livre.append(i[0])
                
            except Exception as ex:
                messagebox.showerror("Erreur", f"Erreur de connexion {str(ex)}")

    


    #Fonction de la Page pour les emprunt
    def PageEmprunt(self):          
        self.PageEmprunt= Toplevel() # top level fenetre fille a la fenetre mere 
        self.PageEmprunt.title("Emprunter un livre") # titre de la frame
        self.PageEmprunt.config(bg="#ff6600")  # background de la frame 
        self.PageEmprunt.geometry("1056x560+400+200") # la taille de la frame
        
        self.PageEmprunt.grab_set() # si on lance une fenetre on poura pas cliquer ailleurs 
        self.PageEmprunt.resizable(width=False, height=False) #eviter d'agrandir la fenetre
        self.PageEmprunt.iconbitmap("Images/bib.ico") 

        
        

        
        #liste pour recuperer les adherent
        titreComboboxAdherent = ttk.Combobox(self.PageEmprunt,values=self.nomdelhadherent_list,   textvariable=self.var_iddelhadherent,font=("goudy old style",20), state="readonly", justify=CENTER)
        titreComboboxAdherent.place(x=200, y=50, width=300)
        titreComboboxAdherent.current(0)

        
        #liste pour recuperer les livres
        titreComboboxLivre = ttk.Combobox(self.PageEmprunt,values= self.livre, textvariable=self.var_idlivre,font=("goudy old style",20), state="readonly", justify=CENTER)
        titreComboboxLivre.place(x=200, y=100, width=270)
        titreComboboxLivre.current(0)

        
 
        #titres
        titrenom = Label(self.PageEmprunt, text=" idAdherent ",font =("algarian", 15,"bold"), bg="#ff6600", fg="black")
        titrenom.place(x=6, y=50)

        titrelivre = Label(self.PageEmprunt, text=" idLivre ",font =("algarian", 15,"bold"), bg="#ff6600", fg="black")
        titrelivre.place(x=10, y=100)

        self.date_emprunte = Label(self.PageEmprunt, text="dateEmprunt ",font =("algarian", 15,"bold"), bg="#ff6600", fg="black")
        self.date_emprunte.place(x=10, y=200)

        date_retour = Label(self.PageEmprunt, text="dateRetour ",font =("algarian", 15,"bold"), bg="#ff6600", fg="black")
        date_retour.place(x=10, y=250)
        


        #Dates
        self.txt_date_emprunte=DateEntry(self.PageEmprunt,font=("time new roman",15),bg="lightgray",textvariable=self.var_dateemprunt, date_pattern="dd/mm/yy")
        self.txt_date_emprunte.place(x=200, y=200, width=140)

        self.txt_date_retour=DateEntry(self.PageEmprunt,font=("time new roman",15),bg="lightgray", textvariable=self.var_dateretour,date_pattern="dd/mm/yy")
        self.txt_date_retour.place(x=200, y=250, width=140)

        #bouton
        BoutonSuivant = Button(self.PageEmprunt, command=self.ClickBoutonSuivant, text="Suivant",font=("times new roman", 20),cursor="hand2", bg="white").place(x=10, y=300, height=60, width=150)
        
        
    
    #Fonction ClickBoutonSuivant qui va ajouter un emprunt dans la base de données
    def ClickBoutonSuivant(self):
        
        if self.var_iddelhadherent.get=="" or self.var_idlivre.get=="" : #si aucun adherent n'a pas été sélectionnez afficher un message d'erreur pour demander a l'utilisateur de sélectionnez un adhérent

            messagebox.showerror("Erreur", "Veuillez sélectionner un idadhérent, un idlivre, une date d'emprunt, une date de retour", parent=self.PageEmprunt)
        
        try:
                connectionbdd= pymysql.connect(host="localhost", user="root", password="", database="bddcomptes")

                execut=connectionbdd.cursor()
                execut.execute("select * from emprunter where idAdherent=%s",self.var_iddelhadherent.get())
                ligne= execut.fetchone()

                if ligne != None:

                   messagebox.showerror("Erreur", "Cet adhérent à déja emprunter un livre", parent=self.PageEmprunt)

                elif execut.execute("select * from emprunter where idLivre=%s",self.var_idlivre.get()):

                  messagebox.showerror("Erreur", "Ce livre à déja été emprunter, il faut choisir un autre livre", parent=self.PageEmprunt)
                
                else:
                
                 execut.execute("insert into emprunter (idAdherent,idLivre,dateEmprunt,dateRetour) values (%s,%s,%s,%s)",
                   
                   (
                       
                       self.var_iddelhadherent.get(),
                       self.var_idlivre.get(),
                      
                       self.var_dateemprunt.get(),
                       self.var_dateretour.get(),
                       
                    ))

                 execut.execute(" update livre set etatLivre = 'Emprunter' where idLivre=%s",self.var_idlivre.get()),

                 messagebox.showinfo("Succes", "Votre livre à bien été emprunter", parent= self.PageEmprunt)
                   
                 connectionbdd.commit()
                 connectionbdd.close
        except Exception as es :
                messagebox.showerror("erreur",f"Erreur de connexionnnn{str(es)}",parent=self.PageEmprunt)

    

root =Tk()
obj = gestionprets(root)
root.mainloop() #methode pour afficher notre fenetre
