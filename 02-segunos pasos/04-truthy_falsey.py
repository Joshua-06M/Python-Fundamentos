#Los truthy son todos los valores que sean positivos o diferentes de 0
#Los falsey son todos los valores que sean 0 o valores vacios

#Truthy
print(bool(1))
print(bool(1.1))
print(bool(-1))
print(bool(1j))
print(bool("hola"))
print(bool({1, 2, 3})) #sets
print(bool([1,2,3])) #lista

#Falsey
print(bool(0))
print(bool(0.0))
print(bool(0j))
print(bool(""))
print(bool({}))#set
print(bool([]))#lista
print(bool())#tupla
