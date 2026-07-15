#es un operador que ayuda a evaluar una condicion

#and = y es su traducccion "evalua si una condicion son verdaderas o todas las operaciones"

#AND(Si todos los operadores son verdaderos)
print(True and True)
print(True and False)
print(False and True)
print(False and False)

#OR(Almenos uno debe de ser verdadero)
print(True or True)
print(True or False)
print(False or True)
print(False or False)

#NOT(Su funcion es negar)
print(not True)
print(not False)

#ejemplos

#AND
age = 20
licencia=True

if age>=18 and licencia:
    print("Puedes manejar ")

#OR
is_student=False
membership=True

if is_student or membership:
    print("Obtiene un descuento especial ")

#NOT
is_admin=False

if not is_admin:
    print("accesos denegado ")
