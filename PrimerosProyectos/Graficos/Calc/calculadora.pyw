from tkinter import *
from Calc import *

raiz= Tk()
""" one,two,three,four,five,six,seven,eight,nine,zero """
miFrame2=Frame(raiz)
miFrame2.pack()

cuadroOper=Text(miFrame2, width=20, height=10)
cuadroOper.grid(row=0,column=0 ,padx=10, pady=5)

miFrame=Frame(raiz, width=600, height=1000)
miFrame.pack()

#Numeros
botonSeven=Button(miFrame,bg="black", fg="red", text="7", font=("Comic Sans MS",18))
botonSeven.grid(row=1,column=0, pady=5,padx=5)
botonFour=Button(miFrame,bg="black", fg="red", text="4",font=("Comic Sans MS",18))
botonFour.grid(row=2,column=0, pady=5,padx=5)
botonOne=Button(miFrame,bg="black", fg="red", text="1",font=("Comic Sans MS",18))
botonOne.grid(row=3,column=0, pady=5,padx=5)
botonEight=Button(miFrame,bg="black", fg="red", text="8",font=("Comic Sans MS",18))
botonEight.grid(row=1,column=1, pady=5,padx=5)
botonFive=Button(miFrame,bg="black", fg="red", text="5",font=("Comic Sans MS",18))
botonFive.grid(row=2,column=1, pady=5,padx=5)
botonTwo=Button(miFrame,bg="black", fg="red", text="2",font=("Comic Sans MS",18))
botonTwo.grid(row=3,column=1, pady=5,padx=5)
botonZero=Button(miFrame,bg="black", fg="red", text="0",font=("Comic Sans MS",18))
botonZero.grid(row=4,column=1, pady=5,padx=5)
botonNine=Button(miFrame,bg="black", fg="red", text="9", font=("Comic Sans MS",18))
botonNine.grid(row=1,column=2, pady=5,padx=5)
botonSix=Button(miFrame,bg="black", fg="red", text="6",font=("Comic Sans MS",18))
botonSix.grid(row=2,column=2, pady=5,padx=5)
botonThree=Button(miFrame,bg="black", fg="red", text="3",font=("Comic Sans MS",18))
botonThree.grid(row=3,column=2, pady=5,padx=5)

"""cuadrOperaciones=Label(miFrame, text="")
cuadrOperaciones.grid(row=0,column=0, sticky="e",pady=5, padx=10)"""
#Operaciones
botonDivide=Button(miFrame,bg="black", fg="red", text="/",font=("Comic Sans MS",18),command=div)
botonDivide.grid(row=1,column=3, pady=5,padx=5)
botonMulti=Button(miFrame,bg="black", fg="red", text="*",font=("Comic Sans MS",18),command=mul)
botonMulti.grid(row=2,column=3, pady=5,padx=5)
botonResta=Button(miFrame,bg="black", fg="red", text="-",font=("Comic Sans MS",18),command=res)
botonResta.grid(row=3,column=3, pady=5,padx=5)
botonSuma=Button(miFrame,bg="black", fg="red", text="+",font=("Comic Sans MS",18),command=sum)
botonSuma.grid(row=4,column=3, pady=5,padx=5)
botonIgual=Button(miFrame,bg="black", fg="blue", text="=",font=("Comic Sans MS",18))
botonIgual.grid(row=4,column=2, pady=5,padx=5)
botonBorrar=Button(miFrame,bg="black", fg="blue", text="C",font=("Comic Sans MS",18))
botonBorrar.grid(row=4,column=0, pady=5,padx=5)

raiz.mainloop()