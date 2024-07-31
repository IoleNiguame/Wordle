from tkinter import *
import random
import pickle

mots = """herbe porte comme entre
cette
était
après
Paris
aussi
alors
ainsi
ville
notes
trois
monde
année
titre
avant
décès
série
avoir
temps
avait
place
début
autre
suite
faire
cours
leurs
album
ligne
moins
homme
forme
grand
selon
genre
situé
ayant
étant
Coupe
Grand
scène
nommé
celle
celui
sorti
ordre
armée
jours
reste
droit
point
prend
femme
siège
effet
toute
match
fille
avril
liste
jeune
texte
route
maire
poste
corps
parti
roman
école
connu
elles
porte
image
ouest
livre
style
union
terme
petit
passe
donne
durée
films
comté
parmi
objet
cadre
cause
comte
quand
abord"""
liste_de_mots = mots.split()
mot = list(random.choice(liste_de_mots))

root = Tk()
root.title("Wordle")
root.configure(bg="#29d9c9")
root.resizable(0, 0)

essais = 0

class Essai:
    def __init__(self):
        self.frame = Frame(root, bd=5)
        self.frame.pack()
        self.entry = Entry(self.frame, width=6, font=("Arial", 50), justify=CENTER, bg="#d5dfde", bd=0)
        self.entry.pack(side=LEFT)
        self.frame_lettres = Frame(self.frame)
        self.frame_lettres.pack(side=RIGHT)
        
    
    def verification(self):
        self.tentative = list(self.entry.get())
        self.entry.config(state=DISABLED)
        if self.tentative == mot:
            rootG = Tk()
            rootG.title("Wordle_perdu")
            rootG.configure(bg="red")
            rootG.resizable(0, 0)
            labelG = Label(rootG, text="Vous avez gagné(e)", font=('Arial', 40), bg='green')
            labelG.pack()
            rootG.mainloop()
        else:
            for indice,lettre in enumerate(self.tentative):
                if lettre in mot:
                    if self.tentative[indice] == mot[indice]:
                        label = Label(self.frame_lettres, text=lettre, fg='green', font=('Arial', 47), bg="#29d9c9")
                        label.pack(side=LEFT)
                    else:
                        label = Label(self.frame_lettres, text=lettre, fg='#d96d22', font=('Arial', 47), bg="#29d9c9")
                        label.pack(side=LEFT)
                else:
                    label = Label(self.frame_lettres, text=lettre, fg='#e62929', font=('Arial', 47), bg="#29d9c9")
                    label.pack(side=LEFT)
            if essais >= 5:
                rootP = Tk()
                rootP.title("Wordle_perdu")
                rootP.configure(bg="red")
                rootP.resizable(0, 0)
                labelPerdu = Label(rootP, text="Vous avez perdu(e)...", font=('Arial', 40), bg='red')
                labelPerdu.pack()
                rootP.mainloop()
            
            
essai = Essai()

essais = 0
def verifier():
    global essais
    essais += 1
    global essai
    essai.verification()
    essai = Essai()

btn = Button(root, text="Verifier", font=('Arial', 20), bg="#93e32d", command=verifier)
btn.pack(side=BOTTOM, fill=X)

f_donnee = open('donnee_wordle.dat', 'rb')
nb = pickle.load(f_donnee)
f_donnee.close()
print(nb)

root.mainloop()