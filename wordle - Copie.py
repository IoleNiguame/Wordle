from tkinter import *
import random

mots = "herbe porte"
liste_de_mots = mots.split()
mot = list(random.choice(liste_de_mots))
print(mot)

root = Tk()
root.title("Wordle")
root.configure(bg="#29d9c9")

class Essai:
    def __init__(self):
        self.frame = Frame(root, bd=5)
        self.frame.pack()
        self.entry = Entry(self.frame, width=5, font=("Arial", 50), justify=CENTER, bg="#d5dfde", bd=0)
        self.entry.pack(side=LEFT)
        self.frame_lettres = Frame(self.frame)
        self.frame_lettres.pack(side=RIGHT)
        
    
    def verification(self):
        self.tentative = list(self.entry.get())
        print(self.tentative)
        self.entry.config(state=DISABLED)
        for i in self.tentative:
            if i in mot:
                if self.tentative.index(i) == mot.index(i):
                    label = Label(self.frame_lettres, text=i, fg='green', font=('Arial', 47), bg="#29d9c9")
                    label.pack(side=LEFT)
                else:
                    label = Label(self.frame_lettres, text=i, fg='#d96d22', font=('Arial', 47), bg="#29d9c9")
                    label.pack(side=LEFT)
            else:
                label = Label(self.frame_lettres, text=i, fg='#e62929', font=('Arial', 47), bg="#29d9c9")
                label.pack(side=LEFT)
            
            
essai = Essai()

def verifier():
    essai.verification()
    essai = Essai()

btn = Button(root, text="Verifier", font=('Arial', 20), bg="#93e32d", command=verifier)
btn.pack(side=BOTTOM, fill=X)

root.mainloop()