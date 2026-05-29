# Consigna – Campeonato Mundial de Fútbol

Se desea desarrollar un programa en Python que procese los resultados de un campeonato de fútbol.

En el campeonato participan 10 selecciones y se juega bajo el formato **todos contra todos**, es decir, cada equipo juega un partido contra cada uno de los demás.

Los resultados de los partidos se encuentran almacenados en un archivo CSV llamado `partidos.csv`.

Cada línea del archivo tiene el siguiente formato:

```csv
Equipo1,goles_equipo1,Equipo2,goles_equipo2
```

Por ejemplo:

```csv
Argentina,2,Brasil,1
```

indica que Argentina le ganó 2 a 1 a Brasil.

---

## Se pide

Desarrollar un programa que:

1. Lea el archivo `partidos.csv`.
2. Calcule para cada equipo:
   - Partidos jugados.
   - Partidos ganados.
   - Partidos empatados.
   - Partidos perdidos.
   - Goles a favor.
   - Goles en contra.
   - Diferencia de gol.
   - Puntos obtenidos.

### Sistema de puntaje

- Partido ganado: 3 puntos.
- Partido empatado: 1 punto.
- Partido perdido: 0 puntos.

3. Muestre la tabla de posiciones ordenada:
   - Primero por puntos.
   - Luego por diferencia de gol.
   - Luego por goles a favor.

4. Muestre el podio del campeonato:
   - Campeón.
   - Subcampeón.
   - Tercer puesto.

---

## Restricciones

- Utilizar estructuras de datos vistas en clase.
- El archivo debe leerse desde disco.
- No se permite cargar manualmente los resultados en listas dentro del código.
- Resolver utilizando funciones.

---

# Archivo `partidos.csv`

```csv
Argentina,2,Brasil,1
Argentina,3,Alemania,0
Argentina,1,Francia,1
Argentina,2,España,0
Argentina,4,Italia,2
Argentina,1,Portugal,0
Argentina,2,Inglaterra,2
Argentina,3,Uruguay,1
Argentina,2,Paises Bajos,1
Brasil,2,Alemania,2
Brasil,1,Francia,3
Brasil,2,España,1
Brasil,3,Italia,1
Brasil,1,Portugal,1
Brasil,2,Inglaterra,0
Brasil,1,Uruguay,0
Brasil,2,Paises Bajos,2
Alemania,1,Francia,0
Alemania,2,España,2
Alemania,1,Italia,1
Alemania,3,Portugal,1
Alemania,2,Inglaterra,1
Alemania,0,Uruguay,0
Alemania,1,Paises Bajos,2
Francia,2,España,0
Francia,1,Italia,1
Francia,2,Portugal,1
Francia,3,Inglaterra,2
Francia,1,Uruguay,0
Francia,2,Paises Bajos,1
España,1,Italia,0
España,2,Portugal,2
España,0,Inglaterra,1
España,2,Uruguay,1
España,1,Paises Bajos,1
Italia,1,Portugal,0
Italia,2,Inglaterra,2
Italia,1,Uruguay,1
Italia,0,Paises Bajos,1
Portugal,1,Inglaterra,3
Portugal,2,Uruguay,0
Portugal,1,Paises Bajos,1
Inglaterra,2,Uruguay,1
Inglaterra,2,Paises Bajos,0
Uruguay,1,Paises Bajos,1
```

---

## Cantidad total de partidos

En un torneo todos contra todos de 10 equipos deben jugarse:

```text
45 partidos
```

El archivo provisto contiene exactamente esa cantidad de encuentros.

