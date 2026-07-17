#se pueen tener diferentes tipos de datos

placa_prueba={
    "name": "Josh",
    "age": 20,
    "text": "hi",
    "list": [1,2,3]
}

# .get() -------- atrae un solo  valor


print(placa_prueba.get('name'))

#in  --- solo busca los valores en las kes
print('name'in placa_prueba)
#con esta funcion ahora si busca entro del apartado de valores y no solo de las keys

print('Josh' in placa_prueba.values)

#aqui buscara dentro del apartado de key y al no encontrarla lanzara un false
print('Josh' in placa_prueba.keys)

# .item --- atrae un resumen el diccionario

print(placa_prueba.items)