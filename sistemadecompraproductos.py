productos= tuple((
    "Coca-Cola", 
    "Pepsi", 
    "Sprite", 
    "Fanta", 
    "7UP", 
    "Mountain Dew", 
    "Dr Pepper", 
    "Schweppes", 
    "Mirinda", 
    "Lift"))
precios = tuple((
    4500, 
    3750, 
    3000, 
    3600, 
    5250, 
    6000, 
    5400, 
    3900, 
    4200, 
    4800))

print("menu de seleccion de productos")
for i,val in enumerate(productos):
    print(f"""   {i}, {val} ${precios[i]}""")

opcion = int(input())
print (f"Usuario usted selecciono el producto {productos[opcion]} con un valor de ${precios[opcion]}")

dinero= int(input("Ingrese la cantidad de dinero disponible"))
vueltos = dinero - precios[opcion]
if dinero >=precios[opcion]:
    print(f"Usuario usted compro el producto {productos[opcion]} con un valor de ${precios[opcion]}, sus vueltos son ${vueltos}")
else:
    print(f"Ususario el producto que desea comprar {productos[opcion]}, con un valor de ${precios[opcion]}, le falta un total de ${-vueltos}")    
    
    
#hacer lo mismo pero con un producto de panaderia
#categoria de panes, hacer un menu, con una categoria,esa categoria tiene que mostrar los productos de esa categoria, despues seleccionar el producto y decir cuantos productos desea, con promocion
