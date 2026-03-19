def export_excel(df):

    output = "reporte_ventas_consolidado.xlsx"

    df.to_excel(output, index=False)

    print("Excel generado")