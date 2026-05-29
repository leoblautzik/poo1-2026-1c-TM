# Sets en Python

Un `set` es una colección **sin orden** y **sin elementos repetidos**.

Sirve muchísimo cuando:
- querés eliminar duplicados,
- verificar pertenencia rápido (`in`),
- hacer operaciones matemáticas de conjuntos (unión, intersección, etc.).

---

# Crear un set

```python
numeros = {1, 2, 3, 4}
```

También:

```python
vacio = set()
```

⚠️ Ojo:

```python
{}
```

NO es un set vacío, es un diccionario vacío.

---

# Características importantes

## 1. No admite repetidos

```python
nums = {1, 2, 2, 3, 3, 3}

print(nums)
```

Resultado:

```python
{1, 2, 3}
```

---

## 2. No tiene orden

No podés hacer:

```python
nums[0]
```

porque no hay posiciones.

---

## 3. Los elementos deben ser hashables

Esto funciona:

```python
{1, "hola", (1, 2)}
```

Esto NO:

```python
{[1, 2], [3, 4]}
```

porque las listas son mutables.

---

# Operaciones básicas

## Agregar elementos

```python
s = {1, 2}

s.add(3)

print(s)
```

---

## Eliminar elementos

```python
s.remove(2)
```

⚠️ Si no existe, lanza error.

Más seguro:

```python
s.discard(2)
```

No falla si no está.

---

## Verificar pertenencia

```python
if 3 in s:
    print("Está")
```

Esto es MUY eficiente en sets.

---

# Recorrer un set

```python
for x in s:
    print(x)
```

Pero recordá:
el orden no está garantizado.

---

# Convertir lista → set

Muy común para eliminar duplicados:

```python
nums = [1, 2, 2, 3, 3, 4]

sin_repetidos = set(nums)

print(sin_repetidos)
```

---

# Ejemplo útil: volver a lista

```python
nombres = ["Ana", "Luis", "Ana"]

unicos = set(nombres)
lista_sin_repetidos = list(set(nombres))

print(lista_sin_repetidos)
print(lista_sin_repetidos[1])
```

⚠️ Ojo:
Aunque conviertas el set nuevamente a lista, el orden original puede perderse.

---

# Operaciones de conjuntos

## Unión

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)
```

Resultado:

```python
{1, 2, 3, 4, 5}
```

---

## Intersección

Elementos comunes:

```python
print(a & b)
```

Resultado:

```python
{3}
```

---

## Diferencia

```python
print(a - b)
```

Resultado:

```python
{1, 2}
```

---

# Casos de uso MUY comunes

## 1. Eliminar duplicados

```python
nombres = ["Ana", "Luis", "Ana"]

unicos = set(nombres)
```

---

## 2. Verificaciones rápidas

Esto:

```python
if palabra in palabras:
```

si `palabras` es un set, es muchísimo más rápido que una lista grande.

---

## 3. Detectar repetidos

```python
vistos = set()

for n in numeros:
    if n in vistos:
        print("Repetido:", n)

    vistos.add(n)
```

---

# frozenset

Existe una versión inmutable:

```python
f = frozenset([1, 2, 3])
```

No se puede modificar.

---

# Diferencia entre list, tuple y set

| Tipo | Ordenado | Mutable | Repetidos |
|---|---|---|---|
| list | Sí | Sí | Sí |
| tuple | Sí | No | Sí |
| set | No | Sí | No |

---

# Detalle importante: hash table

Internamente, los `set` usan una estructura hash (igual que los diccionarios).

Por eso:
- `x in set` es muy rápido,
- agregar y buscar suelen ser O(1).

---

# Ejemplo realista

```python
alumnos_aprobados = {"Ana", "Luis", "Pedro"}

nombre = input("Nombre: ")

if nombre in alumnos_aprobados:
    print("Aprobó")
else:
    print("No aprobó")
```

---

# Set comprehension

Como list comprehension:

```python
cuadrados = {x*x for x in range(5)}

print(cuadrados)
```

Resultado:

```python
{0, 1, 4, 9, 16}
```

---

# Error típico de principiantes

Esto:

```python
s = {}
```

NO crea un set.

Para set vacío:

```python
s = set()
```

---

# Relación importante con dict

Un `dict` es básicamente:

- un set de claves
- donde cada clave tiene asociado un valor.

Por eso:
- ambos usan hashing,
- ambos requieren claves hashables,
- ambos tienen búsquedas rápidas.
