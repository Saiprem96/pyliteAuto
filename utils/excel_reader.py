import openpyxl
import os


def read_excel_data():
    # Build the absolute path to the Excel file
    file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'login_data.xlsx')
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    data = []
    headers = [cell.value for cell in sheet[1]]  # Get header names from first row

    for row in sheet.iter_rows(min_row=2, values_only=True):
        row_data = dict(zip(headers, row))
        data.append(row_data)

    return data
