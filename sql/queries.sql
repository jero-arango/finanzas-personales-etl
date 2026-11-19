-- 1. Ver todas las transacciones 
SELECT * FROM transacciones;

-- 2. Totales de ingresos y de gastos
SELECT 
    tipo,
    COUNT(*) AS cantidad_movimientos,
    SUM(monto) AS total_dinero
FROM transacciones
GROUP BY tipo;

-- 3. Gatos por categoria de menor a
SELECT 
    categoria,
    COUNT(*) AS cantidad,
    SUM(monto) AS total_gastado
FROM transacciones
WHERE tipo = 'Gasto'
GROUP BY categoria
ORDER BY total_gastado DESC;