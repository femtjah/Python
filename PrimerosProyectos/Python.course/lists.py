[1, "hello", 1.34, True,[1,2,3]]
colors= ["red","green","blue"]

numbers_list = list((1,2,3,4))
#print(type(numbers_list))

r= list(range(1,10))
print(r)

#dir = nos indica los metodos 

print(colors[2])
print("vieleta" in colors)
print(colors)
colors[1]="yellow"
print(colors)

#colors.append("violet") agragar 1 a 1 

colors.extend(["violet", "green"]) #agregar lista o tupla a una lista 1 a 1 

colors.insert(1,"porple")
#colors.pop() # Eliminar en posicion 
#colors.remove("green") # eliminar por caracter
colors.sort(reverse=True) # ordenar alfaveticamente 
print(colors)

