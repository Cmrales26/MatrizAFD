# Documentación del Código

Este código implementa una máquina de estados finitos para procesar cadenas de caracteres.

## Estructura del Código
El código consta de una matriz que representa la tabla de transiciones de la máquina de estados, una función `Separar` que convierte las horas en una cadena de letras entendibles por la matriz de transición y una función `Recorrer` que procesa una cadena de entrada a través de la máquina.

### Matriz
La matriz es una representación bidimensional de la tabla de transiciones de la máquina de estados. Cada fila corresponde a un estado y cada columna a un símbolo del alfabeto. El valor en una celda específica representa el estado al que se transita cuando se está en el estado correspondiente a la fila y se lee el símbolo correspondiente a la columna.

### Función `Separar`
```python
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
```


Este fragmento de código Python define una función llamada `separar` que toma una cadena de texto `expression` como argumento. La función tiene como objetivo dividir la cadena en elementos individuales, manteniendo los dígitos consecutivos como un solo elemento en la lista resultante.

En esta se recorre la cadena (Hora) ingresada el # de veces que de la longitud de la cadena, esto con el objetivo de poder separar en partes la individuales la cadena, la cual se almacenara es la variable `expres`

####En esta inicialmente se valida que:  
Sí, la expresión en la posición i son dos dígitos sin contar el **0** inicial, este se almacene como un solo valor. Por ejemplo, en una entrada: **15:40** el vector `expres` quedaría de la siguiente manera: `['15',':',''40]` y en caso de ser por ejemplo **04:05** el vector `expres` quedaría de la siguiente manera: `['0','4',':','0','5']`, esto con el objetivo se valida el **0** como una definición básica separada. Esto lo hace validando siempre que: 

- `Expression[i] != '0' ` el dato de la expresión sea diferente de 0
- `i + 1 < len(expression)` Que no sea la última posición
- ` expression[i + 1].isdigit()` El siguiente valor de `i` sea también un dígito

En caso de que esto se cumpla, se almacenará como el primer caso mencionado anteriormente.

### Converción de horas a cadenas letras
Para convertir una cadena de digitos a letras inicialmente se realizó dos variables que almacenan el valor que se esta evaluando como el valor resultantes, estas son`cadena` y `cadenaletras`respectivamente. 

```python
for z in range(len(expres)):
	cadena += expres[z]
		if ":" in cadena:
			letra = DiccionarioMinutos.get(expres[z], '-')
			cadenaletras += letra
		else:
			letra = DiccionarioHoras.get(expres[z], '-')
			cadenaletras += letra
```
Para el correcto funcionamiento de esta porción de código se generaro 2 Diccionarios de la siguente manera: 
```python
DiccionarioHoras = {
    '0': 'a',
    **{str(i): 'b' for i in range(1, 10)},  # Hora Minutos
    **{str(i): 'c' for i in range(10, 12)},  # Horas
    **{str(i): 'd' for i in range(12, 24)},  # Horas
    **{'T': 'e', 't': 'e'},  # Letra
}

DiccionarioMinutos = {
    '0': 'a',
    **{str(i): 'b' for i in range(1, 10)},  # Hora Minutos
    **{'T': 'e', 't': 'e'},  # Letra
    **{str(i): 'f' for i in range(10, 60)},   # Minutos
    ':': ':'  # :
}
```

Dentro del bucle`for`, se itera sobre cada carácter de la cadena de texto`expres`. Se agrega cada carácter a la variable`cadena`. Si el carácter actual es `':'`, se utiliza el diccionario`DiccionarioMinutos` para obtener la letra correspondiente según el carácter. De lo contrario, se utiliza el diccionario`DiccionarioHoras`. La letra obtenida se agrega a la variable`cadenaletras`.

Una vez se tiene la nueva cadena de letras se realiza la función `recorrido`. 


### Función `recorrido`
La función `recorrido` toma una cadena como entrada y procesa cada carácter de la cadena a través de la máquina de estados. Comienza en el estado inicial **A** y para cada carácter en la cadena, realiza una transición al estado correspondiente en la matriz.

### Obtener la Fila
```python
 for i in range(len(matriz)):
 	if matriz[i][0] == Resultante[-1]:
		fila_index = i
    break
```
Este ciclo recorre la la primera columna buscando el valor del ultimo caracter de la variable `Resultante`, la cual lamacena el recorrido. Una vez lo encuentre almacena su posición en `fila_index`.

### Obtener la Columna
```python
for j in range(len(matriz[0])):
    fila = list(Expresion[a])
    if matriz[0][j] == "".join(fila):
        columna_index = j
        break
    else:
        columna_index = None
```
`Fila = List(Expresion[A])` Esta línea de código descompone la cadena Expresion en un vector con cada carácter de la cadena separados por `,`.  Una vez hecho esto, toma el valor de `a` en el vector y lo almacena en la variable `fila`. por ejemplo si el valor de a es ***3*** y la cadena es ***aa:f*** `fila = f `

El ciclo busca la posición del valor de fila en la primera fila y almacena su valor en la varible `columna_index`, en caso de no ser encontrada almacena su valor será `None`

#### Almacener el nuevo estado
```python
valor = matriz[fila_index][columna_index]
	Resultante = Resultante + valor
```
Una vez con los valores de `fila_index` y `columna_index` se procede a hallar el valor que esta almacenado en esa posición de la matriz, este valor será concatenado a `Resultante` permitiendo de este modo volver a realizar el recorido, hasta que el largo de la cadena sera terminado, o hasta que encuentre una transición vacia. 

Si al final del procesamiento, la máquina se encuentra que la ultima posición de resultante es uno de los estados de aceptación, la cadena será aceptada, en cualquier otro caso esta será rechazada.

## Uso
Para usar este código, simplemente llama a la función `separar` con una cadena como argumento. Por ejemplo: `20:15`, esta será tranformada en `d:f` y esta será evaluada por la función `Recorrer`.

# Desarrollado por
- [Nelson Morales](https://github.com/Cmrales26)
- [Diana Vidal](https://github.com/Dicavimer)
- [Sharith Blanco](https://github.com/Sblanco16)
- [Andrea Dominguez](https://github.com/AndyDA1810)
