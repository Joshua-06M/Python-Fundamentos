
shopping_car=['leche',
                'huevos',
                'avena',
                 'platano']

new_list=shopping_car[0:3]
print(new_list) #list slicing o corte
print(shopping_car)

new_list[0]='dinero'

print(new_list)

#ejercicio
copy_list=shopping_car[:] # se crea una lista nueva
copy_list[0]='Tenis'
print(copy_list)

