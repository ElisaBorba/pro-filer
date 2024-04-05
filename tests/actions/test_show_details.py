from pro_filer.actions.main_actions import show_details  # NOQA
import os
from datetime import date

# from pathlib import Path


def test_show_details_existing_path(capsys, tmp_path):
    test_path = tmp_path / "test_path.png"
    context = {"base_path": str(test_path)}

    test_path.touch()
    file_stats = os.stat(test_path)
    last_modified = date.fromtimestamp(file_stats.st_mtime)

    expected = (
        f"File name: {test_path.name}\n"
        f"File size in bytes: {file_stats.st_size}\n"
        f"File type: file\n"
        f"File extension: {test_path.suffix}\n"
        f"Last modified date: {last_modified}\n"
    )
    assert test_path.exists()
    assert os.path.isfile(test_path)

    show_details(context)
    captured = capsys.readouterr()
    assert captured.out == expected


def test_show_details_existing_but_no_extension(capsys, tmp_path):
    test_path = tmp_path / "test_path"
    context = {"base_path": str(test_path)}

    test_path.touch()
    file_stats = os.stat(test_path)
    last_modified = date.fromtimestamp(file_stats.st_mtime)

    expected = (
        f"File name: {test_path.name}\n"
        f"File size in bytes: {file_stats.st_size}\n"
        f"File type: file\n"
        f"File extension: [no extension]\n"
        f"Last modified date: {last_modified}\n"
    )
    assert test_path.exists()
    assert os.path.isfile(test_path)

    show_details(context)
    captured = capsys.readouterr()
    assert captured.out == expected


def test_show_details_non_existing_path(capsys):
    context_no_file = {"base_path": "nothing/no_path.png"}

    show_details(context_no_file)
    captured = capsys.readouterr()
    assert captured.out == "File 'no_path.png' does not exist\n"


# if __name__ == "__main__":
#     context = {"base_path": "/home/trybe/Downloads/Trybe_logo.png"}
#     print(show_details(context))
