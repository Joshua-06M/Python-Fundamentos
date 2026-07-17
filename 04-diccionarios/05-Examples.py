#Ejemplos Listas

"""List slicing"""

# Bikes=["Kawasaki", "Yamaha", "MV", "Ducati"]
# print(Bikes)
# #Se crea una nueva lista recortando la original 
# prox_list=Bikes[10:50]
# print(prox_list)

"""LIst_methods_adding"""

#.append

# lista_prueba=[1,2,3,4,5]
# print(lista_prueba)
# lista_prueba.append(400)
# print(lista_prueba)

#.insert

# lista_prueba.insert(1, 200)
# print(lista_prueba)

#extend

# lista_prueba.extend([50,100,200, 'Josh'])
# print(lista_prueba)

"""List_methods_remove"""

# segunda_lista=[2,4,6,8,6]
# print(segunda_lista)

#.pop

# segunda_lista.pop(1)
# print(segunda_lista)

#remove (puede eliminar el elemento)

# segunda_lista.remove(6)
# print(segunda_lista)

#clear 

# segunda_lista.clear()
# print(segunda_lista)

"""List_methods_search"""

# numbers_list = [1, 2, 3, 4, 5,2]
# print(numbers_list)

# index
# print(numbers_list.index(3, 0, 3))

# in
# print( 2 in numbers_list)

# names=["manzana", "papa", "pera", 'sandia']

# busqueda='sandia'
# message=f"existe en la lista" if busqueda in names else f"no se encuentra"
# print(message)



# True o False

#count 
# print(numbers_list.count(0))

#hace el conteo de cuantas veces aparece l numero que nosotros queramos

"""Others"""

range
numbers=list(range(100))#con el metoo list itera cada uno de los valores

print(numbers)


sentence=''.join(['VAMOS POR EL 100','2','DESDE EL JOIN'])
print(sentence)

total=sum(numbers)
mayor=max(numbers)
menor=min(numbers)
elements=len(numbers)
print(total,mayor,menor,elements)


################## Ejemplo diccionarios ##################

# """Keys"""

# user={
#     "Modelo":"Mazda",
#     "Amno":2012,
#     "Transmicion":"Automatica"
# }

# user["Amno"]=2015
# print(user)


"""Dictionar_methods_search"""

# placa_prueba={
#     "name": "Josh",
#     "age": 20,
#     "text": "hi",
#     "list": [1,2,3]
# }

# .get() -------- atrae un solo  valor


# print(placa_prueba.get('name'))

#in  --- solo busca los valores en las kes

# print('name'in placa_prueba)

#con esta funcion ahora si busca entro del apartado de valores y no solo de las keys


# print('Josh' in placa_prueba.values)

#aqui buscara dentro del apartado de key y al no encontrarla lanzara un false

# print('Josh' in placa_prueba.keys)

# .item --- atrae un resumen el diccionario

# print(placa_prueba.items)

"""Dictionar_methods_remove and adding"""

# placa_prueba={
#     "name": "Josh",
#     "age": 20,
#     "text": "hi",
#     "list": [1,2,3]
# }

# .copy() ----- puede servir para alterar ese diccionario sin alterar el original

# placa_prueba_copy=placa_prueba.copy()

# print(placa_prueba)

"""print(placa_prueba_copy) """ 

# .pop() ----- no funciona como las listas aqui tenemos que audarlo dandole la llave

# placa_prueba.pop('age')

# .popitem() ---- poco comun de ver  elimina el ultimo item del diccionario

# .upate ----- aztualiza un valor

# placa_prueba.update({'name': 'padilla'})

# .append() 

# placa_prueba['skills']=placa_prueba.get('skills',[]) # si no existe creara una lista vacia
# placa_prueba['skills'].append('python')

# print(placa_prueba)