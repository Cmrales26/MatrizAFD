# Documentación del Código

Este código implementa una máquina de estados finitos para procesar cadenas de caracteres.

## Estructura del Código
El código consta de una matriz que representa la tabla de transiciones de la máquina de estados y una función `recorrido` que procesa una cadena de entrada a través de la máquina.

### Matriz

La matriz es una representación bidimensional de la tabla de transiciones de la máquina de estados. Cada fila corresponde a un estado y cada columna a un símbolo del alfabeto. El valor en una celda específica representa el estado al que se transita cuando se está en el estado correspondiente a la fila y se lee el símbolo correspondiente a la columna.

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

###Obtener la Columna
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
Para usar este código, simplemente llama a la función `recorrido` con una cadena como argumento. Por ejemplo: `aa:f`.

#Desarrollado por
- [Nelson Morales](https://github.com/Cmrales26)
- [Diana Vidal](https://github.com/Dicavimer)
- [Sharith Blanco](https://github.com/Sblanco16)
- [Andrea Dominguez](https://github.com/AndyDA1810)
