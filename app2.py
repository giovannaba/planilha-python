import openpyxl

# carregando arquivo
book = openpyxl.load_workbook('Planilha de compras.xlsx')

# selecionando uma pagina
frutas_page = book['Frutas']

# imprimindo dados de cada linha
for rows in frutas_page.iter_rows(min_row=2, max_row=5):
    for cell in rows:
        print(cell.value)
