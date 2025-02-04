
set_a = {1,2,3}
set_b = {3,4,5}

# Union: Genera un nuevo set pero sin valores duplicados
union_sets = set_a.union(set_b)
print("Resultado de union de set_a y set_b =",union_sets)

# Intersección: son los valores comunes entre ambos sets
interseccion_sets = set_a.intersection(set_b)
print("Los elementos comununes entre set_a y set_b son = ", interseccion_sets)

# Diferencia: genera un nuevo setr con los elementos que esta en set_a pero no en set_b
diferencia_sets = set_a.difference(set_b)
print("Los valores que existen en set_a pero no en set_b son = ", diferencia_sets)

#Subconjunto : validar que los elemento de set_a existan en set_b
print("Los valores de set_a existen en set_b? ",set_a.issubset(set_b))

#Superconjuntos: validar si el set_a contiene todos los elementos de set_b
print("Los valores en set_a son los mismos o contiene los valores de set_b?", set_a.issuperset(set_b))