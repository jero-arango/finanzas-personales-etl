import sqlite3
import pandas as pd
from pathlib import Path

#Definicion de rutas Pathlib
BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DATA_PATH = BASE_DIR / "data" / "raw" / "movimientos.csv"
SCHEMA_PATH = BASE_DIR / "sql" / "schema.sql"
DB_PATH = BASE_DIR / "finanzas.db" 

def extract(file_path: Path) -> pd.DataFrame:
    """Extrae los datos desde un archivo CSV."""
    print(f"Extrayendo datos desde {file_path}...")
    df = pd.read_csv(file_path)
    return df


def categorizar_movimiento(descripcion: str) -> str:
    """Asigna una categoría según palabras clave en la descripción."""
    desc = descripcion.upper()
    if any(palabra in desc for palabra in ["EXITO", "CARULLA", "D1", "MERCADO"]):
        return "Alimentación y Mercado"
    elif any(palabra in desc for palabra in ["TERPEL", "GASOLINA", "PEAJE", "UBER"]):
        return "Transporte"
    elif any(palabra in desc for palabra in ["RESTAURANT", "PIPA", "COMIDA", "CAFE"]):
        return "Restaurantes"
    elif any(palabra in desc for palabra in ["NETFLIX", "SPOTIFY", "CINE"]):
        return "Entretenimiento"
    elif any(palabra in desc for palabra in ["QUINCENA", "NOMINA", "DIDI", "PAGO"]):
        return "Ingresos Laborales"
    else:
        return "Otros"

def transform(df: pd.DataFrame) -> pd.DataFrame:
    """Limpia y transforma los datos crudos."""
    print("Transformando datos...")
    df_clean = df.copy()

    # 1. Normalizar texto
    df_clean["descripcion"] = df_clean["descripcion"].str.strip().str.upper()

    # 2. Determinar si es Ingreso o Gasto antes de quitar el signo
    df_clean["tipo"] = df_clean["monto"].apply(
        lambda x: "Ingreso" if x > 0 else "Gasto"
    )

    # 3. Convertir el monto a valor absoluto (positivo)
    df_clean["monto"] = df_clean["monto"].abs()

    # 4. Aplicar categorización automática
    df_clean["categoria"] = df_clean["descripcion"].apply(categorizar_movimiento)

    return df_clean


def load(df: pd.DataFrame, db_path: Path, schema_path: Path) -> None:
    """Crea la tabla en SQLite y carga los datos transformados."""
    print(f"Cargando {len(df)} registros en {db_path}...")
    
    with sqlite3.connect(db_path) as conn:
        # Ejecutar el esquema SQL para asegurar que la tabla exista y esté limpia
        with open(schema_path, "r", encoding="utf-8") as f:
            conn.executescript(f.read())
        
        # Insertar los datos del DataFrame en la tabla 'transacciones'
        df.to_sql("transacciones", conn, if_exists="append", index=False)

    print("¡Carga completada con éxito!")


if __name__ == "__main__":
    datos_crudos = extract(RAW_DATA_PATH)
    datos_limpios = transform(datos_crudos)
    load(datos_limpios, DB_PATH, SCHEMA_PATH)