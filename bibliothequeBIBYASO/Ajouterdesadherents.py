from tkinter import * # pour importer la bibliotheque tkinter
from ast import Delete, excepthandler 
from cProfile import label
from email.mime import image
from logging import root
from re import L 
from subprocess import call 
from tkinter import ttk, messagebox #permet d'afficher les message d'erreur qu'on appel les messages box
from turtle import bgcolor, title
#from tkcalendar import *
import pymysql  
 

class AjouterDesadherents:  # classe ajouter des adherents
    def __init__(self,root):                   
        self.PageAjouterDesAdherents = root
        self.PageAjouterDesAdherents.title("Ajouter un Adhérent")
        self.PageAjouterDesAdherents.geometry("1040x560+400+200")
        self.PageAjouterDesAdherents.resizable(width=False, height=False)
        self.PageAjouterDesAdherents.iconbitmap("Images/bib.ico")       
        


        self.nomAdherent = StringVar()
        self.prenomAdherent = StringVar()
        self.codepostalAdherent = StringVar()
        self.villeAdherent = StringVar()
        


        self.Paneauvertdegestionlivres = Frame(self.PageAjouterDesAdherents, bg="#bedb0d")
        self.Paneauvertdegestionlivres.place(x=190, y=0, width=1100, height=1000)

        Paneauorangedegestionlivres = Frame(self.PageAjouterDesAdherents, bg="#ff7f00")
        Paneauorangedegestionlivres.place(x=0, y=0, width=190, height=1000)

        self.ImageGestionlivres = PhotoImage(file="Images/Gestionlivre.png")
        self.BoutonImageGestionlivres = Button(self.PageAjouterDesAdherents,cursor="hand2",command=self.Versgestionlivres, text="",image=self.ImageGestionlivres, width=184,height=90, bg="#ff7f00",font="arial 12 bold")
        self.BoutonImageGestionlivres.place(x=0 , y=0) 
        
        self.ImageAdherents = PhotoImage(file="Images/Adherents.png")
        self.BoutonImageAdherents = Button(self.PageAjouterDesAdherents,cursor="hand2",command=self.VersPageAdherents, text="",image=self.ImageAdherents, width=184, height=90, bg="#ff7f00",font="arial 12 bold")
        self.BoutonImageAdherents.place(x=0 , y=140) 

        self.ImageGestiondesprets = PhotoImage(file="Images/Emprunter.png")
        self.BoutonImageGestiondesprets = Button(self.PageAjouterDesAdherents,cursor="hand2",command=self.Versgestiondesprets, text="",image=self.ImageGestiondesprets, width=184, height=90, bg="#ff7f00",font="arial 12 bold")
        self.BoutonImageGestiondesprets.place(x=0 , y=280) 

        self.ImageSedeconnecter = PhotoImage(file="Images/Sedeconnecter.png")
        self.BoutonImageSedeconnecter = Button(self.PageAjouterDesAdherents,cursor="hand2",command=self.PourSedeconnecter, text="",image=self.ImageSedeconnecter, width=184, height=90, bg="#ff7f00",font="arial 12 bold")
        self.BoutonImageSedeconnecter.place(x=0 , y=420)

        titresgestionlivretitre = Label(self.PageAjouterDesAdherents, text=" Ajout d'adhérents ",font =("algarian", 20,"bold"), bg="#bedb0d", fg="black")
        titresgestionlivretitre.place(x=350, y=20,width=500)

        titresgestionlivres = Label(self.PageAjouterDesAdherents, text=" Livres ",font =("algarian", 15,"bold"), bg="#ff7f00", fg="black")
        titresgestionlivres.place(x=0, y=100,width=190)

        titresadherents = Label(self.PageAjouterDesAdherents, text="Adhérents",font =("algarian", 15,"bold"), bg="#ff7f00", fg="black")
        titresadherents.place(x=0, y=240,width=190)

        titresgestionprets = Label(self.PageAjouterDesAdherents, text=" Prêts",font =("algarian", 15,"bold"), bg="#ff7f00", fg="black")
        titresgestionprets.place(x=0, y=380,width=190)

        titressedeconnecter = Label(self.PageAjouterDesAdherents, text=" Se déconnecter",font =("algarian", 15,"bold"), bg="#ff7f00", fg="black")
        titressedeconnecter.place(x=0, y=520,width=190) 

        

        #label pour ajouter un livre 

        titrenom = Label(self.PageAjouterDesAdherents, text=" Nom ",font =("algarian", 12,"bold"), bg="#bedb0d", fg="black")
        titrenom.place(x=300, y=150,width=100)

        titreauteurs = Label(self.PageAjouterDesAdherents, text=" Prénom ",font =("algarian", 12,"bold"), bg="#bedb0d", fg="black")
        titreauteurs.place(x=310, y=200,width=100)

        titrecodepostal = Label(self.PageAjouterDesAdherents, text=" Code postal ",font =("algarian", 12,"bold"), bg="#bedb0d", fg="black")
        titrecodepostal.place(x=323, y=240,width=100)

        titreville= Label(self.PageAjouterDesAdherents, text=" Ville ",font =("algarian", 12,"bold"), bg="#bedb0d", fg="black")
        titreville.place(x=300, y=285,width=100)

      

        
        
        
        
        #Champs de saisie
        
        nomAdherent= Entry(self.PageAjouterDesAdherents,textvariable=self.nomAdherent, font= (5), bg="white")
        nomAdherent.place(x=500, y=150,width=150)

        prenomAdherent= Entry(self.PageAjouterDesAdherents, textvariable=self.prenomAdherent,font= (5), bg="white")
        prenomAdherent.place(x=500, y=200,width=150)

        villeAdherent= Entry(self.PageAjouterDesAdherents,textvariable=self.codepostalAdherent, font= (5), bg="white")
        villeAdherent.place(x=500, y=240,width=150)
  
        codepostalAdherent= Entry(self.PageAjouterDesAdherents,textvariable=self.villeAdherent, font= (5), bg="white")
        codepostalAdherent.place(x=500, y=280,width=150)

        
        # bouton
        BoutonAjouterUnAdherent = Button(self.PageAjouterDesAdherents, command=self.ClickBoutonAjouterUnAdherent, text="Ajouter un adhérent",cursor="hand2", font=("times new roman",11), bd=0,bg="white",fg="black")
        BoutonAjouterUnAdherent.place(x=700, y=400)


    def VersPageAdherents(self): #fonction qui permet de supprimer la page
        self.PageAjouterDesAdherents.destroy()
        call(["python", "Adherents.py"])

    def Versgestiondesprets(self):
        self.PageAjouterDesAdherents.destroy()
        call(["python", "Gestiondesprets.py"])
        
    def Versgestionlivres(self):
        self.PageAjouterDesAdherents.destroy()
        call(["python", "Gestionlivres.py"])

    def PourSedeconnecter(self):
        lemessagebox = messagebox.askyesno("Déconnexion", "Voulez-vous vous déconnecter", parent=self.PageAjouterDesAdherents)
        if lemessagebox == YES:
         self.PageAjouterDesAdherents.destroy()
         call(["python", "Connexion.py"])

    
    def ClickBoutonAjouterUnAdherent(self):
        if self.nomAdherent.get()=="" or self.prenomAdherent.get()=="" or self.codepostalAdherent.get()=="" or self.villeAdherent.get()=="":
         messagebox.showerror("Erreur", "Veuillez, remplir tout les champs", parent=self.PageAjouterDesAdherents) #si tout les champs ne sont pas rempli alors affiche un message box pour dire que les champs ne sont pas rempli 
        
        else:
           try:
                connectionbdd= pymysql.connect(host="localhost", user="root", password="", database="bddcomptes")
                execut=connectionbdd.cursor()
                execut.execute("select * from adherent where nomAdherent=%s",self.nomAdherent.get())
                lignebdd= execut.fetchone() #fetchone récupere une seule ligne de la bdd

                if lignebdd != None: 
                    messagebox.showerror("Erreur", "Cet adhérent existe déja", parent=self.PageAjouterDesAdherents) #
                else:
                   execut.execute("insert into adherent(nomAdherent, prenomAdherent, codepostalAdherent, villeAdherent) values (%s,%s,%s,%s)",
                   (
                       
                       self.nomAdherent.get(),
                       self.prenomAdherent.get(),
                       self.codepostalAdherent.get(),
                       self.villeAdherent.get(),
                       
                    ))

                   messagebox.showinfo("Succes","L'adhérent à été ajouter avec succés", parent=self.PageAjouterDesAdherents)
                   
                connectionbdd.commit()
                connectionbdd.close
           except Exception as es :
                messagebox.showerror("erreur",f"Erreur de connexion{str(es)}",parent=self.PageAjouterDesAdherents)


root =Tk()
obj = AjouterDesadherents(root)
root.mainloop() 
