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
Cible=Entry(Frameentry1,
            exportselection = 0).pack(side=RIGHT, padx=1, pady=10)

### entry 2 -> Utilisateur == nom Users dans Windows
Frameentry2 = Frame(root, borderwidth=2, relief=SUNKEN)
Frameentry2.grid(column=0, row=2, ipadx=18, ipady=10)
Label(Frameentry2,
      text="Taper nom user en respectant la casse",
      wraplength=(150),
      bg="green",
      fg="white",
      borderwidth=4,relief=RIDGE).pack(side=LEFT, fill=X, padx=1, pady=1, ipady=20)
Utilisateur=Entry(Frameentry2,
                  exportselection = 0).pack(side=RIGHT, padx=1, pady=10)

## Construction chemins

#C:\Users\MB\Videos
#C:\Users\MB\Music
#C:\Users\MB\Pictures
#C:\Users\MB\Documents
#C:\Users\MB\Downloads

Ch_videos=(f'{Cible}:\\Users\\{Utilisateur}\\Videos')
Ch_audio=(f'{Cible}:\\Users\\{Utilisateur}\\Music')
Ch_images=(f'{Cible}:\\Users\\{Utilisateur}\\Pictures')
Ch_documents=(f'{Cible}:\\Users\\{Utilisateur}\\Documents')
Ch_telechargements=(f'{Cible}:\\Users\\{Utilisateur}\\Downloads')

#Fonctions Button commands




# frame control

Framecontrol1 = Frame(root, borderwidth=2)
Framecontrol1.grid(column=0, row=3, ipadx=10, ipady=50)
Boutonvideos=Button(Framecontrol1,text="lister videos",
                    pady=10,width=30).pack()
Boutonaudio=Button(Framecontrol1,text="lister audio",
                   pady=10,width=30).pack()
Boutonimages=Button(Framecontrol1,text="lister images",
                    pady=10,width=30).pack()
Boutondocuments=Button(Framecontrol1,text="lister documents",
                       pady=10,width=30).pack()

Framecontrol2 = Frame(root, borderwidth=2)
Framecontrol2.grid(column=0, row=4, ipadx=10, ipady=50)
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
Listeur.insert("end", "one", "two", "three", "four", "five", "six",
               "seven", "eight", "nine", "ten", "eleven", "twelve",
               "thirteen", "fourteen", "fifteen", "sixteen")
scrollbar = Scrollbar(Listeur)
Listeur.config(yscrollcommand = scrollbar.set)
scrollbar.config(command = Listeur.yview)


root.mainloop()
