# matriz = [
#     [' ','a', 'b', 'c'],
#     ['A', 'A', 'A', 'B'],
#     ['B', 'C', 'C', '0'],
#     ['C', 'C', 'C', '0']
# ]


matriz = [
    [' ','a','b','c','d','e','f',':'],
    ['A','B','C','D','E','-','-','-'],
    ['B','F','c','-','-','-','-','G'],
    ['C','-','-','-','-','H','-','G'],
    ['D','-','-','-','H','-','-','G'],
    ['E','-','-','-','-','-','-','I'],
    ['F','-','-','-','-','-','-','G'],
    ['G','J','-','-','-','-','K','-'],
    ['H','-','-','-','-','-','L','-'],
    ['I','L','-','-','-','-','M','-'],
    ['J','N','O','-','-','-','-','-'],
    ['K','-','-','-','-','P','-','-'],
    ['L','Q','R','-','-','-','-','-'],
    ['M','-','-','-','-','-','-','-'],
    ['N','-','-','-','-','P','-','-'],
    ['O','-','-','-','-','P','-','-'],
    ['P','-','-','-','-','-','-','-'],
    ['Q','-','-','-','-','-','-','-'],
    ['R','-','-','-','-','-','-','-']
]



def recorrido(Expresion):

    EstadosAceptacion = ['C','D','E','H','K','M','N','O','P','Q','R'] ; Resultante = "A"

    if len(Expresion) == 0:
        print("Ingrese Una expresión")
        return

    if Expresion.find(" ") != -1 :
        print("La expresión no puede contener espacios vacíos")
        return

    
    for a in range(len(Expresion)):
        fila_index = None; columna_index = None;

    #! VALIDACIONES
        empytchek = Resultante[-1]
        if empytchek =='0' or empytchek == '-' or empytchek == ' ':
            print(f"El recorrido del grafo fue:{Resultante} por lo que la Expresión es *RECHAZADA*")
            return
        
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
            else:
                columna_index = None

        # Verificar si se encontraron los índices y obtener el valor
        if fila_index is not None and columna_index is not None:
            valor = matriz[fila_index][columna_index]
            Resultante = Resultante + valor
        else:
            print("No se encontró la fila o columna especificada.")
            return

    if Resultante[-1] in EstadosAceptacion:
        print(f"El recorrido del grafo fue:{Resultante} por lo que la Expresión es *ACEPTADA*")
    else:
        print(f"El recorrido del grafo fue:{Resultante} por lo que la Expresión es *RECHAZADA*")


recorrido(input("Ingrese su expresión Regular: "))