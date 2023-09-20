# Listeur avec fonction

import os
from os import listdir

#C:\Users\MB\Videos
#C:\Users\MB\Music
#C:\Users\MB\Pictures
#C:\Users\MB\Documents
#C:\Users\MB\Downloads

Lecteur=str(input("Taper le nom du disque à scanner en majuscule : "))
Utilisateur=str(input("Taper le nom d'utilisateur en respectant la casse : "))

Ch_videos=(Lecteur+":\\Users\\"+Utilisateur+"\\Videos")
Ch_audio=(Lecteur+":\\Users\\"+Utilisateur+"\\Music")
Ch_image=(Lecteur+":\\Users\\"+Utilisateur+"\\Pictures")
Ch_documents=(Lecteur+":\\Users\\"+Utilisateur+"\\Documents")

Dico_videos={}
Dico_audio={}
Dico_image={}
Dico_documents={}


#Listeur videos

def list_videos ():
    for videos in os.listdir(Ch_videos):
        if (videos.endswith(".mkv")) or (videos.endswith(".mp4")) or (videos.endswith(".avi")):
            print(Ch_videos+"\\"+videos)
            
print(list_videos())

#Listeur audio

def list_audio ():
    for audio in os.listdir(Ch_audio):
        if (audio.endswith(".mp3")) or (audio.endswith(".wav")) or (audio.endswith(".ogg")):
            print(Ch_audio+"\\"+audio)
            
print(list_audio())

#Listeur image

def list_image ():
    for images in os.listdir(Ch_image):
        if (images.endswith(".jpg")) or (images.endswith(".png")) or (images.endswith(".gif")):
            print(Ch_image+"\\"+images)
            
print(list_image())

#Listeur documents

def list_documents ():
    for documents in os.listdir(Ch_documents):
        if (documents.endswith(".doc")) or (documents.endswith(".docx")) or (documents.endswith(".pdf")):
            print(Ch_documents+"\\"+documents)
            
print(list_documents())

