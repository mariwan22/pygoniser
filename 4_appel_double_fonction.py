#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter.messagebox import showinfo
import os
from os import listdir

root = Tk()
root.geometry("800x600-300+100")
root.title('Pygoniser')

# frame 1
Frame1 = Frame(root, borderwidth=2, relief=RIDGE)
Frame1.grid(column=0,row=0,sticky=N+W, padx=3, pady=3, ipadx=100)
# frame 2
Frame2 = Frame(root, borderwidth=2, relief=RIDGE)
Frame2.grid(column=1,row=0,sticky=N+E, padx=3, pady=3, ipadx=200)


# labels des frames
Label_Controle = Label(Frame1, text="Contrôle", font=(50)).pack(padx=1, pady=1, ipady=20)
Label_Listeur = Label(Frame2, text="Listeur", font=(50)).pack(padx=1, pady=1, ipady=20)

# frame controle
## labels et champs des entry
### entry 1 -> Cible == lettre lecteur

Frameentry1 = Frame(root, borderwidth=2, relief=SUNKEN)
Frameentry1.grid(column=0, row=1, ipadx=10, ipady=10)
Label_lecteur = Label(Frameentry1,
      text="Taper lettre lecteur en majuscule",
      wraplength=(150),
      bg="green",
      fg="white",
      borderwidth=4,relief=RIDGE).pack(side=LEFT, fill=X, padx=1, pady=1, ipady=20)
Cible=StringVar()
Lettre_lecteur=Entry(Frameentry1,textvariable=Cible)
Lettre_lecteur.pack(side=RIGHT, padx=1, pady=10)


### entry 2 -> Utilisateur == nom Users dans Windows
Frameentry2 = Frame(root, borderwidth=2, relief=SUNKEN)
Frameentry2.grid(column=0, row=2, ipadx=18, ipady=10)
Label_utilisateur = Label(Frameentry2,
      text="Taper nom user en respectant la casse",
      wraplength=(150),
      bg="green",
      fg="white",
      borderwidth=4,relief=RIDGE).pack(side=LEFT, fill=X, padx=1, pady=1, ipady=20)
Utilisateur=StringVar()
Nom_utilisateur=Entry(Frameentry2, textvariable=Utilisateur)
Nom_utilisateur.pack(side=RIGHT, padx=1, pady=10)




###################
#Fonctions Boutons#
###################

def double_fonction(*LesFonctions):
    def double_fonction(*ArgsFonctions,**KwargsFonctions):
        for Foncs in LesFonctions:
            Foncs(*ArgsFonctions,**KwargsFonctions)
    return double_fonction

def Liste_videos ():
    Cible1=Cible.get()
    Utilisateur1=Utilisateur.get()
    Chemin_videos=(f'{Cible1}:\\Users\\{Utilisateur1}\\Videos')
    Dico_videos=dict()
    listNom=[]
    listChemin=[]
    for videos in os.listdir(Chemin_videos):
        if (videos.endswith(".mkv")) or (videos.endswith(".avi")) or (videos.endswith(".mp4")):
            listNom.append(videos)
            listChemin.append(Chemin_videos+"\\"+videos)
    Dico_videos["Nom : "]=listNom
    Dico_videos["Chemin : "]=listChemin
    Listeur.delete(0,'end')
    for films in Dico_videos['Nom : ']:
        Listeur.insert(END, films) 


def Liste_audio():
    Cible1=Cible.get()
    Utilisateur1=Utilisateur.get()
    Chemin_audio=(f'{Cible1}:\\Users\\{Utilisateur1}\\Music')
    Dico_audio=dict()
    listNom=[]
    listChemin=[]
    for audio in os.listdir(Chemin_audio):
        if (audio.endswith(".mp3")) or (audio.endswith(".wav")) or (audio.endswith(".wma")):
            listNom.append(audio)
            listChemin.append(Chemin_audio+"\\"+audio)
    Dico_audio["Nom : "]=listNom
    Dico_audio["Chemin : "]=listChemin
    Listeur.delete(0,'end')
    for sons in Dico_audio['Nom : ']:
        Listeur.insert(END, sons)

def Liste_image():
    Cible1=Cible.get()
    Utilisateur1=Utilisateur.get()
    Chemin_image=(f'{Cible1}:\\Users\\{Utilisateur1}\\Pictures')
    Dico_image=dict()
    listNom=[]
    listChemin=[]
    for image in os.listdir(Chemin_image):
        if (image.endswith(".png")) or (image.endswith(".jpg")) or (image.endswith(".jpeg")):
            listNom.append(image)
            listChemin.append(Chemin_image+"\\"+image)
    Dico_image["Nom : "]=listNom
    Dico_image["Chemin : "]=listChemin
    Listeur.delete(0,'end')
    for images in Dico_image['Nom : ']:
        Listeur.insert(END, images)

def Liste_docs():
    Cible1=Cible.get()
    Utilisateur1=Utilisateur.get()
    Chemin_documents=(f'{Cible1}:\\Users\\{Utilisateur1}\\Documents')
    Dico_docs=dict()
    listNom=[]
    listChemin=[]
    for documents in os.listdir(Chemin_documents):
        if (documents.endswith(".pdf")) or (documents.endswith(".doc")) or (documents.endswith(".csv")):
            listNom.append(documents)
            listChemin.append(Chemin_documents+"\\"+documents)
    Dico_docs["Nom : "]=listNom
    Dico_docs["Chemin : "]=listChemin
    Listeur.delete(0,'end')
    for docs in Dico_docs['Nom : ']:
        Listeur.insert(END, docs)

##FLUSH LISTBOX
def Flush_list ():
    Listeur.delete(0,'end')



##fonction fenêtre de confirmation de création liste
def Confirmation():    
    msg = ("Listage en cours !")
    showinfo(title='Information', message=msg)



########################
#Fins fonctions boutons#
########################

# frame control

Framecontrol1 = Frame(root, borderwidth=2)
Framecontrol1.grid(column=0, row=3, ipadx=10, ipady=50)
Boutonvideos=Button(Framecontrol1,text="lister videos",
                    command=double_fonction(Confirmation,Liste_videos),
                    pady=10,width=30).pack()

Boutonaudio=Button(Framecontrol1,text="lister musiques",
                    command=double_fonction(Confirmation,Liste_audio),
                    pady=10,width=30).pack()
                    
Boutonimage=Button(Framecontrol1,text="lister images",
                    command=double_fonction(Confirmation,Liste_image),
                    pady=10,width=30).pack()
                    
Boutonaudio=Button(Framecontrol1,text="lister documents",
                    command=double_fonction(Confirmation,Liste_docs),
                    pady=10,width=30).pack()

Framecontrol2 = Frame(root, borderwidth=2)
Framecontrol2.grid(column=0, row=4, ipadx=10, ipady=50)

Boutonflushlist=Button(Framecontrol1,text="Reset",
                       command=Flush_list,
                       pady=10, width=30).pack()

Boutonquitter=Button(Framecontrol1,text="Quitter",
                     command=root.destroy,
                    pady=10, width=30).pack()

## frame listeur

Framelisteur = Frame(root, borderwidth=2, relief=SUNKEN)
Framelisteur.grid(column=1, row=1, ipadx=1, ipady=1, rowspan=3,sticky=NSEW)
Label_liste = Label(Framelisteur,
      text="Liste des fichiers",
      bg="Black",
      fg="white",
      borderwidth=4,relief=RIDGE).pack(side=TOP, fill=X, padx=1, pady=1, ipady=20)
Listeur = Listbox(Framelisteur, height=15, width=50)
Listeur.pack(side=TOP, fill=X, padx=10, pady=20, ipady=70)
Listeur.insert("end")
scrollbar = Scrollbar(Listeur)
Listeur.config(yscrollcommand = scrollbar.set)
scrollbar.config(command = Listeur.yview)
scrollbar.pack(side=RIGHT, fill=Y)

Afficheur=Label(Framelisteur).pack()
Lanceur=Button(Framelisteur,text="Lire le média").pack()


#######################################################



#######################################################


root.mainloop()