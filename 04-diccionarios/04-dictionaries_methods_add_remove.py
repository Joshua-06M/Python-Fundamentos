
placa_prueba={
    "name": "Josh",
    "age": 20,
    "text": "hi",
    "list": [1,2,3]
}

# .copy() ----- puede servir para alterar ese diccionario sin alterar el original

placa_prueba_copy=placa_prueba.copy()

print(placa_prueba)
"""print(placa_prueba_copy) """ 

# .pop() ----- no funciona como las listas aqui tenemos que audarlo dandole la llave

placa_prueba.pop('age')

# .popitem() ---- poco comun de ver  elimina el ultimo item del diccionario

# .upate ----- aztualiza un valor
placa_prueba.update({'name': 'padilla'})

# .append() 
placa_prueba['skills']=placa_prueba.get('skills',[]) # si no existe creara una lista vacia
placa_prueba['skills'].append('python')

print(placa_prueba)
