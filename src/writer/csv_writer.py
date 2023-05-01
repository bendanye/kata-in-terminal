import os
from typing import List


class CsvWriter:
    def __init__(self, file_path: str, headers: List[str], delimiter: str = ","):
        self._file_path = file_path
        self._headers = headers
        self._delimiter = delimiter

    def write(self, row: List[str]):
        if not os.path.isfile(self._file_path):
            with open(self._file_path, "w") as f:
                f.write(f"{self._delimiter.join(self._headers)}\n")

        with open(self._file_path, "a") as f:
            f.write(f"{self._delimiter.join(row)}\n")
