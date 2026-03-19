import pandas as pd
import json

def extract_files():

    ventas = pd.read_csv("data_sources/ventas_distribuidores.csv")

    with open("data_sources/clientes.json","r",encoding="utf-8") as f:
        clientes = pd.DataFrame(json.load(f))

    productos = pd.read_xml("data_sources/productos.xml")

    print("Archivos cargados")

    return ventas, clientes, productos