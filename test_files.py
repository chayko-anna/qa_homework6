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

   # with ZipFile(zip_path) as zip_file:
   #     if namelist not in zip_file.namelist():
   #         assert False, f"File {namelist} not found."

    if ".xlsx" in zip_path:
        with ZipFile('resources/archive.zip') as zip_file:
            with zip_file.open(zip_path, "r") as file:
                excel_file = openpyxl.load_workbook(file)
                excel_sheet = excel_file.active
                text = []
                for row in excel_sheet.iter_rows(values_only=True):
                    text.append(row)
                actual_result = ', '.join([', '.join(row) for row in text])
                return actual_result

    if ".csv" in zip_path:
        with ZipFile('resources/archive.zip') as zip_file:
            with zip_file.open(zip_path, "r") as file:
                excel_file = openpyxl.load_workbook(file)
                excel_sheet = excel_file.active
                text = []
                for row in excel_sheet.iter_rows(values_only=True):
                    text.append(row)
                actual_result = ', '.join([', '.join(row) for row in text])
                return actual_result

    if ".pdf" in zip_path:
        with ZipFile('resources/archive.zip') as zip_file:
            with zip_file.open(zip_path, "r") as file:
                pdf_file = PdfReader(file)
                text = []