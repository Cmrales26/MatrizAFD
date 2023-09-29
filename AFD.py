# a = input ("Ingrese una cadena: ") #INGRESA LA CADENA
# expresion = list(a) #SEPARA LA CADENA EN CARACTERES


# Definir la matriz
# Crear una matriz
matriz = [
    [' ','a', 'b', 'c'],
    ['A', 'A', 'A', 'B'],
    ['B', 'C', 'C', '0'],
    ['C', 'C', 'C', '0']
]

EstadosAceptacion = ['C']

# Definir las variables columna y fila
Resultante = "A"
Expresion = "acba"

for a in range(len(Expresion)):
# Encontrar el índice de la fila
    for i in range(len(matriz)):
        if matriz[i][0] == Resultante[-1]:
            fila_index = i
            break

# Encontrar el índice de la columna
    for j in range(len(matriz[0])):
        fila = list(Expresion[a])
        if matriz[0][j] == "".join(fila):
            columna_index = j
            break

# Verificar si se encontraron los índices y obtener el valor
    if fila_index is not None and columna_index is not None:
        valor = matriz[fila_index][columna_index]
        Resultante = Resultante+valor
    else:
        print("No se encontró la fila o columna especificada.")


if Resultante[-1] in EstadosAceptacion:
    print(f"El recorrido del grafo fue:{Resultante} por lo que la Expresión es *ACEPTADA*")
else:
    print(f"El recorrido del grafo fue:{Resultante} por lo que la Expresión es *RECHAZADA*")