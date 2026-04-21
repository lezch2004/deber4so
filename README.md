# Algoritmo del Banquero

## Integrantes del grupo

| Nombre | Contribución |
|---|---|
| Luis Zaldumbide |  Implementación del algoritmo del banquero y validación de entradas |
| Isabella Tulcan | Implementación de la lectura de datos de entrada y validación de estado del sistema
| Martin Ruiz | Creación del Dockerfile, configuración del contenedor y documentación del README

---

## Descripción

Implementación interactiva del **Algoritmo del Banquero** (*Banker's Algorithm*) de Dijkstra en Python. El programa:

1. Recibe el estado actual del sistema (asignaciones y máximos).
2. Calcula si el sistema está en un **estado seguro** y devuelve una secuencia segura.
3. Permite simular **peticiones de recursos** y determina si concederlas mantiene el estado seguro.
   

## ¿Qué es el Algoritmo del Banquero?

El algoritmo del banquero es un algoritmo de prevención de deadlocks en sistemas operativos. Dado un estado actual de asignación de recursos, determina si el sistema se encuentra en un estado seguro, es decir, si existe algún orden en que todos los procesos pueden terminar sin quedar bloqueados.

---

## Requisitos

- Docker instalado en tu máquina
- No se necesita Python ni ninguna otra dependencia

---

## Cómo ejecutar localmente (sin Docker)

Requiere **Python 3.8+**.

```bash
python banker.py
```

## Cómo correr el programa con Docker

**Opción 1 — Descargar desde Docker Hub:**
```bash
docker pull luiszaldumbide/banquero
docker run -it luiszaldumbide/banquero
```

**Opción 2 — Construir localmente:**
```bash
docker build -t banquero .
docker run -it banquero
```

---

## Entradas del programa

El programa es interactivo (por eso el flag -it), te irá pidiendo los datos paso a paso:

| Entrada | Descripción |
|---|---|
| 1. Número de procesos | Cuántos procesos compiten por recursos |
| 2. Número de recursos | Cuántos tipos de recursos hay en el sistema |
| 3. Total por recurso | Cuántas instancias hay de cada recurso en total |
| 4. Máximo por proceso | Cuánto podría necesitar cada proceso de cada recurso como máximo |
| 5. Asignación por proceso | Cuánto ya tiene asignado cada proceso de cada recurso |

Todos los valores deben ser **enteros no negativos**.

---

## Salidas del programa

- Si el sistema es **seguro**: imprime la secuencia segura de ejecución
- Si el sistema es **inseguro**: imprime qué procesos están bloqueados

---

## Ejemplo de uso

### Caso seguro

```
Número de procesos: 5
Número de recursos: 3

Total de recursos:
  Recurso 1: 10
  Recurso 2: 5
  Recurso 3: 7

Max por proceso:
  Proceso 1: 7 5 3
  Proceso 2: 3 2 2
  Proceso 3: 9 0 2
  Proceso 4: 2 2 2
  Proceso 5: 4 3 3

Allocation por proceso:
  Proceso 1: 0 1 0
  Proceso 2: 2 0 0
  Proceso 3: 3 0 2
  Proceso 4: 2 1 1
  Proceso 5: 0 0 2
```

**Resultado esperado:**
```
✅ ESTADO SEGURO
Secuencia segura: P2 → P4 → P5 → P3 → P1
```

### Caso inseguro

```
Número de procesos: 2
Número de recursos: 1

Total de recursos:
  Recurso 1: 2

Max por proceso:
  Proceso 1: 2
  Proceso 2: 2

Allocation por proceso:
  Proceso 1: 1
  Proceso 2: 1
```

**Resultado esperado:**
```
❌ ESTADO INSEGURO - posible deadlock
Procesos bloqueados: [1, 2]
```

---

## Notas sobre validación

- Si `Asignación[Pi][Rj] > Máximo[Pi][Rj]` → error, estado inválido.
- Si la suma de asignaciones supera el total de recursos → error.
- Si una petición supera la `Necesidad` declarada → denegada.
- Si los recursos no están disponibles → el proceso debe esperar.
- Si conceder la petición lleva a estado inseguro → denegada.

## Estructura del proyecto

```
banquero/
├── banquero.py
├── Dockerfile
└── README.md
```
