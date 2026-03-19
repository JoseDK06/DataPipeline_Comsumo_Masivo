import pandas as pd
import mysql.connector

def extract_db():

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Root1234",
        database="consumo_masivo"
    )

    query = "SELECT * FROM ventas_erp"

    df = pd.read_sql(query, conn)

    conn.close()

    print(f"MySQL registros: {len(df)}")

    return df