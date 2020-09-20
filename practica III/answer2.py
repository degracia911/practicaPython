def esta_en_rango(rango, numero): 
    return numero in range(*rango)

print(esta_en_rango([1, 10], 3 ))
