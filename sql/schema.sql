DROP TABLE IF EXISTS transacciones;

CREATE TABLE transacciones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha TEXT NOT NULL,
    descripcion TEXT NOT NULL,
    monto REAL NOT NULL,
    categoria TEXT NOT NULL,
    tipo TEXT NOT NULL
);