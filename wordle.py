from tkinter import *
import random

mots = "herbe porte"
liste_de_mots = mots.split()
mot = list(random.choice(liste_de_mots))
print(mot)
root = Tk()

entree = Entry(root, width=50, font=("Arial", 20))
entree.pack()

def verifier():
    tentative = list(entree.get())
    for i in tentative:
        if i in mot:
            if tentative.index(i) == mot.index(i):
                print('très bien !! %s' % i)
            else:
                print('bien... %s' % i)
                
        else:
            print('dommage  %s' % i)

btn = Button(root, text="Bien", command=verifier)
btn.pack()

root.mainloop()