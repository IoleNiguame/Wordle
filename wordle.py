from tkinter import *
import random

mots = "herbe porte"
liste_de_mots = mots.split()
mot = list(random.choice(liste_de_mots))
print(mot)

root = Tk()
root.title("Wordle")
root.configure(bg="#29d9c9")

def Entre(self):
    entree = Entry(root, width=5, font=("Arial", 50), justify=CENTER, bg="#d5dfde", bd=0)
    entree.pack(side=TOP)

Entre()

def verifier():
    tentative = list(entry.entree.get())
    for i in tentative:
        if i in mot:
            if tentative.index(i) == mot.index(i):
                label = Label(root, text=i, fg='green', font=('Arial', 50), bg="#29d9c9")
                label.pack(side=LEFT)
            else:
                print('bien... %s' % i)
                label = Label(root, text=i, fg='#d96d22', font=('Arial', 50), bg="#29d9c9")
                label.pack(side=LEFT)
        else:
            print('dommage  %s' % i)
            label = Label(root, text=i, fg='#e62929', font=('Arial', 50), bg="#29d9c9")
            label.pack(side=LEFT)

btn = Button(root, text="Verifier", font=('Arial', 20), bg="#93e32d", command=verifier)
btn.pack(side=BOTTOM)

root.mainloop()