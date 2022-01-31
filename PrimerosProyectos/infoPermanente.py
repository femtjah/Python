import pickle

class Persona:
    def __init__(self, nombre, genero, edad):
        self.nombre=nombre
        self.genero=genero
        self.edad=edad
        print("Se ha creado una persona nueva con el nombre de ",self.nombre)

    def __str__(self):
        return "{} {} {}".format(self.nombre, self.genero, self.edad)

class ListaPersonas: 
    personas= []

    def __init__(self):
        listDePersonas=open("ficheroExterno", "ab+")
        listDePersonas.seek(0)

        try:
            self.personas=pickle.load(listDePersonas)
            print("Se cargaron {} personas del fichero externo".format(len(self.personas)))
        except:
            print("El fichero está vacío")
        finally:
            listDePersonas.close()
            del(listDePersonas)     

    def agregarPersonas(self, p):
        self.personas.append(p)
        self.guardarPersonasEnFicheroExterno()

    def mostrarPersonas(self):
        for p in self.personas:
            print(p)

    def guardarPersonasEnFicheroExterno(self):
        listDePersonas=open("ficheroExterno", "wb")
        pickle.dump(self.personas, listDePersonas)
        listDePersonas.close()
        del(listDePersonas)        

    def mostrarInfoFicheroExterno(self):
        print("La información del fichero externo es la siguiente: ")
        for p in self.personas:
            print(p)

miLista=ListaPersonas()            
persona=Persona("fernando", "Masculino", 39)
miLista.agregarPersonas(persona)
miLista.mostrarInfoFicheroExterno()


