class Vehiculos():
    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
        self.enMarcha=False
        self.acelera=False
        self.frena=False

    def arrancar(self):
        self.enMarcha=True

    def acelera(self):
        self.acelera=True    
    
    def frena(self):
        self.frena=True

    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ",self.enMarcha, "\nAcelerando: ", self.acelera,"\nFrenando: ",self.frena)

class VElectricos(Vehiculos):
    def __init__(self, marca_bici,  modelo_bici):
        super().__init__(marca_bici, modelo_bici)
        self.autonomia=100
    def cargaEnergia(self):
        self.cargando=True
    def estado(self):
        return super().estado()    

class Furgoneta(Vehiculos):
    def carga(self, carga):
        self.cargado=carga
        if(self.cargado):
            return"La furgoneta esta cargada"
        else:
            return "La furgoneta no esta cargada"            

class Moto(Vehiculos):
    hcaballito=""
    def caballito(self):
        self.hcaballito="Voy haciendo el caballito"
    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ",self.enMarcha, "\nAcelerando: ", self.acelera,"\nFrenando: ",self.frena, "\n", self.hcaballito)



class BicicletaElectrica(VElectricos, Vehiculos):

    pass            
        

print("------------------Comienzo de pruebas-------------------")

miMoto=Moto("Yamaha","R1 M")
miMoto.caballito()

print( miMoto.estado())

print("--------------Furgoneta----------------")

miFurgoneta=Furgoneta("Renault", "Kangoo")
miFurgoneta.arrancar()
print(miFurgoneta.estado())
print(miFurgoneta.carga(True))

print("-------------Bici------------------")

miBici=BicicletaElectrica("Orbea", "IJK")
miBici.estado()


