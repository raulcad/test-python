# import coche
from classes.coche import Coche, CocheElectrico

# Ejecución: python3 main.py

'''
Comentario
de varias líneas
'''
name = "Raúl"
# years = 45
years = int(input("¿Cuántos años tienes? "))
# Otros conversores: float(), str(), bool()
print(f"¡Hola, {name}! Tienes {years} años.")
if years < 18:
    print("Eres menor de edad.")
elif years == 18:
    print("¡Acabas de cumplir la mayoría de edad!")
else:
    print("Eres mayor de edad.")

languages = ["Basic", "Pascal", "C", "Java", "HTML", "JavaScript", "PHP"]
del languages[0]
languages[2] = "Eiffel"
languages.insert(3, "Java")
languages.append("Python")
print(languages[-1]) # -1 = Python, -2 = PHP, -3 = JavaScript, ...
print(languages)

# Una tupla es como una colección de datos, pero no se pueden modificar
tupla = ("Raúl", 45)
print(f"{tupla[0]} tiene {tupla[1]} años.")

# Un diccionario es una colección de datos que se accede por una clave
person = {"name": "Raúl", "years": 45}
person["surname"] = "Casillas"
print(len(person))
print(f"{person['name']} {person['surname']} tiene {person['years']} años.")

numeros = [1, 2, 3, 4, 5]
print("For array:")
for num in numeros:
    print(num)

rango = range(1, 6)
print("For range:")
for num in rango:
    print(num)

table = int(input("¿Qué tabla de multiplicar quieres ver? "))
count = 0
while count <= 10:
    print(f"{table} x {count} = {table * count}")
    count += 1

# coche1 = coche.Coche("Ford", "Focus")
coche1 = Coche("Ford", "Focus")
print(coche1)

# coche2 = coche.CocheElectrico("Tesla", "Model S", 100)
coche2 = CocheElectrico("Tesla", "Model S", 100)
print(coche2)

