
menu=f"""CARRITO DE COMPRAS
        OPCIONES DISPONIBLES
        1 : AGREGAR PRODUCTO
        2 : ELIMINAR PRODUCTO
        3 : MOSTRAR LA LISTA ORDENADA
        4 : BUSCAR PRODUCTO
        5 : CONTAR PRODUCTOS DE CARRITO
        6 : VACIAR EL CARRITO
        """

print(menu)

supermarkecar=["laptop", "vaso", "cafe", "audifonos"]
print(supermarkecar)
seleccion=int(input("Selecciona una opcion disponible del menu: "))


if seleccion ==1:
    supermarkecar.append(input("Que producto deseas agregar: "))
    print(supermarkecar)
    pass
elif seleccion ==2:
    eliminar=input(f"Ingresa lo q eliminaras: {supermarkecar} :")
    if eliminar not in supermarkecar:
        print("No se encuentra dentro de la lista ")
        pass
    else:
        index=supermarkecar.index(eliminar)
        supermarkecar.pop(index)
        print(supermarkecar)
        pass
elif seleccion ==3:
    supermarkecar.sort()
    print("se creo una lista nueva ")
    pass
elif seleccion ==4:
    busqueda=input("que producto buscas dentro de tu carrito? ")
    print(busqueda in supermarkecar)
    pass
elif seleccion ==5:
    cantidad_productos=len(supermarkecar)
    print(f"existe una cantidad de {cantidad_productos} en tu carrito")
    pass
elif seleccion ==6:
    supermarkecar.clear()
    print(supermarkecar)
    pass
else:
    print("no existen mas opciones intenta con las disponibles")
    pass



