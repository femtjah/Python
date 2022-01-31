from tkinter import * 

raiz=Tk() #crear la raiz app
raiz.title("Ventana de pruebas") 
#raiz.resizable(True,False) Bloqueo de cambio de dimencion  
raiz.iconbitmap("Reggae.ico")
# raiz.geometry("650x350") # tamaño ventana
raiz.config(bg="green") #fondo
raiz.config(bd=25)
raiz.config(relief="groove")

miFrame=Frame()
miFrame.pack()
#miFrame.pack(side="left", anchor="n") # enpaquete en la raiz y darle un punto donde deve quedarce 
#miFrame.pack(fill="both", expand=True) #expandir en x o y 
miFrame.config(bg="yellow")
miFrame.config(width=650, height=350)
miFrame.config(bd=35)
miFrame.config(relief="sunken")
miFrame.config(cursor="pirate")


miLabel= Label(miFrame, text="Hola alumnos de Python", fg="red", font=("Comic Sans MS",18)).place(x=100, y=200)


raiz.mainloop()

