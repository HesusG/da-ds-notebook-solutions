# Criterios de Evaluación: Proyecto 2 — Python Básico (Continuación)

## Objetivo

Aplicar técnicas avanzadas de Python para procesar y analizar datos de clientes de Store 1, incluyendo funciones reutilizables, bucles, condicionales y filtrado de datos para responder preguntas de negocio.

**Requisitos previos**: Completar SP1 (manipulación de strings, tipos de datos, listas básicas).

**Competencias que desarrollarás**: Definición y uso de funciones, bucles for, condicionales if/elif/else, operador `in` para membresía, función sum(), filtrado de datos con condiciones múltiples, trabajo con listas anidadas

> **NOTA IMPORTANTE**: Este sprint está estructurado en **pasos secuenciales (Paso 1-9)**. Cada paso introduce un concepto nuevo y debe completarse correctamente antes de avanzar al siguiente. La evaluación se basa en la correcta ejecución de cada paso con su salida esperada.

<details>
<summary>Task Statement</summary>

## Descripción del proyecto

Como miembro del equipo analítico de Store 1, has recibido una base de datos cruda con información de clientes y sus compras. Tu objetivo es limpiar y procesar estos datos para poder responder a preguntas clave del negocio, como identificar clientes leales, analizar ingresos por categoría, y encontrar oportunidades de marketing segmentado.

## Instrucciones del proyecto

1. **Limpieza de datos:**
   - Limpiar espacios y guiones bajos de nombres
   - Convertir edades a enteros
   - Convertir categorías a minúsculas
   - Crear función reutilizable para limpieza

2. **Análisis de ingresos:**
   - Calcular ingresos totales de la empresa
   - Sumar gastos de todos los usuarios

3. **Segmentación de clientes:**
   - Filtrar usuarios menores de 30 años
   - Identificar jóvenes con alto gasto (>$1000)
   - Filtrar por categoría de compra

4. **Automatización:**
   - Crear función para filtrar por categoría
   - Generar reportes reutilizables

## Descripción de los datos

Estructura de cada registro de usuario:
- `[0]` user_id: identificador único (string)
- `[1]` user_name: nombre y apellido (string con posibles errores)
- `[2]` user_age: edad (float)
- `[3]` fav_categories: categorías favoritas (lista de strings en mayúsculas)
- `[4]` total_spendings: gastos por categoría (lista de números)

</details>

## Glosario de Términos Técnicos

**Función (def)**: Bloque de código reutilizable que realiza una tarea específica. Se define con `def nombre(argumentos):` y puede retornar valores con `return`.

**Bucle for**: Estructura de control que itera sobre una secuencia (lista, string, rango) ejecutando un bloque de código para cada elemento.

**Condicional if**: Estructura que ejecuta código solo si una condición es verdadera. Puede incluir `elif` y `else` para condiciones alternativas.

**Operador in**: Operador de membresía que verifica si un elemento existe dentro de una secuencia. Retorna True o False.

**lower()**: Método de cadena que convierte todos los caracteres a minúsculas.

**sum()**: Función incorporada que suma todos los elementos de un iterable numérico.

**Listas anidadas**: Listas que contienen otras listas como elementos, permitiendo estructuras de datos multidimensionales.

**append()**: Método de lista que agrega un elemento al final de la lista.

**return**: Palabra clave que devuelve un valor desde una función y termina su ejecución.

**Índice negativo**: En Python, `lista[-1]` accede al último elemento, `lista[-2]` al penúltimo, etc.

---

## Rúbrica de Evaluación - Checklist para Revisores

### BÁSICO (Todos los Pasos - OBLIGATORIOS)

#### Paso 1: Limpieza inicial de un registro de cliente
- [ ] **[OBLIGATORIO]** Usa `strip()` y `replace('_', ' ')` para limpiar el nombre
- [ ] **[OBLIGATORIO]** Usa `split()` para dividir nombre y apellido
- [ ] **[OBLIGATORIO]** Usa `int()` para convertir la edad
- [ ] **[OBLIGATORIO]** Modifica la lista `user` directamente usando índices
- [ ] **[OBLIGATORIO]** La salida muestra la lista con nombre como lista y edad como entero

**Código correcto:**
```python
# Usuario de ejemplo
user = ['32415', ' mike_reed ', 32.0, ['ELECTRONICS', 'SPORT', 'BOOKS'], [894, 213, 173]]

# Paso 1: limpiar y dividir el nombre
user[1] = user[1].strip().replace('_', ' ')

# Paso 2: dividir el nombre en una lista
user[1] = user[1].split()

# Paso 3: convertir la edad a entero
user[2] = int(user[2])

# Mostrar resultado
print(user)
```

**Salida esperada:**
```
['32415', ['mike', 'reed'], 32, ['ELECTRONICS', 'SPORT', 'BOOKS'], [894, 213, 173]]
```

---

#### Paso 2: Convertir las categorías a minúsculas
- [ ] **[OBLIGATORIO]** Crea una lista vacía `fav_categories_low`
- [ ] **[OBLIGATORIO]** Usa un bucle `for` para iterar sobre las categorías
- [ ] **[OBLIGATORIO]** Usa `lower()` para convertir cada categoría a minúsculas
- [ ] **[OBLIGATORIO]** Usa `append()` para agregar cada categoría convertida
- [ ] **[OBLIGATORIO]** La salida es exactamente: `['electronics', 'sport', 'books']`

**Código correcto:**
```python
# Lista original de categorías favoritas escritas en mayúsculas
fav_categories = ['ELECTRONICS', 'SPORT', 'BOOKS']

# 1. Lista vacía donde almacenaremos las categorías convertidas a minúsculas
fav_categories_low = []

# 2. Recorremos cada categoría en la lista original
for category in fav_categories:
    # 3. Convertimos la categoría a minúscula utilizando el método lower()
    lowered_category = category.lower()

    # 4. Agregamos la categoría convertida a la nueva lista
    fav_categories_low.append(lowered_category)

# Mostramos en pantalla la lista resultante
print(fav_categories_low)
```

**Salida esperada:**
```
['electronics', 'sport', 'books']
```

---

#### Paso 3: Limpieza completa de un usuario (función)
- [ ] **[OBLIGATORIO]** Define función `clean_user(user)` con parámetro
- [ ] **[OBLIGATORIO]** Dentro de la función, limpia el nombre con `strip()`, `replace()` y `split()`
- [ ] **[OBLIGATORIO]** Convierte edad a entero con `int()`
- [ ] **[OBLIGATORIO]** Convierte categorías a minúsculas con bucle `for` y `lower()`
- [ ] **[OBLIGATORIO]** Usa `return` para devolver la lista limpia
- [ ] **[OBLIGATORIO]** La función retorna una lista con el formato correcto

**Código correcto:**
```python
def clean_user(user):
    # Limpia y divide el nombre
    name = user[1].strip().replace('_', ' ').split()

    # Edad como entero
    age = int(user[2])

    # Categorías a minúsculas
    categories = []
    for cat in user[3]:
        categories.append(cat.lower())

    return [user[0], name, age, categories, user[4]]

# Prueba
test_user = ['32415', ' mike_reed ', 32.0, ['ELECTRONICS', 'SPORT', 'BOOKS'], [894, 213, 173]]
print(clean_user(test_user))
```

**Salida esperada:**
```
['32415', ['mike', 'reed'], 32, ['electronics', 'sport', 'books'], [894, 213, 173]]
```


---

#### Paso 4: Limpieza de toda la base de usuarios
- [ ] **[OBLIGATORIO]** Crea lista vacía `users_clean`
- [ ] **[OBLIGATORIO]** Usa bucle `for` para iterar sobre `users_raw`
- [ ] **[OBLIGATORIO]** Llama a `clean_user()` para cada usuario
- [ ] **[OBLIGATORIO]** Usa `append()` para agregar usuarios limpios a la lista
- [ ] **[OBLIGATORIO]** Muestra `users_clean` al final

**Código correcto:**
```python
users_raw = [
    ['32415', ' mike_reed ', 32.0, ['ELECTRONICS', 'SPORT', 'BOOKS'], [894, 213, 173]],
    ['31980', 'kate morgan', 24.0, ['CLOTHES', 'BOOKS'], [439, 390]],
    ['32156', ' john doe ', 37.0, ['ELECTRONICS', 'HOME', 'FOOD'], [459, 120, 99]],
    ['32761', 'SAMANTHA SMITH', 29.0, ['CLOTHES', 'ELECTRONICS', 'BEAUTY'], [299, 679, 85]],
    ['32984', 'David White', 41.0, ['BOOKS', 'HOME', 'SPORT'], [234, 329, 243]],
    ['33001', 'emily brown', 26.0, ['BEAUTY', 'HOME', 'FOOD'], [213, 659, 79]],
    ['33767', ' Maria Garcia', 33.0, ['CLOTHES', 'FOOD', 'BEAUTY'], [499, 189, 63]],
    ['33912', 'JOSE MARTINEZ', 22.0, ['SPORT', 'ELECTRONICS', 'HOME'], [259, 549, 109]],
    ['34009', 'lisa wilson ', 35.0, ['HOME', 'BOOKS', 'CLOTHES'], [329, 189, 329]],
    ['34278', 'James Lee', 28.0, ['BEAUTY', 'CLOTHES', 'ELECTRONICS'], [189, 299, 579]]
]

users_clean = []

for user in users_raw:
    user_new = clean_user(user)
    users_clean.append(user_new)

print(users_clean)
```

**Salida esperada (primeros 3 elementos):**
```
[['32415', ['mike', 'reed'], 32, ['electronics', 'sport', 'books'], [894, 213, 173]],
 ['31980', ['kate', 'morgan'], 24, ['clothes', 'books'], [439, 390]],
 ['32156', ['john', 'doe'], 37, ['electronics', 'home', 'food'], [459, 120, 99]],
 ...]
```

> **Nota para revisores**: Verificar que los 10 usuarios están en la lista y que todos los nombres están separados correctamente en sublistas de 2 elementos.

---

#### Paso 5: Calcular ingresos totales
- [ ] **[OBLIGATORIO]** Inicializa variable `revenue = 0` antes del bucle
- [ ] **[OBLIGATORIO]** Usa bucle `for` para iterar sobre `users_clean`
- [ ] **[OBLIGATORIO]** Accede a la lista de gastos con `user[-1]` o `user[4]`
- [ ] **[OBLIGATORIO]** Usa `sum()` para sumar los gastos de cada usuario
- [ ] **[OBLIGATORIO]** Acumula con `+=` en cada iteración
- [ ] **[OBLIGATORIO]** La salida es exactamente: `9189`

**Código correcto:**
```python
users_clean = [['32415', ['mike', 'reed'], 32, ['electronics', 'sport', 'books'], [894, 213, 173]],
               ['31980', ['kate', 'morgan'], 24, ['clothes', 'books'], [439, 390]],
               ['32156', ['john', 'doe'], 37, ['electronics', 'home', 'food'], [459, 120, 99]],
               ['32761', ['samantha', 'smith'], 29, ['clothes', 'electronics', 'beauty'], [299, 679, 85]],
               ['32984', ['david', 'white'], 41, ['books', 'home', 'sport'], [234, 329, 243]],
               ['33001', ['emily', 'brown'], 26, ['beauty', 'home', 'food'], [213, 659, 79]],
               ['33767', ['maria', 'garcia'], 33, ['clothes', 'food', 'beauty'], [499, 189, 63]],
               ['33912', ['jose', 'martinez'], 22, ['sport', 'electronics', 'home'], [259, 549, 109]],
               ['34009', ['lisa', 'wilson'], 35, ['home', 'books', 'clothes'], [329, 189, 329]],
               ['34278', ['james', 'lee'], 28, ['beauty', 'clothes', 'electronics'], [189, 299, 579]]]

revenue = 0

for user in users_clean:
    spendings_list = user[-1]
    total_spendings = sum(spendings_list)
    revenue += total_spendings

print(revenue)
```

**Salida esperada:**
```
9189
```

---

#### Paso 6: Usuarios menores de 30 años
- [ ] **[OBLIGATORIO]** Usa bucle `for` para iterar sobre `users_clean`
- [ ] **[OBLIGATORIO]** Usa condicional `if` para verificar `user[2] < 30`
- [ ] **[OBLIGATORIO]** Imprime solo el primer nombre con `user[1][0]`
- [ ] **[OBLIGATORIO]** La salida muestra exactamente 5 nombres

**Código correcto:**
```python
for user in users_clean:
    if user[2] < 30:
        print(user[1][0])
```

**Salida esperada:**
```
kate
samantha
emily
jose
james
```

> **Nota para revisores**: La edad está en `user[2]`. El nombre está en `user[1]` como sublista, y `user[1][0]` accede al primer nombre.

---

#### Paso 7: Jóvenes con alto gasto
- [ ] **[OBLIGATORIO]** Usa bucle `for` para iterar sobre `users_clean`
- [ ] **[OBLIGATORIO]** Calcula el gasto total con `sum(user[-1])`
- [ ] **[OBLIGATORIO]** Usa `if` con operador `and` para combinar condiciones
- [ ] **[OBLIGATORIO]** Condiciones: `user[2] < 30` AND `total_spendings > 1000`
- [ ] **[OBLIGATORIO]** La salida muestra exactamente 2 nombres

**Código correcto:**
```python
for user in users_clean:
    spendings_list = user[-1]
    total_spendings = sum(spendings_list)

    if user[2] < 30 and total_spendings > 1000:
        print(user[1][0])
```

**Salida esperada:**
```
samantha
james
```

> **Nota para revisores**:
> - samantha: edad 29 (<30), gasto total = 299+679+85 = 1063 (>1000) ✓
> - james: edad 28 (<30), gasto total = 189+299+579 = 1067 (>1000) ✓

---

#### Paso 8: Usuarios que compraron ropa
- [ ] **[OBLIGATORIO]** Usa bucle `for` para iterar sobre `users_clean`
- [ ] **[OBLIGATORIO]** Verifica si `'clothes'` está en las categorías del usuario
- [ ] **[OBLIGATORIO]** Imprime nombre y edad en la misma línea
- [ ] **[OBLIGATORIO]** La salida muestra exactamente 5 usuarios

**Código correcto (solución MÁS básica - verificación por índice):**
```python
for user in users_clean:
    categories = user[3]

    if categories[0] == 'clothes':
        print(user[1][0], user[2])
    elif categories[1] == 'clothes':
        print(user[1][0], user[2])
    elif len(categories) > 2 and categories[2] == 'clothes':
        print(user[1][0], user[2])
```

> **Nota**: Esta solución es válida pero frágil - solo funciona si todas las listas tienen 2-3 categorías. Es común en estudiantes principiantes.

**Código correcto (solución básica con bucle anidado):**
```python
for user in users_clean:
    categories = user[3]

    for category in categories:
        if category == 'clothes':
            print(user[1][0], user[2])
```

**Código correcto (solución avanzada con operador `in`):**
```python
for user in users_clean:
    categories = user[3]

    if 'clothes' in categories:
        print(user[1][0], user[2])
```

**Salida esperada:**
```
kate 24
samantha 29
maria 33
lisa 35
james 28
```

> **Nota para revisores**: Las tres soluciones son válidas y producen la misma salida.
> - La solución MÁS básica usa múltiples `elif` (común en principiantes)
> - La solución con bucle anidado es más robusta
> - La solución con `in` es la más elegante y eficiente

---

#### Paso 9: Función con filtro por categoría
- [ ] **[OBLIGATORIO]** Define función `get_clients_by_category(users, category)` con 2 parámetros
- [ ] **[OBLIGATORIO]** Crea lista vacía `result` dentro de la función
- [ ] **[OBLIGATORIO]** Usa bucle `for` para iterar sobre usuarios
- [ ] **[OBLIGATORIO]** Verifica si la categoría está en las categorías del usuario
- [ ] **[OBLIGATORIO]** Calcula gasto total con `sum(user[-1])`
- [ ] **[OBLIGATORIO]** Agrega sublista `[id, nombre, edad, gasto_total]` a `result`
- [ ] **[OBLIGATORIO]** Usa `return` para devolver la lista
- [ ] **[OBLIGATORIO]** La prueba con `'home'` retorna 5 usuarios

**Código correcto:**
```python
def get_clients_by_category(users, category):
    result = []

    for user in users:
        if category in user[3]:
            total_spent = sum(user[-1])
            result.append([user[0], user[1], user[2], total_spent])

    return result

# Prueba con la categoría 'home'
filtered = get_clients_by_category(users_clean, 'home')
print(filtered)
```

**Salida esperada:**
```
[['32156', ['john', 'doe'], 37, 678],
 ['32984', ['david', 'white'], 41, 806],
 ['33001', ['emily', 'brown'], 26, 951],
 ['33912', ['jose', 'martinez'], 22, 917],
 ['34009', ['lisa', 'wilson'], 35, 847]]
```

> **Nota para revisores**: Verificar que:
> - La función acepta 2 parámetros (users, category)
> - Retorna una lista (no imprime)
> - Cada elemento tiene formato [id, nombre, edad, gasto_total]
> - El gasto total está calculado correctamente para cada usuario

---

#### Estructura General del Código
- [ ] **[OBLIGATORIO]** El código ejecuta sin errores de sintaxis
- [ ] **[OBLIGATORIO]** Todas las celdas están ejecutadas secuencialmente

---

### AVANZADO (Criterios No Obligatorios)

**Buenas Prácticas en Funciones**
- [ ] La función `clean_user()` no depende de variables globales
- [ ] Usa nombres de parámetros descriptivos
- [ ] Documenta qué hace la función con comentarios

**Optimización de Código**
- [ ] Usa operador `in` en lugar de bucle anidado para buscar en lista (Paso 8)
- [ ] Evita calcular `sum()` múltiples veces para el mismo usuario
- [ ] Usa índices negativos (`user[-1]`) para acceder al último elemento

**Comprensión Conceptual**
- [ ] Puede explicar la diferencia entre modificar lista original vs crear nueva
- [ ] Entiende cuándo usar `for` vs `while`
- [ ] Reconoce patrones de filtrado de datos
- [ ] Puede explicar por qué usar `and` en lugar de dos `if` anidados

**Código Limpio**
- [ ] Usa nombres de variables descriptivos y consistentes
- [ ] Código bien indentado y organizado
- [ ] Sin código duplicado innecesario

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
- No implementa ninguna función (def)
- No usa bucles for en ningún momento
- No usa condicionales if en ningún momento
- Código genera errores de sintaxis sin corregir
- Las salidas no coinciden con las esperadas en más de 3 pasos
- Plagio o copia directa sin comprensión

---

## Errores Frecuentes

*Esta sección identifica los errores más comunes observados en este proyecto.*

### Errores en Funciones

1. **No usar return en la función**:
   - Incorrecto: `def clean_user(user): print(resultado)` - no retorna valor
   - Correcto: `def clean_user(user): return resultado`
   - Consecuencia: La función retorna None, no se puede usar el resultado

2. **Usar variables globales dentro de función**:
   - Incorrecto: `def clean(): return users_raw[0]` - depende de variable externa
   - Correcto: `def clean(user): return user[0]` - usa parámetro
   - Consecuencia: Función no es reutilizable

3. **Confundir replace("-", " ") con replace("_", " ")**:
   - Incorrecto: `user[1].replace("-", " ")` cuando los datos tienen guiones bajos
   - Correcto: `user[1].replace("_", " ")` para los datos de este proyecto
   - Consecuencia: Los nombres con guión bajo no se limpian correctamente
   - **NOTA**: Este error aparece en la solución oficial (Paso 3)

### Errores en Bucles

4. **No inicializar acumulador antes del bucle**:
   - Incorrecto: `for user in users: revenue += sum(user[-1])` sin definir revenue
   - Correcto: `revenue = 0` antes del bucle
   - Consecuencia: NameError - variable no definida

5. **Modificar lista mientras se itera**:
   - Incorrecto: `for user in users: users.append(clean_user(user))`
   - Correcto: Usar lista separada `users_clean.append(clean_user(user))`
   - Consecuencia: Bucle infinito o resultados inesperados

6. **Olvidar append() en bucle**:
   - Incorrecto: `for cat in fav_categories: cat.lower()` sin guardar
   - Correcto: `fav_categories_low.append(cat.lower())`
   - Consecuencia: La lista resultado queda vacía

### Errores en Condicionales

7. **Usar = en lugar de == para comparación**:
   - Incorrecto: `if user[2] = 30:` - asignación, no comparación
   - Correcto: `if user[2] == 30:` - comparación de igualdad
   - Consecuencia: SyntaxError

8. **No usar paréntesis con operadores lógicos complejos**:
   - Incorrecto: `if age < 30 and spending > 1000 or category == 'home'`
   - Correcto: `if (age < 30 and spending > 1000) or category == 'home'`
   - Consecuencia: Lógica incorrecta por precedencia de operadores

9. **Confundir `in` con `==` para buscar en lista**:
   - Incorrecto: `if user[3] == 'clothes':` - compara lista completa con string
   - Correcto: `if 'clothes' in user[3]:` - busca elemento en lista
   - Consecuencia: Siempre retorna False, no encuentra ningún usuario

### Errores en Índices

10. **Índice incorrecto para acceder a datos**:
    - Incorrecto: `user[3]` para acceder a gastos (son las categorías)
    - Correcto: `user[4]` o `user[-1]` para gastos
    - Consecuencia: Cálculos con datos incorrectos

11. **Olvidar doble índice para listas anidadas**:
    - Incorrecto: `print(user[1])` imprime ['mike', 'reed']
    - Correcto: `print(user[1][0])` imprime 'mike'
    - Consecuencia: Muestra lista en lugar de elemento específico

### Errores en Cálculos

12. **No usar sum() para sumar lista**:
    - Incorrecto: `total = user[-1]` - asigna la lista, no la suma
    - Correcto: `total = sum(user[-1])`
    - Consecuencia: TypeError al intentar comparar lista con número

13. **Calcular total dentro de condición sin guardarlo**:
    - Incorrecto: `if sum(user[-1]) > 1000: print(sum(user[-1]))` - calcula dos veces
    - Correcto: `total = sum(user[-1]); if total > 1000: print(total)`
    - Consecuencia: Código ineficiente

---

## Error Conceptual en la Solución Oficial

> **Advertencia para revisores**: En el **Paso 3** de la solución oficial (`S2 ESP SOLV Python básico (continuación).ipynb`), la función `clean_user()` usa `replace("-"," ")` en lugar de `replace("_"," ")`:
>
> ```python
> # Código en la solución oficial (INCORRECTO)
> name = user[1].strip().replace("-"," ").split()
> ```
>
> Esto causa que el nombre `mike_reed` NO se separe correctamente:
> - Resultado incorrecto: `['mike_reed']` (un solo elemento)
> - Resultado correcto: `['mike', 'reed']` (dos elementos)
>
> El código correcto debería usar guión bajo:
> ```python
> name = user[1].strip().replace("_"," ").split()
> ```

**Formulario de Feedback**: [TBD - Google Form](enlace-por-definir)
