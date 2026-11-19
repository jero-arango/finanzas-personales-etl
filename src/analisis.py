import sqlite3
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "finanzas.db"


def ejecutar_reporte():
    with sqlite3.connect(DB_PATH) as conn:
        print("\n=== 1. RESUMEN GENERAL (INGRESOS VS GASTOS) ===")
        df_resumen = pd.read_sql_query("""
            SELECT tipo, COUNT(*) AS movimientos, SUM(monto) AS total
            FROM transacciones
            GROUP BY tipo;
        """, conn)
        print(df_resumen.to_string(index=False))

        print("\n=== 2. GASTOS POR CATEGORÍA ===")
        df_categorias = pd.read_sql_query("""
            SELECT categoria, COUNT(*) AS cantidad, SUM(monto) AS total_gastado
            FROM transacciones
            WHERE tipo = 'Gasto'
            GROUP BY categoria
            ORDER BY total_gastado DESC;
        """, conn)
        print(df_categorias.to_string(index=False))


if __name__ == "__main__":
    ejecutar_reporte()