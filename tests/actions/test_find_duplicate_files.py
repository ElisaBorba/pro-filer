from pro_filer.actions.main_actions import find_duplicate_files  # NOQA
import pytest


@pytest.fixture
def tmp_files(tmp_path):
    file_1 = tmp_path / "file_1.py"
    file_2 = tmp_path / "file_2.py"
    file_3 = tmp_path / "file_3.py"

    file_1.write_text("Hello")
    file_2.write_text("Goodbye")
    file_3.write_text("Goodbye")

    context = {"all_files": [str(file_1), str(file_2), str(file_3)]}
    return context


def test_find_duplicate_files(tmp_files):
    find_duplicate_files(tmp_files)
    duplicates = find_duplicate_files(tmp_files)

    expected = [
        (tmp_files["all_files"][1], tmp_files["all_files"][2]),
    ]

    assert duplicates == expected


def test_find_duplicate_files_error():
    context = {
        "all_files": [
            "./tests/no_file.py",
            "./tests/actions/no_file_2.py",
            "./pro_filer/no_file_3.py",
        ]
    }

    with pytest.raises(ValueError, match="All files must exist"):
        find_duplicate_files(context)
