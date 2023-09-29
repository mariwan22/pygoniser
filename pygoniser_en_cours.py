#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *

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
Label(Frame1, text="Contrôle", font=(50)).pack(padx=1, pady=1, ipady=20)
Label(Frame2, text="Listeur", font=(50)).pack(padx=1, pady=1, ipady=20)

# frame controle
## labels et champs des entry
### entry 1 -> Cible == lettre lecteur

Frameentry1 = Frame(root, borderwidth=2, relief=SUNKEN)
Frameentry1.grid(column=0, row=1, ipadx=10, ipady=10)
Label(Frameentry1,
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
Label(Frameentry2,
      text="Taper nom user en respectant la casse",
      wraplength=(150),
      bg="green",
      fg="white",
      borderwidth=4,relief=RIDGE).pack(side=LEFT, fill=X, padx=1, pady=1, ipady=20)
Utilisateur=StringVar()
Nom_utilisateur=Entry(Frameentry2, textvariable=Utilisateur)
Nom_utilisateur.pack(side=RIGHT, padx=1, pady=10)

Dico_videos=dict()

##VIDEOS
def traite_videos(*Fonctions_videos):
    def traite_videos(*FV1, **FV2):
        for Ma_Fonction_Video in Fonctions_videos:
            Ma_Fonction_Video(*FV1,**FV2)
        return traite_videos


Dico_videos=dict()

def list_videos ():
    Cible1=Cible.get()
    Utilisateur1=Utilisateur.get()
    Ch_videos=(f'{Cible1}:\\Users\\{Utilisateur1}\\Videos')
    global Dico_videos
    Nom_video=[]
    Chemin_video=[]
    for videos in os.listdir(Ch_videos):
        if (videos.endswith(".mkv")) or (videos.endswith(".mp4")) or (videos.endswith(".avi")):
            Nom_video.append(videos)
            Chemin_video.append(Ch_videos+"\\"+videos)
    Dico_videos["Nom : "]=Nom_video
    Dico_videos["Chemin : "]=Chemin_video
    return Dico_videos
    
def affiche_videos():
    for films in Dico_videos["Nom : "]:
        Listeur.insert(END, films)  
    
##FLUSH LISTBOX
def Flush_list ():
    Listeur.delete(0,'end')

# frame control

Framecontrol1 = Frame(root, borderwidth=2)
Framecontrol1.grid(column=0, row=3, ipadx=10, ipady=50)
Boutonvideos=Button(Framecontrol1,text="lister videos",
                    command=traite_videos(list_videos,affiche_videos),
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
Framelisteur.grid(column=1, row=1, ipadx=18, ipady=10,rowspan=3)
Label(Framelisteur,
      text="Liste des fichiers",
      bg="Black",
      fg="white",
      borderwidth=4,relief=RIDGE).pack(side=TOP, fill=X, padx=1, pady=1, ipady=20)
Listeur = Listbox(Framelisteur, height=20, width=50)
Listeur.pack(side=TOP, fill=BOTH)
scrollbar = Scrollbar(Listeur)
Listeur.config(yscrollcommand = scrollbar.set)
scrollbar.config(command = Listeur.yview)


root.mainloop()
