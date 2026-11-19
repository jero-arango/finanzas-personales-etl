# Pipeline ETL de Finanzas Personales

Pipeline de datos automatizado desarrollado en **Python** y **SQLite** para extraer movimientos bancarios crudos desde archivos CSV, limpiarlos, categorizarlos automáticamente mediante reglas de negocio y cargarlos en una base de datos relacional para análisis financiero con SQL.

## Estructura del Proyecto

```text
finanzas-personales-etl/
├── data/
│   └── raw/
│       └── movimientos.csv    # Datos simulados de extractos bancarios
├── sql/
│   ├── schema.sql             # Definición de la tabla relacional
│   └── queries.sql            # Consultas SQL de negocio y agregación
├── src/
│   ├── etl.py                 # Proceso Extract, Transform, Load
│   └── analisis.py            # Ejecución de reportes en consola
├── .gitignore
├── requirements.txt
└── README.md