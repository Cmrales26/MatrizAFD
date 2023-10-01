# matriz = [
#     [' ','a', 'b', 'c'],
#     ['A', 'A', 'A', 'B'],
#     ['B', 'C', 'C', '0'],
#     ['C', 'C', 'C', '0']
# ]


# matriz = [
#     [' ','a','b','c','d','e','f',':'],
#     ['A','B','C','D','E','-','-','-'],
#     ['B','F','c','-','-','-','-','G'],
#     ['C','-','-','-','-','H','-','G'],
#     ['D','-','-','-','-','H','-','G'],
#     ['E','-','-','-','-','-','-','I'],
#     ['F','-','-','-','-','-','-','G'],
#     ['G','J','-','-','-','-','K','-'],
#     ['H','-','-','-','-','-','L','-'],
#     ['I','L','-','-','-','-','M','-'],
#     ['J','N','O','-','-','-','-','-'],
#     ['K','-','-','-','-','P','-','-'],
#     ['L','Q','R','-','-','-','-','-'],
#     ['M','-','-','-','-','-','-','-'],
#     ['N','-','-','-','-','P','-','-'],
#     ['O','-','-','-','-','P','-','-'],
#     ['P','-','-','-','-','-','-','-'],
#     ['Q','-','-','-','-','-','-','-'],
#     ['R','-','-','-','-','-','-','-']
# ]
    

matriz = [
    [' ', 'a', 'b', 'c', 'd', 'e', 'f', ':'],
    ['A', 'B', 'C', 'C', 'D', '-', '-', '-'],
    ['B', 'E', 'C', '-', '-', '-', '-', 'F'],
    ['C', '-', '-', '-', '-', 'G', '-', 'F'],
    ['D', '-', '-', '-', '-', '-', '-', 'H'],
    ['E', '-', '-', '-', '-', '-', '-', 'F'],
    ['F', 'I', '-', '-', '-', '-', 'J', '-'],
    ['G', '-', '-', '-', '-', '-', '-', '-'],
    ['H', 'K', '-', '-', '-', '-', 'G', '-'],
    ['I', 'J', 'J', '-', '-', '-', '-', '-'],
    ['J', '-', '-', '-', '-', 'G', '-', '-'],
    ['K', 'G', 'G', '-', '-', '-', '-', '-']
]


def recorrido(Expresion):

    EstadosAceptacion = ['C','D','G', 'J'] ; Resultante = "A"
    # EstadosAceptacion = ['C','D','E','H','K','M','N','O','P','Q','R'] ; Resultante = "A"

    if len(Expresion) == 0:
        print("Vació no es una cadena aceptada")
        return

    if Expresion.find(" ") != -1 :
        print("La cadena no puede contener espacios vacíos")
        return

    
    for a in range(len(Expresion)):
        fila_index = None; columna_index = None;

    #! VALIDACIONES
        empytchek = Resultante[-1]
        if empytchek =='0' or empytchek == '-' or empytchek == ' ':
            print(f"El recorrido del grafo fue:{Resultante} por lo que la Cadena es *RECHAZADA*")
            return
        
        for i in range(len(matriz)):
            if matriz[i][0] == Resultante[-1]:
                fila_index = i
                break
            
        for j in range(len(matriz[0])):
            fila = list(Expresion[a])
            if matriz[0][j] == "".join(fila):
                columna_index = j
                break
            else:
                columna_index = None

        if fila_index is not None and columna_index is not None:
            valor = matriz[fila_index][columna_index]
            Resultante = Resultante + valor
        else:
            print("No se encontró la fila o columna especificada.")
            return

    if Resultante[-1] in EstadosAceptacion:
        print(f"Para la cadena {Expresion}, el recorrido del grafo fue:{Resultante} por lo que la Cadena es *ACEPTADA*")
    else:
        print(f"Para la cadena {Expresion}, el recorrido del grafo fue:{Resultante} por lo que la Cadena es *RECHAZADA*")


recorrido(input("Ingrese una cadena: "))