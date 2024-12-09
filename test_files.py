from zipfile import ZipFile
import openpyxl
from pypdf import PdfReader
import csv
import os


def assert_path():
    zip_path = os.path.abspath("res/files.zip")
    return zip_path


def test_file_pdf(zip_files):
    zip_path = assert_path()
    zip_file = ZipFile(zip_path)
    pdf_zip = zip_file.open('morr.pdf')
    pdf_file = PdfReader(pdf_zip)
    assert 'The purpose and significance of this paper' in pdf_file.pages[0].extract_text()
    pdf_zip.close()
    zip_file.close()


def test_file_csv(zip_files):
    zip_path = assert_path()
    zip_file = ZipFile(zip_path)
    csv_file = zip_file.open('csv_tab.csv')
    csv_content = csv_file.read().decode('utf-8')
    csv_reader = csv.reader(csv_content.splitlines())
    text = []
    csv_out = []
    for row in csv_reader:
        text.append(row)
        csv_out = ', '.join([', '.join(row) for row in text])
    assert "Павлова" in csv_out
    zip_file.close()


def test_file_xlsx(zip_files):
    zip_path = assert_path()
    zip_file = ZipFile(zip_path)
    xlsx_file = zip_file.open('tab.xlsx')
    excel_file = openpyxl.load_workbook(xlsx_file)
    excel_sheet = excel_file.active
    assert "Дубина" in excel_sheet.cell(row=9,column=1).value
    xlsx_file.close()
    zip_file.close()
