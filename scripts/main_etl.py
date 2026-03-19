from con_db import extract_db
from data_read import extract_files
from data_transform import transform_data
from data_export import export_excel

print("INICIANDO ETL")

ventas_db = extract_db()

ventas_csv, clientes, productos = extract_files()

dataset = transform_data(
    ventas_csv,
    ventas_db,
    clientes,
    productos
)

export_excel(dataset)

print("ETL FINALIZADO")