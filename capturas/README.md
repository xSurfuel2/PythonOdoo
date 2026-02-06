# 📊 Automatización de Datos en Odoo con Python (ETL) — Odoo + PostgreSQL en Docker

Esta práctica consiste en desarrollar un script en **Python** que actúe como proceso **ETL (Extracción, Transformación y Carga)** para importar un listado de centros educativos desde un **CSV** a la base de datos **PostgreSQL** usada por **Odoo**, ejecutándose en un entorno **Docker**.

---

## ✅ Requisitos del Enunciado (resumen)

- **Python 3.10+**
- Librerías obligatorias: **pandas**, **psycopg2-binary**
- Infraestructura: **Docker Desktop** con contenedores **Odoo** y **DB** activos
- Script `importar.py` (en mi repo aparece como `conexion.py`, pero cumple la misma función ETL)
- Tabla destino creada automáticamente si no existe
- Lectura de CSV con `encoding="latin1"`
- Inserción recorriendo el DataFrame con bucle y acceso por posiciones (`iloc`)
- `commit()` solo si no hay errores
- **README profesional con capturas incrustadas y explicadas**

---

## 🛠️ Tecnologías

- Python 3.10+
- pandas
- psycopg2-binary
- Docker Desktop
- Odoo + PostgreSQL
- pgAdmin
- VS Code
- Git / GitHub

---

## 📁 Estructura del repositorio (referencia)

```
.
├── conexion.py / importar.py
├── listado.csv / centros_educativos.csv
├── docker-compose.yaml
├── README.md
└── capturas/
    ├── cap1.png
    ├── cap2.png
    ├── cap3.png
    ├── cap4.png
    ├── cap5.png
    ├── cap6.png
    ├── cap7.png
    ├── cap8.png
    └── cap9.png
```

> **Nota:** En el enunciado se pide `importar.py`. Si tu archivo se llama distinto (por ejemplo `conexion.py`), puedes renombrarlo a `importar.py` para ajustarte 100% al enunciado.

---

## ⚙️ Procedimiento (paso a paso)

### 1) Levantar el entorno Docker (Odoo + DB + pgAdmin)

Desde la carpeta donde está `docker-compose.yaml`:

```bash
docker-compose up -d
```

Opcionalmente, para comprobar que los contenedores están arriba:

```bash
docker ps
```

---

### 2) Instalar dependencias en Python

```bash
py -m pip install pandas psycopg2-binary
```

---

### 3) Ejecutar el script ETL

Ejecuta el script (según el nombre en tu repo):

```bash
python importar.py
# o
python conexion.py
```

Si todo va bien, verás mensajes de éxito (lectura CSV, conexión OK e importación completada).

---

### 4) Verificar en pgAdmin (consulta SQL)

En pgAdmin, abre la herramienta de consulta y ejecuta:

```sql
SELECT * FROM public.contactos_mailing LIMIT 10;
```

Con esto se verifica que los registros del CSV están cargados en PostgreSQL.

---

## 🧾 Qué hace el script (ETL)

- **Extracción:** lee el CSV con `encoding="latin1"` para respetar tildes/ñ.
- **Transformación:** carga el CSV en un `DataFrame` (pandas) y prepara los valores.
- **Carga:** crea la tabla destino (si no existe) y recorre el DataFrame insertando fila a fila usando `iloc`.
- **Robustez:** usa un bloque `try/except` y hace `commit()` únicamente si no hay errores.

---

## 📸 Evidencias (capturas obligatorias)

A continuación se incluyen **todas las capturas** (cap1.png → cap9.png) **incrustadas y explicadas**, tal como exige el enunciado.

> **Importante:** en varias capturas se ve el reloj/barra de tareas del sistema (requisito de validación del alumno).

---

### 🖼️ cap1.png — Instalación de psycopg2-binary

En esta captura se observa la instalación correcta de la librería `psycopg2-binary`, necesaria para la conexión con PostgreSQL.

![cap1](./capturas/cap1.png)

---

### 🖼️ cap2.png — docker-compose up -d (contenedores levantados)

Ejecución de `docker-compose up -d` donde se ve que se crean/inician los contenedores (odoo, db, pgadmin) y la red.

![cap2](./capturas/cap2.png)

---

### 🖼️ cap3.png — docker ps (estado de contenedores)

Comprobación del estado con `docker ps`, donde se listan los contenedores y su estado (Up/Restarting, puertos, etc.).

![cap3](./capturas/cap3.png)

---

### 🖼️ cap4.png — Instalación de pandas

Instalación de la librería `pandas`, usada para leer el CSV y manejar el DataFrame.

![cap4](./capturas/cap4.png)

---

### 🖼️ cap5.png — Ejecución del script en VS Code (éxito)

Ejecución del script desde VS Code. Se aprecia:
- lectura correcta del CSV,
- conexión establecida,
- mensaje de éxito con el número de registros importados,
- y el reloj/barra inferior del sistema.

![cap5](./capturas/cap5.png)

---

### 🖼️ cap6.png — Alta/registro de servidor en pgAdmin (General)

Pantalla de configuración inicial del servidor en pgAdmin (nombre del servidor, grupo, etc.) para conectarse a la base de datos del contenedor.

![cap6](./capturas/cap6.png)

---

### 🖼️ cap7.png — Configuración de conexión en pgAdmin (host, puerto, usuario)

Configuración de conexión en pgAdmin:
- Host: `db` (nombre del servicio en docker-compose)
- Puerto: `5432`
- Usuario: `odoo`
- Base de mantenimiento: `postgres`
- Contraseña configurada

![cap7](./capturas/cap7.png)

---

### 🖼️ cap8.png — Acceso a la herramienta de consulta SQL en pgAdmin

Acceso a **Herramienta de Consulta** para ejecutar el `SELECT` y validar que los datos se han cargado correctamente.

![cap8](./capturas/cap8.png)

---

### 🖼️ cap9.png — SELECT mostrando datos cargados

Resultado del `SELECT` en pgAdmin mostrando registros ya insertados en la tabla destino (`public.contactos_mailing`), confirmando que la carga ETL se completó correctamente.

![cap9](./capturas/cap9.png)

---

## ✅ Checklist de rúbrica

- **Conectividad (2.5 pts):** conexión Python ↔ PostgreSQL (Docker) verificada ✅  
- **Código (2.5 pts):** pandas + bucle + inserciones + `commit()` seguro ✅  
- **Git (2.0 pts):** repositorio con script, CSV y commits ✅  
- **Documentación (3.0 pts):** README claro + **capturas incrustadas** + evidencias ✅  

---

## 👤 Autor

**Surfuel**  
Repositorio: PythonOdoo
