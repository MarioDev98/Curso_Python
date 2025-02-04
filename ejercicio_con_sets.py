matematicas = {"Ana", "Pedro", "Luis", "Sofía"}
fisica = {"Sofía", "Luis", "María"}

#Encontrar los alumnos que estan en matematicas pero no en fisica
solo_en_matematicas = matematicas.difference(fisica)
print("Estos alumnos solo esta en matematicas pero no en fisica = ",solo_en_matematicas)

#Encontrar los alumnos que estan solo en una sola materia pero nunca en las dos
solo_en_una_materia= matematicas.symmetric_difference(fisica)
print("Esota alumnos solo estan en una materia pero no em ambas = ",solo_en_una_materia)

#Añadir al grupo de fisica a el alumno Mario
fisica.add("Mario")
print("Se agrego a Mario al grupo de fisica = ", fisica)

# -------------------------------------
set_1 = {1, 2, 3, 4, 5, 5, 6}
set_2 = {4, 5, 6, 7, 8, 8, 9}


# Tienes dos sets de números. Encuentra los elementos únicos que aparecen en ambos sets combinados - Union.
elementos_unicos_union = set_1.union(set_2)
print("Elementos unicos en ambos set unidos o combinados = ", elementos_unicos_union)