# Criterios de Evaluación: Proyecto 1 — Python Básico (Store 1)

## Objetivo

Limpiar y preparar datos de clientes para futuros análisis de negocio, aplicando técnicas fundamentales de Python: manipulación de strings, conversión de tipos, manejo de errores y operaciones con listas.

**Requisitos previos**: Conocimientos básicos de sintaxis Python, variables y tipos de datos.

**Competencias que desarrollarás**: Manipulación de cadenas (strip, replace, split), conversión de tipos (int, float), manejo de excepciones (try/except), operaciones con listas (sort, append, indexación), f-strings, función len()

> **NOTA IMPORTANTE**: Este sprint está estructurado en **pasos secuenciales (Paso 1-9)**. Cada paso introduce un concepto nuevo y debe completarse correctamente antes de avanzar al siguiente. La evaluación se basa en la correcta ejecución de cada paso con su salida esperada.

<details>
<summary>Task Statement</summary>

## Descripción del proyecto

Store 1 está revisando la calidad y coherencia de sus datos de clientes. Como parte del equipo de análisis, tu tarea es limpiar y preparar estos datos para que puedan ser utilizados en futuros análisis de negocio orientados a identificar clientes leales, analizar ingresos por categoría y buscar oportunidades de marketing.

## Instrucciones del proyecto

1. **Limpieza de nombres de usuario:**
   - Eliminar espacios innecesarios al inicio y final
   - Reemplazar guiones bajos por espacios
   - Separar nombre y apellido en una lista

2. **Conversión de tipos de datos:**
   - Convertir edades de float a int
   - Manejar errores cuando la conversión no es posible

3. **Operaciones con listas:**
   - Ordenar registros por ID de usuario
   - Calcular suma de gastos por categoría
   - Contar número de clientes

4. **Formateo de cadenas:**
   - Crear resúmenes de clientes usando f-strings
   - Mostrar información formateada

## Descripción de los datos

La tienda Store 1 almacena información de sus usuarios en listas anidadas. Cada sublista contiene:

- `user_id`: identificador único
- `user_name`: nombre y apellido en un solo string
- `user_age`: edad
- `fav_categories`: categorías favoritas de compra (mayúsculas)
- `total_spendings`: montos correspondientes a cada categoría

Ejemplo:

```python
usuarios = [
    ['32415', ' mike_reed ', 32.0, ['ELECTRONICS', 'SPORT', 'BOOKS'], [894, 213, 173]],
    ...
]
```

</details>

## Glosario de Términos Técnicos

**strip()**: Método de cadena que elimina espacios en blanco (u otros caracteres especificados) del inicio y final de una cadena.

**replace(old, new)**: Método de cadena que reemplaza todas las ocurrencias de una subcadena por otra.

**split()**: Método de cadena que divide una cadena en una lista de subcadenas, usando un separador (espacio por defecto).

**int()**: Función que convierte un valor a tipo entero. Genera ValueError si el valor no puede convertirse.

**try/except**: Estructura de control para manejar excepciones (errores) sin interrumpir la ejecución del programa.

**sort()**: Método de lista que ordena los elementos in-place (modifica la lista original) en orden ascendente.

**append()**: Método de lista que agrega un elemento al final de la lista.

**f-string**: Cadena formateada (f"...") que permite insertar expresiones Python dentro de llaves {}.

**len()**: Función que devuelve la cantidad de elementos en una secuencia (lista, cadena, etc.).

**Indexación**: Acceso a elementos individuales de una secuencia usando corchetes y un índice numérico (comenzando en 0).

---

## Rúbrica de Evaluación - Checklist para Revisores

### BÁSICO (Todos los Pasos - OBLIGATORIOS)

#### Paso 1: Limpieza de nombre con strip() y replace()
- [ ] **[OBLIGATORIO]** Usa `strip()` para eliminar espacios al inicio y final
- [ ] **[OBLIGATORIO]** Usa `replace("_", " ")` para sustituir guiones bajos por espacios
- [ ] **[OBLIGATORIO]** Muestra el resultado con `print()`
- [ ] **[OBLIGATORIO]** La salida es exactamente: `mike reed`

**Código correcto:**
```python
usuario_nombre = ' mike_reed '

# 1. Limpia el dato eliminando los espacios innecesarios
usuario_nombre = usuario_nombre.strip()

# 2. Reemplaza el guion bajo por un espacio
usuario_nombre = usuario_nombre.replace("_", " ")

print(usuario_nombre)
```

**Salida esperada:**
```
mike reed
```

---

#### Paso 2: Separación de nombre con split()
- [ ] **[OBLIGATORIO]** Usa `split()` para dividir el nombre en una lista
- [ ] **[OBLIGATORIO]** Guarda el resultado en una variable
- [ ] **[OBLIGATORIO]** Muestra el resultado con `print()`
- [ ] **[OBLIGATORIO]** La salida es exactamente: `['mike', 'reed']`

**Código correcto:**
```python
usuario_nombre = 'mike reed'

# 1. Divide el usuario en dos partes: nombre y apellido
usuario_sep = usuario_nombre.split()

print(usuario_sep)
```

**Salida esperada:**
```
['mike', 'reed']
```

---

#### Paso 3: Conversión de tipo con int()
- [ ] **[OBLIGATORIO]** Usa `int()` para convertir edad de float a entero
- [ ] **[OBLIGATORIO]** Muestra el resultado con `print()`
- [ ] **[OBLIGATORIO]** La salida es exactamente: `32`

**Código correcto:**
```python
usuario_edad = 32.0

# 1. Convierte el valor al tipo de dato correcto
usuario_edad = int(usuario_edad)

print(usuario_edad)
```

**Salida esperada:**
```
32
```

---

#### Paso 4: Manejo de excepciones con try/except
- [ ] **[OBLIGATORIO]** Implementa estructura `try/except`
- [ ] **[OBLIGATORIO]** Intenta convertir a entero dentro del `try`
- [ ] **[OBLIGATORIO]** Muestra mensaje de error en el `except`
- [ ] **[OBLIGATORIO]** La salida es exactamente: `Proporcione su edad como un valor numérico.`

**Código correcto:**
```python
usuario_edad = 'treinta y dos'

# 1. Intenta convertir usuario_edad a entero
# 2. Si falla, muestra el mensaje correspondiente
try:
    usuario_edad_int = int(usuario_edad)
except:
    print('Proporcione su edad como un valor numérico.')
```

**Salida esperada:**
```
Proporcione su edad como un valor numérico.
```

---

#### Paso 5: Ordenamiento de lista con sort()
- [ ] **[OBLIGATORIO]** Usa `sort()` para ordenar la lista de usuarios
- [ ] **[OBLIGATORIO]** La lista queda ordenada por ID (primer elemento) en orden ascendente
- [ ] **[OBLIGATORIO]** Muestra el resultado con `print()`
- [ ] **[OBLIGATORIO]** El primer elemento de la lista ordenada tiene ID `'31980'`

> **Nota para revisores**: El método `sort()` en listas anidadas ordena automáticamente por el **primer elemento** de cada sublista. En este caso, el primer elemento es el `user_id` (string). Como todos los IDs tienen la misma longitud (5 dígitos), el ordenamiento lexicográfico coincide con el numérico.
>
> **Verificar que**:
> - El ID `'31980'` aparece primero (era el segundo en la lista original)
> - El ID `'34278'` aparece último
> - Los IDs están en orden: 31980 → 32156 → 32415 → 32761 → 32984 → 33001 → 33767 → 33912 → 34009 → 34278

**Código correcto:**
```python
usuarios = [
    ['32415', ' mike_reed ', 32.0, ['ELECTRÓNICA', 'DEPORTE', 'LIBROS'], [894, 213, 173]],
    ['31980', 'kate morgan', 24.0, ['ROPA', 'LIBROS'], [439, 390]],
    ['32156', ' john doe ', 37.0, ['ELECTRÓNICA', 'HOGAR', 'COMIDA'], [459, 120, 99]],
    ['32761', 'SAMANTHA SMITH', 29.0, ['ROPA', 'ELECTRÓNICA', 'BELLEZA'], [299, 679, 85]],
    ['32984', 'David White', 41.0, ['LIBROS', 'HOGAR', 'DEPORTE'], [234, 329, 243]],
    ['33001', 'emily brown', 26.0, ['BELLEZA', 'HOGAR', 'COMIDA'], [213, 659, 79]],
    ['33767', ' Maria Garcia', 33.0, ['ROPA', 'COMIDA', 'BELLEZA'], [499, 189, 63]],
    ['33912', 'JOSE MARTINEZ', 22.0, ['DEPORTE', 'ELECTRÓNICA', 'HOGAR'], [259, 549, 109]],
    ['34009', 'lisa wilson ', 35.0, ['HOGAR', 'LIBROS', 'ROPA'], [329, 189, 329]],
    ['34278', 'James Lee', 28.0, ['BELLEZA', 'ROPA', 'ELECTRÓNICA'], [189, 299, 579]],
]

# sort() ordena por el primer elemento de cada sublista (user_id)
usuarios.sort()

print(usuarios)
```

**Salida esperada:**
```
[['31980', 'kate morgan', 24.0, ['ROPA', 'LIBROS'], [439, 390]],
 ['32156', ' john doe ', 37.0, ['ELECTRÓNICA', 'HOGAR', 'COMIDA'], [459, 120, 99]],
 ['32415', ' mike_reed ', 32.0, ['ELECTRÓNICA', 'DEPORTE', 'LIBROS'], [894, 213, 173]],
 ['32761', 'SAMANTHA SMITH', 29.0, ['ROPA', 'ELECTRÓNICA', 'BELLEZA'], [299, 679, 85]],
 ['32984', 'David White', 41.0, ['LIBROS', 'HOGAR', 'DEPORTE'], [234, 329, 243]],
 ['33001', 'emily brown', 26.0, ['BELLEZA', 'HOGAR', 'COMIDA'], [213, 659, 79]],
 ['33767', ' Maria Garcia', 33.0, ['ROPA', 'COMIDA', 'BELLEZA'], [499, 189, 63]],
 ['33912', 'JOSE MARTINEZ', 22.0, ['DEPORTE', 'ELECTRÓNICA', 'HOGAR'], [259, 549, 109]],
 ['34009', 'lisa wilson ', 35.0, ['HOGAR', 'LIBROS', 'ROPA'], [329, 189, 329]],
 ['34278', 'James Lee', 28.0, ['BELLEZA', 'ROPA', 'ELECTRÓNICA'], [189, 299, 579]]]
```

---

#### Paso 6: Suma de elementos con indexación
- [ ] **[OBLIGATORIO]** Calcula la suma de los gastos usando indexación
- [ ] **[OBLIGATORIO]** Muestra el resultado con `print()`
- [ ] **[OBLIGATORIO]** La salida es exactamente: `1280`

**Código correcto:**
```python
categorias_fav_low = ['electrónica', 'deporte', 'libros']
gasto_por_categoria = [894, 213, 173]

# 1. Calcula la suma de los gastos del usuario
# Solución básica (esperada en este nivel):
suma_total = gasto_por_categoria[0] + gasto_por_categoria[1] + gasto_por_categoria[2]

# Solución alternativa avanzada (también válida):
# suma_total = sum(gasto_por_categoria)

print(suma_total)
```

**Salida esperada:**
```
1280
```

---

#### Paso 7: f-strings para formateo de cadenas
- [ ] **[OBLIGATORIO]** Usa f-string para crear la cadena formateada
- [ ] **[OBLIGATORIO]** Accede al primer elemento de la lista `usuario_nombre` con indexación
- [ ] **[OBLIGATORIO]** Incluye las variables `usuario_id`, `usuario_nombre[0]` y `usuario_edad`
- [ ] **[OBLIGATORIO]** La salida es exactamente: `El usuario 32415 es mike, quien tiene 32 años.`

**Código correcto:**
```python
usuario_id = '32415'
usuario_nombre = ['mike', 'reed']
usuario_edad = 32

# 1. Crea la cadena de resumen del cliente
usuario_info = f'El usuario {usuario_id} es {usuario_nombre[0]}, quien tiene {usuario_edad} años.'

print(usuario_info)
```

**Salida esperada:**
```
El usuario 32415 es mike, quien tiene 32 años.
```

---

#### Paso 8: Uso de len() con f-strings
- [ ] **[OBLIGATORIO]** Usa `len()` para contar los elementos de la lista
- [ ] **[OBLIGATORIO]** Usa f-string para crear la cadena formateada
- [ ] **[OBLIGATORIO]** La salida es exactamente: `Hemos registrado datos de 10 clientes.`

**Código correcto:**
```python
usuarios = [
    ['32415', ' mike_reed ', 32.0, ['ELECTRÓNICA', 'DEPORTE', 'LIBROS'], [894, 213, 173]],
    ['31980', 'kate morgan', 24.0, ['ROPA', 'LIBROS'], [439, 390]],
    # ... (10 usuarios en total)
]

# 1. Cuenta el número de clientes registrados
usuarios_info = f'Hemos registrado datos de {len(usuarios)} clientes.'

print(usuarios_info)
```

**Salida esperada:**
```
Hemos registrado datos de 10 clientes.
```

---

#### Paso 9: Procesamiento de múltiples usuarios
- [ ] **[OBLIGATORIO]** Procesa correctamente los 3 usuarios de la lista
- [ ] **[OBLIGATORIO]** Aplica `strip()` y `replace('_', ' ')` a cada nombre
- [ ] **[OBLIGATORIO]** Convierte cada edad a entero con `int()`
- [ ] **[OBLIGATORIO]** Separa cada nombre con `split()`
- [ ] **[OBLIGATORIO]** Usa `append()` para agregar cada usuario limpio a `usuarios_limpio`
- [ ] **[OBLIGATORIO]** La lista `usuarios_limpio` tiene la estructura correcta

**Código correcto:**
```python
usuarios = [
    ['32415', ' mike_reed ', 32.0, ['ELECTRÓNICA', 'DEPORTE', 'LIBROS'], [894, 213, 173]],
    ['31980', 'kate morgan', 24.0, ['ROPA', 'LIBROS'], [439, 390]],
    ['32156', ' john doe ', 37.0, ['ELECTRÓNICA', 'HOGAR', 'COMIDA'], [459, 120, 99]],
]

usuarios_limpio = []

# Procesa al primer usuario
usuario_nombre_1 = usuarios[0][1].strip().replace('_', ' ')
usuario_edad_1 = int(usuarios[0][2])
usuario_nombre_1 = usuario_nombre_1.split()
usuarios_limpio.append([usuarios[0][0], usuario_nombre_1, usuario_edad_1, usuarios[0][3], usuarios[0][4]])

# Procesa al segundo usuario
usuario_nombre_2 = usuarios[1][1].strip().replace('_', ' ').split()
usuario_edad_2 = int(usuarios[1][2])
usuarios_limpio.append([usuarios[1][0], usuario_nombre_2, usuario_edad_2, usuarios[1][3], usuarios[1][4]])

# Procesa al tercer usuario
usuario_nombre_3 = usuarios[2][1].strip().replace('_', ' ').split()
usuario_edad_3 = int(usuarios[2][2])
usuarios_limpio.append([usuarios[2][0], usuario_nombre_3, usuario_edad_3, usuarios[2][3], usuarios[2][4]])

print(usuarios_limpio)
```

**Salida esperada:**
```
[['32415', ['mike', 'reed'], 32, ['ELECTRÓNICA', 'DEPORTE', 'LIBROS'], [894, 213, 173]],
 ['31980', ['kate', 'morgan'], 24, ['ROPA', 'LIBROS'], [439, 390]],
 ['32156', ['john', 'doe'], 37, ['ELECTRÓNICA', 'HOGAR', 'COMIDA'], [459, 120, 99]]]
```

---

#### Estructura General del Código
- [ ] **[OBLIGATORIO]** El código ejecuta sin errores de sintaxis
- [ ] **[OBLIGATORIO]** Todas las celdas están ejecutadas secuencialmente

---

### AVANZADO (Criterios No Obligatorios)

**Buenas Prácticas de Código**
- [ ] Aplica los métodos en el orden correcto (strip antes de split)
- [ ] Encadena métodos de string cuando es apropiado (ej: `strip().replace().split()`)
- [ ] Usa nombres de variables descriptivos y consistentes
- [ ] Usa consistentemente español O inglés en nombres de variables (no mezcla)

**Manejo de Excepciones Mejorado**
- [ ] El `except` captura la excepción específica (`ValueError`) en lugar de genérica
- [ ] Muestra mensaje de error informativo y claro

**Comprensión Conceptual**
- [ ] Demuestra entendimiento del flujo de limpieza de datos
- [ ] Identifica patrones en los datos que requieren limpieza
- [ ] Puede explicar por qué cada paso de limpieza es necesario
- [ ] Entiende la diferencia entre tipos de datos (int vs float vs str)

**Código Optimizado**
- [ ] Usa `sum()` en lugar de sumar elementos uno por uno (Paso 6)
- [ ] Mantiene consistencia en el formato de datos limpios
- [ ] Código es legible y bien organizado

---

## Criterios de Aprobación General

**Niveles de aprobación:**

- **APROBADO**:
  - Todos los 9 pasos completados correctamente con las salidas esperadas
  - El código ejecuta sin errores
  - Todas las celdas ejecutadas secuencialmente

- **APROBADO CON DISTINCIÓN**:
  - Todos los criterios de APROBADO
  - Al menos 5 criterios adicionales de AVANZADO

---

## Criterios de Descalificación

**Errores Críticos que descalifican automáticamente:**
- Notebook con celdas sin ejecutar
- Código que genera errores de sintaxis sin corregir
- No implementa `strip()` ni `replace()` para limpieza de nombres
- No usa `int()` para conversión de tipos
- No implementa `try/except` en ningún momento
- Las salidas no coinciden con las esperadas en más de 3 pasos
- Plagio o copia directa sin comprensión

---

## Errores Frecuentes

*Esta sección identifica los errores más comunes observados en este proyecto.*

### Errores en Manipulación de Cadenas

1. **Aplicar split() antes de strip()**:
   - Incorrecto: `usuario_nombre.split().strip()` - Error: listas no tienen método strip()
   - Correcto: `usuario_nombre.strip().split()`
   - Consecuencia: Error de ejecución o espacios no eliminados

2. **Olvidar el argumento en replace()**:
   - Incorrecto: `usuario_nombre.replace("_")` - Error: replace requiere 2 argumentos
   - Correcto: `usuario_nombre.replace("_", " ")`
   - Consecuencia: TypeError

3. **No reasignar el resultado de strip()/replace()**:
   - Incorrecto: `usuario_nombre.strip()` sin asignar
   - Correcto: `usuario_nombre = usuario_nombre.strip()`
   - Consecuencia: El valor original no se modifica

### Errores en Conversión de Tipos

4. **Usar str() en lugar de int()**:
   - Incorrecto: `usuario_edad = str(usuario_edad)` convierte a string
   - Correcto: `usuario_edad = int(usuario_edad)` convierte a entero
   - Consecuencia: Tipo de dato incorrecto para análisis numérico

5. **No manejar excepciones en conversión**:
   - Incorrecto: `int('treinta')` sin try/except causa error fatal
   - Correcto: Envolver en try/except
   - Consecuencia: Programa se detiene ante datos inválidos

### Errores en Try/Except

6. **Usar except genérico sin acción**:
   - Incorrecto: `except: pass` - oculta todos los errores
   - Correcto: `except ValueError: print('Mensaje de error')`
   - Consecuencia: Errores silenciosos, difícil debugging

7. **Mezclar nombres de variables (español/inglés)**:
   - Incorrecto: Definir `usuario_edad` pero usar `user_age` en el código
   - Correcto: Usar consistentemente `usuario_edad` en todo el código
   - Consecuencia: NameError - variable no definida
   - **NOTA**: Este error aparece en la solución oficial (Paso 4) donde se define `usuario_edad` pero se usa `user_age` dentro del try/except

### Errores en Listas

8. **Confundir índices (off-by-one)**:
   - Incorrecto: `usuarios[1]` para acceder al primer elemento
   - Correcto: `usuarios[0]` - índices comienzan en 0
   - Consecuencia: Acceso a datos incorrectos

9. **Modificar lista mientras se itera**:
   - Incorrecto: `for u in usuarios: usuarios.append(...)`
   - Correcto: Crear lista nueva `usuarios_limpio` y agregar ahí
   - Consecuencia: Bucle infinito o resultados inesperados

### Errores en F-strings

10. **Olvidar la 'f' antes de la cadena**:
    - Incorrecto: `"El usuario {usuario_id}..."` - no sustituye variables
    - Correcto: `f"El usuario {usuario_id}..."`
    - Consecuencia: Se imprime el nombre de variable literal, no su valor

11. **Usar comillas incorrectas dentro de f-string**:
    - Incorrecto: `f"El usuario es "{usuario_nombre[0]}""`
    - Correcto: `f"El usuario es {usuario_nombre[0]}"`
    - Consecuencia: SyntaxError

---

## Error Conceptual en la Solución Oficial

> **Advertencia para revisores**: En el **Paso 4** de la solución oficial (`S1 ESP SOLV Python básico.ipynb`), existe una inconsistencia en los nombres de variables:
>
> - Se define `usuario_edad = 'treinta y dos'`
> - Pero dentro del try se usa `user_age_int = int(user_age)` (en inglés)
>
> Esto funcionaría si `user_age` estuviera definido previamente, pero es un error conceptual que mezcla idiomas. El código correcto debería ser:
> ```python
> usuario_edad_int = int(usuario_edad)
> ```

**Formulario de Feedback**: [TBD - Google Form](enlace-por-definir)
