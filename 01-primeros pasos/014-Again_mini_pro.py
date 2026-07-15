
name=input("Ingresa tu nombre completo: ")
age=input("Ingresa tu amno de nacimiento: ")
password=input("Ingresa tu contrasena: ")

age_2050=2050-int(age)

encryption_password=len(password)

card=f"""
NAME : {name}
AGE_2050: {age_2050}
PASSWOR: {encryption_password * "*"}
"""

print(card)
