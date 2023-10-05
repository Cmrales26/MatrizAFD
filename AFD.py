a = ['0'] #0
b = [str(i) for i in range(1, 10)] # Hora Minutos
c = ['10', '11'] # Horas
d = [str(i) for i in range(12, 24)] # Horas
e = ['T', 't'] #Letra
f = [str(i) for i in range(10, 60)] # Minutos
dp = [":"] # :


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
        cadena = cadena + expres[z]
        if ':' in cadena: 
            if expres[z] in dp:
                cadenaletras += ':'
            elif expres[z] in a:
                cadenaletras += 'a'
            elif expres[z] in b:
                cadenaletras += 'b'
            elif expres[z] in f:
                cadenaletras += 'f'
            elif expres[z] in e:
                cadenaletras += 'e'
            else:
                cadenaletras += '-'
        else:
            if expres[z] in a:
                cadenaletras += 'a'
            elif expres[z] in b:
                cadenaletras += 'b'
            elif expres[z] in c:
                cadenaletras += 'c'
            elif expres[z] in d:
                cadenaletras += 'd'
            elif expres[z] in e:
                cadenaletras += 'e'
            else:
                cadenaletras += '-'

        
    print(cadena)
    print(cadenaletras)
    recorrido(cadenaletras,expression)

def recorrido(cadena,hora):

    EstadosAceptacion = ['C','D','G', 'J'] ; Resultante = "A"
    # EstadosAceptacion = ['C','D','E','H','K','M','N','O','P','Q','R'] ; Resultante = "A"

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
            print(f"El recorrido del grafo fue:{Resultante} por lo que la Cadena es *RECHAZADA*")
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
            print("No se encontró la fila o columna especificada.")
            return

    if Resultante[-1] in EstadosAceptacion:
        print(f"Para la hora: {hora}, el recorrido del grafo fue:{Resultante} por lo que la Cadena es *ACEPTADA*")
    else:
        print(f"Para la hora: {hora}, el recorrido del grafo fue:{Resultante} por lo que la Cadena es *RECHAZADA*")


separar(input("Ingrese una hora: "))