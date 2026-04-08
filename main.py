import pandas as pd
import numpy as np

# Creación de nuestro ÚNICO dataframe principal de trabajo
datos_ventas = {
    'id_venta': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115],
    'sucursal': ['Norte', 'Sur', 'Centro', 'Norte', 'Centro', 'Sur', 'Norte', 'Sur', 'Centro', 'Norte', 'Sur', 'Centro', 'Norte', 'Norte', 'Sur'],
    'producto': ['Laptop', 'Mouse', 'Teclado', 'Laptop', 'Monitor', 'Teclado', 'Mouse', 'Monitor', 'Laptop', 'Mouse', 'Teclado', 'Monitor', 'Laptop', 'Monitor', 'Teclado'],
    'cantidad': [2, np.nan, 5, 1, 2, 4, np.nan, 3, 2, 5, 3, np.nan, 4, 1, 2],
    'precio_base': ['1200.50', '25.00', '45.00', '1200.50', '250.00', '45.00', '25.00', '250.00', '1200.50', '25.00', '45.00', '250.00', '1200.50', '250.00', '45.00'],
    'categoria': ['Computación', 'Accesorios', 'Accesorios', 'Computación', 'Periféricos', 'Accesorios', 'Accesorios', 'Periféricos', 'Computación', 'Accesorios', 'Accesorios', 'Periféricos', 'Computación', 'Periféricos', 'Accesorios'],
    'columna_basura': ['x', 'y', 'z', 'w', 'a', 'b', 'c', 'x', 'y', 'z', 'a', 'b', 'c', 'w', 'x']
}

df_ventas = pd.DataFrame(datos_ventas)

# Reto 1: Mantenimiento y orden (Limpieza inicial)

df_ventas = df_ventas.drop(columns=['columna_basura'])

df_ventas = df_ventas.rename(columns={'precio_base': 'precio_unitario'})

df_ventas = df_ventas.sort_values(by='id_venta', ascending=False)


# Reto 2: Sondeo de datos

df_ventas["sucursal"].unique()
df_ventas["producto"].nunique()

df_ventas['producto'].value_counts()


# Reto 3: Limpieza de datos profunda

df_ventas['cantidad'] = df_ventas['cantidad'].fillna(1)

df_ventas["precio_unitario"] = df_ventas["precio_unitario"].astype(float)

df_ventas["sucursal"] = df_ventas["sucursal"].astype('category')


# Reto 4: Filtrado inteligente

ventas_fuertes = df_ventas[df_ventas['precio_unitario'] > 150.0]

filtro = (df_ventas['sucursal'] == 'Norte') & (df_ventas['precio_unitario'] > 150.0)

df_filtrado = df_ventas[filtro]

# Reto 5: Filtrado inteligente

df_ventas["total_venta"] = df_ventas["cantidad"]*df_ventas['precio_unitario']

resumen = df_ventas.groupby("sucursal")["total_venta"].agg(["sum", "mean"])
 

df_presupuestos = pd.DataFrame({
    'categoria': ['Computación', 'Accesorios', 'Periféricos'],
    'presupuesto_marketing': [5000, 1500, 2000]
})


df_final = df_ventas.merge(df_presupuestos, on='categoria', how='left')

print(df_final)