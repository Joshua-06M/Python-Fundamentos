
#son metoos que nos ayudan a ordenar

letters=['a','t','c','b','c']
print(letters)
"""letters.sort()
print(letters)"""

new_letters=sorted(letters) #asi se crea una nueva lista

print(new_letters)

#Nueva lista sin sorted

new_letters=letters[:] #copea la lista 
new_letters.sort()

#copy

"""new_letters=letters.copy
new_letters.sort()"""

#reverse voltea la lista

letters.reverse()
print(letters)