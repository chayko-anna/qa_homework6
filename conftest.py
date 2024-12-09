import os
from asyncio import wait_for
from zipfile import ZipFile
import pytest
import time

@pytest.fixture()
def zip_files():
    CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
    res_dir = os.path.join(CURRENT_DIRECTORY, 'res')
    zip_path = os.path.abspath("res/files.zip")

    with ZipFile('res/files.zip', 'w') as res_zip:
        for file in os.listdir(res_dir):
            if ".zip" not in file:
                add_file = os.path.join(res_dir, file)
                res_zip.write(add_file, arcname=file)
    yield

    os.remove(zip_path)