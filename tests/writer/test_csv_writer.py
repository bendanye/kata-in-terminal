import os
import tempfile

from src.writer.csv_writer import CsvWriter


def test_create_new_file_with_header_if_file_not_exists():
    with tempfile.TemporaryDirectory() as tmp_dir_name:
        file_path = f"{tmp_dir_name}/test.txt"

        CsvWriter(file_path, ["one", "two"]).write(["oneone;twotwo"])

        assert os.path.isfile(file_path) is True
        with open(file_path, "r") as actual_file:
            assert "one,two\n" == actual_file.readline()


def test_write_to_new_file():
    with tempfile.TemporaryDirectory() as tmp_dir_name:
        file_path = f"{tmp_dir_name}/test.txt"

        CsvWriter(file_path, ["one", "two"]).write(["oneone", "twotwo"])

        assert os.path.isfile(file_path) is True
        with open(file_path, "r") as actual_file:
            actual_file.readline()
            assert "oneone,twotwo\n" == actual_file.readline()


def test_does_not_create_file_if_file_already_exists():
    expected_header = "orig1,orig2\n"
    with tempfile.TemporaryDirectory() as tmp_dir_name:
        file_path = f"{tmp_dir_name}/test.txt"
        with open(file_path, "w") as actual_file:
            actual_file.write(expected_header)

        CsvWriter(file_path, ["one", "two"]).write(["oneone,twotwo"])

        assert os.path.isfile(file_path) is True
        with open(file_path, "r") as actual_file:
            assert expected_header == actual_file.readline()


def test_append_to_file_if_file_exists():
    with tempfile.TemporaryDirectory() as tmp_dir_name:
        file_path = f"{tmp_dir_name}/test.txt"
        with open(file_path, "w") as actual_file:
            actual_file.write("orig1,orig2\n")
            actual_file.write("onecol,seccol\n")

        CsvWriter(file_path, ["one", "two"]).write(["oneone", "twotwo"])

        assert os.path.isfile(file_path) is True
        with open(file_path, "r") as actual_file:
            actual_file.readline()
            assert "onecol,seccol\n" == actual_file.readline()
            assert "oneone,twotwo\n" == actual_file.readline()
