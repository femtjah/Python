from abc import ABCMeta


class Persona():
    def __init__(self, nombre, edad, lugar_residencia):
        self.nombre=nombre
        self.edad=edad
        self.lugar_residencia=lugar_residencia

    def descripccion(self):
        print("Nombre: ", self.nombre, " Edad: ", self.edad, " Residencia: ",self.lugar_residencia)

class Empleado(Persona):
    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):
        super().__init__(nombre_empleado, edad_empleado, residencia_empleado)
        self.salario=salario
        self.antiguedad=antiguedad
    def descripccion(self):
        super().descripccion()
        print("Salario: ", self.salario, " Antigüedad: ", self.antiguedad)

        
print("------------Ejemplos-----------")

Manuel=Empleado(1500, 15, "Manuel", 55, "Colombia ")

Manuel.descripccion()

print(isinstance(Manuel, Persona)) 