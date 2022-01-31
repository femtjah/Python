def devuelveCiudades(*ciudades):
    for elemento in ciudades:
        #for subElemento in elemento:
            yield from elemento

ciudadesDevueltas=devuelveCiudades('Madrid','Barcelona','Bilbao','Valencia')
print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))