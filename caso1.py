import random

def mini_max(lst, x=0):
    if x == len(lst):
        return float('inf'), float('-inf') 
    else:
        min_r, max_r = mini_max(lst, x+1)
        val = lst[x]
        
        if val % 3 == 0:
            return min(val, min_r), max(val, max_r)
        else:
            return min_r, max_r

n = int(input("Digitar tamaño de arreglo:  "))
arreglo = [random.randint(10, 9999) for _ in range(n)]
print(f"Arreglo: {arreglo}")

min, max = mini_max(arreglo)

if min == float('inf'):
    print("Sin múltiplos de 3 en el arreglo. Inténtelo de nuevo.")
else:
    promedio = (min + max) / 2
    print(f"Resultado = ({max}+{min})/2 = {promedio}")
