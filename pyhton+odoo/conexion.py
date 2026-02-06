import pandas as pd
import psycopg2

# 1. Configuración de la conexión a PostgreSQL
params = {
    "host": "localhost",
    "port": 5432,
    "database": "postgres",
    "user": "odoo",
    "password": "odoo"
}

# 2. Ruta del archivo CSV
ruta_csv = r"C:/Users/Usuario1/Downloads/2ºDAM/Desarrollo de Interfaces/pyhton+odoo/listado.csv"

try:
    # 3. Leer el archivo CSV
    df = pd.read_csv(ruta_csv, encoding="latin1")
    print("✅ Archivo listado.csv leído correctamente.")

    # 4. Conexión con PostgreSQL
    conn = psycopg2.connect(**params)
    cur = conn.cursor()
    print("✅ Conexión con PostgreSQL establecida.")

    # 5. Crear tabla (campos TEXT para cualquier longitud)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS contactos_mailing (
            id SERIAL PRIMARY KEY,
            nombre TEXT,
            domicilio TEXT,
            localidad TEXT,
            cp TEXT,
            telefono TEXT
        );
    """)

    # 6. Insertar los datos del CSV
    for _, row in df.iterrows():
        cur.execute("""
            INSERT INTO contactos_mailing (
                nombre, domicilio, localidad, cp, telefono
            )
            VALUES (%s, %s, %s, %s, %s)
        """, (
            str(row.iloc[0]),  # Nombre
            str(row.iloc[1]),  # Domicilio
            str(row.iloc[2]),  # Localidad
            str(row.iloc[3]),  # Código Postal
            str(row.iloc[4])   # Teléfono
        ))

    conn.commit()
    print(f"🚀 ¡Éxito! Se han importado {len(df)} contactos.")

except Exception as e:
    print(f"❌ Ha ocurrido un error: {e}")
    if 'conn' in locals():
        conn.rollback()

finally:
    if 'cur' in locals():
        cur.close()
    if 'conn' in locals():
        conn.close()
