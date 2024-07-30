from tkinter import *
import random

mots = "herbe porte"
liste_de_mots = mots.split()
mot = list(random.choice(liste_de_mots))
print(mot)

root = Tk()
root.title("Wordle")
root.configure(bg="#29d9c9")


entree = Entry(root, width=5, font=("Arial", 50), justify=CENTER, bg="#d5dfde", bd=0)
entree.grid(column=0, row=0)

def verifier():
    tentative = list(entree.get())
    lettres = 1
    for i in tentative:
        if i in mot:
            if tentative.index(i) == mot.index(i):
                label = Label(root, text=i, fg='green', font=('Arial', 50), bg="#29d9c9")
                label.grid(column=lettres, row=0)#pack(side=BOTTOM)
                print(lettres)
            else:
                print('bien... %s' % i)
                label = Label(root, text=i, fg='#d96d22', font=('Arial', 50), bg="#29d9c9")
                label.grid(column=lettres, row=0)
        else:
            print('dommage  %s' % i)
            label = Label(root, text=i, fg='#e62929', font=('Arial', 50), bg="#29d9c9")
            label.grid(column=lettres, row=0)
        lettres += 1
        

btn = Button(root, text="Verifier", font=('Arial', 20), bg="#93e32d", command=verifier)
btn.grid(row=2, column=0)#pack(side=BOTTOM)

root.mainloop()