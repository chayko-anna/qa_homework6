import os
from zipfile import ZipFile

import pytest

@pytest.fixture(scope='class')

def zip_files():
    files = []
