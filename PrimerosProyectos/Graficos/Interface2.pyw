from tkinter import *


raiz=Tk()

miFrame=Frame()
miFrame.config(width=650, height=450)

miFrame.pack()

miImagen=PhotoImage(file="Hola.gif")
Label(miFrame, image=miImagen).place(x=100, y=200)

raiz.mainloop()
