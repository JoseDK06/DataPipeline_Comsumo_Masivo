import pandas as pd

def transform_data(ventas_csv, ventas_db, clientes, productos):

    ventas_total = pd.concat([ventas_csv, ventas_db], ignore_index=True)

    df = ventas_total.merge(clientes, on="cliente_id", how="left")

    df = df.merge(productos, on="producto_id", how="left")

    df["ticket_promedio"] = df["monto"] / df["unidades"]

    df["anio"] = pd.to_datetime(df["fecha"]).dt.year
    df["mes"] = pd.to_datetime(df["fecha"]).dt.month

    print("Transformación completada")
    #Se agrego esta linea a modo de prueba
    return df