from zipfile import ZipFile

import openpyxl
from pypdf import PdfReader
from openpyxl import load_workbook
import csv
import os


def test_files():
    namelist = ["morr.pdf", "csv_tab.csv", "tab.xlsx"]
    CURRENT_FILE = os.path.abspath(__file__)
    CURRENT_DIRECTORY = os.path.dirname(CURRENT_FILE)

    zip_path = os.path.join(CURRENT_DIRECTORY, 'files.zip')
    
    if ".xlsx" in zip_path:
        with ZipFile(zip_path) as zip_file:
            with zip_file.open(zip_path, "r") as file:
                excel_file = openpyxl.load_workbook(file)
                excel_sheet = excel_file.active
                text = []
                for row in excel_sheet.iter_rows(values_only=True):
                    text.append(row)
                excel_out = ', '.join([', '.join(row) for row in text])
                return excel_out

    if ".csv" in zip_path:
        with ZipFile(zip_path) as zip_file:
            with zip_file.open(zip_path, "r") as file:
                csv_content = file.read().decode('utf-8')
                csv_reader = csv.reader(csv_content.splitlines())
                text = []
                for row in csv_reader:
                    text.append(row)
                csv_out = ', '.join([', '.join(row) for row in text])
                return csv_out

    if ".pdf" in zip_path:
        with ZipFile(zip_path) as zip_file:
            with zip_file.open(zip_path, "r") as file:
                pdf_file = PdfReader(file)
                return pdf_file.pages[0].extract_text()
