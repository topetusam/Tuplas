productos = {
    "Panes_Dulces": [
        {"nombre": "Pan de canela", "precio": 2500},
        {"nombre": "Rosca de pasas", "precio": 1250},
        {"nombre": "Concha de chocolate", "precio": 3500},
        {"nombre": "Pan de nueces", "precio": 4000},
        {"nombre": "Cuerno de vainilla", "precio": 3700},
        {"nombre": "Trenza de frutas", "precio": 4600},
        {"nombre": "Oreja de azúcar", "precio": 1000},
        {"nombre": "Bollo de canela", "precio": 1300},
        {"nombre": "Donas variadas", "precio": 8000},
        {"nombre": "Pan de almendra", "precio": 10000}
    ],
    "Panes_Salados": [
        {"nombre": "Pan de ajo", "precio": 3500},
        {"nombre": "Baguette de hierbas", "precio": 7500},
        {"nombre": "Fougasse de aceitunas", "precio": 3450},
        {"nombre": "Pretzel", "precio": 4250},
        {"nombre": "Pan integral de semillas", "precio": 2500},
        {"nombre": "Bollos de queso", "precio": 3850},
        {"nombre": "Pan de centeno", "precio": 7900},
        {"nombre": "Pan de focaccia", "precio": 12000},
        {"nombre": "Palitos de pan con romero", "precio": 6750},
        {"nombre": "Pan de centeno con pasas", "precio": 15000}
    ],
    "Postres": [
        {"nombre": "Tarta de chocolate", "precio": 20000},
        {"nombre": "Helado de vainilla", "precio": 5000},
        {"nombre": "Cheesecake de fresa", "precio": 12500},
        {"nombre": "Crepes de crema y frutas", "precio": 4670},
        {"nombre": "Tiramisú", "precio": 11900},
        {"nombre": "Pastel de zanahoria", "precio": 4900},
        {"nombre": "Flan de caramelo", "precio": 7750},
        {"nombre": "Fresas con crema", "precio": 9500}
    ],
    "Promociones": {
        "Oferta Especial": (
            {"nombre": "Pan Especial", "precio": 10000},
            {"nombre": "Descuento en Postres", "precio": 2000},
            {"nombre": "Combo Salado y Dulce", "precio": 1000}
        )
    }
}

while True:
    print("Que desea hoy, Pan Dulce, Pan salado o algun Postre? :")

    for i, (key, val) in enumerate(productos.items()):
        if (key!="Promociones"):
            print(f"{i} ,{key},")
    opcion=int(input("Ingrese la opcion deseada : "))
    opcion_deseada=list(productos.keys())[opcion]

    print(f"Usted escogio {opcion_deseada}, por favor escoja su pan preferido :")

    for i, productoseleccionado in enumerate(productos[opcion_deseada]):
        nombre_producto=productoseleccionado["nombre"]
        precio_producto=productoseleccionado["precio"]
        print(f"{i} {nombre_producto}, con un precio de $ {precio_producto}.")

    productosel=int(input("Que producto desea de la lista :"))

    producto_elegido=productos[opcion_deseada][productosel]

    producto_elegido_nombre= producto_elegido["nombre"]
    producto_elegido_precio= producto_elegido["precio"]
    print(f"Usted escogió {producto_elegido_nombre}, con un precio de ${producto_elegido_precio}")

    dinero = int(input("Con cuanto va a pagar? :"))
    

    if dinero >= producto_elegido_precio:
        cambio = dinero - producto_elegido_precio
        print(f"Le sobran ${cambio}")
    else:
        print("No tiene suficiente dinero")

    otroproducto=input("Desea comprar otro producto? s/n : ").lower()
    if otroproducto == 'n':
        print("Gracias por su compra!, vuelva pronto")
        break