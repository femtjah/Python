from tkinter import * 

raiz= Tk()

miFrame=Frame(raiz, width=1200, height=600)
miFrame.pack()

minombre=StringVar()
cuadroNombre = Entry(miFrame, textvariable=minombre)
cuadroNombre.grid(row=0,column=1, padx=4)
cuadroNombre.config(fg="red", justify="center")
cuadroPassword = Entry(miFrame)
cuadroPassword.grid(row=1,column=1, padx=4)
cuadroPassword.config(show="=")
cuadroApellido = Entry(miFrame)
cuadroApellido.grid(row=2,column=1, padx=4)
cuadroDireccion = Entry(miFrame)
cuadroDireccion.grid(row=3,column=1,padx=4)
textoComentario=Text(miFrame, width= 16, height=5)
textoComentario.grid(row=4,column=1, padx=10, pady=10)
scrollvert=Scrollbar(miFrame, command=textoComentario.yview)
scrollvert.grid(row=4, column=2, sticky="nsew")
textoComentario.config(yscrollcommand=scrollvert.set)

nombreLabel=Label(miFrame, text="Nombre:")
nombreLabel.grid(row=0,column=0, sticky="e", pady=4)
passwordLabel=Label(miFrame, text="Password:")
passwordLabel.grid(row=1,column=0, sticky="e", pady=4)
apellidoLabel=Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=2,column=0, sticky="e", pady=4)
direccionLabel=Label(miFrame, text="Direccion:")
direccionLabel.grid(row=3,column=0, sticky="e", pady=4)
comentarioLabel=Label(miFrame, text="Comentarios:")
comentarioLabel.grid(row=4,column=0, sticky="e", pady=4)

def codigoBoton():
    minombre.set("Fabio")
    
botonEnvio=Button(raiz, text="Enviar", command=codigoBoton)
botonEnvio.pack()


raiz.mainloop()