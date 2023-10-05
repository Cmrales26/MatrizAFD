DiccionarioHoras = {
    '0': 'a',
    **{str(i): 'b' for i in range(1, 10)},  # Hora Minutos
    **{str(i): 'c' for i in range(10, 12)},  # Horas
    **{str(i): 'd' for i in range(12, 24)},  # Horas
    **{'T': 'e', 't': 'e'},  # Letra
}

# MINUTOS

DiccionarioMinutos = {
    '0': 'a',
    **{str(i): 'b' for i in range(1, 10)},  # Hora Minutos
    **{'T': 'e', 't': 'e'},  # Letra
    **{str(i): 'f' for i in range(10, 60)},   # Minutos
    ':': ':'  # :
}


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



def separar(expression):
    expres = [] 
    i = 0
    while i < len(expression):
        if expression[i].isdigit():
            if expression[i] != '0' and i + 1 < len(expression) and expression[i + 1].isdigit():
                expres.append(expression[i] + expression[i + 1])
                i += 2
            else:
                expres.append(expression[i])
                i += 1
        else:
            expres.append(expression[i])
            i += 1

    cadena = ''; cadenaletras = ''
    
    for z in range(len(expres)):
        cadena += expres[z]
        if ":" in cadena:
            letra = DiccionarioMinutos.get(expres[z], '-')
            cadenaletras += letra
        else:
            letra = DiccionarioHoras.get(expres[z], '-')
            cadenaletras += letra

    recorrido(cadenaletras,expression)

def recorrido(cadena,hora):

    EstadosAceptacion = ['C','D','G', 'J'] ; Resultante = "A"

    if len(cadena) == 0:
        print("Vació no es una cadena aceptada")
        return

    if cadena.find(" ") != -1 :
        print("La cadena no puede contener espacios vacíos")
        return

    
    for a in range(len(cadena)):
        fila_index = None; columna_index = None;

    #! VALIDACIONES
        empytchek = Resultante[-1]
        if empytchek =='0' or empytchek == '-' or empytchek == ' ':
            print(f"Para la hora: {hora}, El recorrido del grafo fue:{Resultante} por lo que la Cadena es *RECHAZADA*")
            return
        
        for i in range(len(matriz)):
            if matriz[i][0] == Resultante[-1]:
                fila_index = i
                break
            
        for j in range(len(matriz[0])):
            fila = list(cadena[a])
            if matriz[0][j] == "".join(fila):
                columna_index = j
                break
            else:
                columna_index = None

        if fila_index is not None and columna_index is not None:
            valor = matriz[fila_index][columna_index]
            Resultante = Resultante + valor
        else:
            print(f"Para la hora: {hora}, El recorrido del grafo fue:{Resultante} por lo que la Cadena es *RECHAZADA*")
            return

    if Resultante[-1] in EstadosAceptacion:
        print(f"Para la hora: {hora}, el recorrido del grafo fue:{Resultante} por lo que la Cadena es *ACEPTADA*")
    else:
        print(f"Para la hora: {hora}, el recorrido del grafo fue:{Resultante} por lo que la Cadena es *RECHAZADA*")


separar(input("Ingrese una hora: "))


# tesing = ["00:00","23:50","00:75","24:00","9:30","00:48","0:30",":40","00:00t","9:40t","22:40t","15","8t","9", "0t"]



# for valor in tesing:
#     result = separar(valor)