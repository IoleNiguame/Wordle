from tkinter import *
import random

mots = "herbe porte"
liste_de_mots = mots.split()
mot = list(random.choice(liste_de_mots))
print(mot)
root = Tk()

entree = Entry(root, width=50, font=("Arial", 20), justify=CENTER)
entree.pack()

def verifier():
    tentative = list(entree.get())
    for i in tentative:
        if i in mot:
            if tentative.index(i) == mot.index(i):
                label = Label(root, text=i, fg='green')
                label.pack(side=LEFT)
            else:
                print('bien... %s' % i)
                label = Label(root, text=i, fg='orange')
                label.pack(side=LEFT)
        else:
            print('dommage  %s' % i)
            label = Label(root, text=i, fg='red')
            label.pack(side=LEFT)

btn = Button(root, text="Bien", command=verifier)
btn.pack()

root.mainloop()