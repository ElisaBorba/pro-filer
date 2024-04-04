from pro_filer.actions.main_actions import show_preview  # NOQA
import pytest


context_dict = {
    "all_files": ["src/__init__.py", "src/app.py", "src/utils/__init__.py"],
    "all_dirs": ["src", "src/utils"],
}

context_dict_expected = "Found 3 files and 2 directories\nFirst 5 files: ['src/__init__.py', 'src/app.py', 'src/utils/__init__.py']\nFirst 5 directories: ['src', 'src/utils']\n"

context_more_than_5 = {
    "all_files": [
        "src/__init__.py",
        "src/app.py",
        "src/utils/__init__.py",
        "src/python.py",
        "src/java.py",
        "src/javascript.py",
    ],
    "all_dirs": [
        "src",
        "src/utils",
        "src/utils/a",
        "src/utils/a/b",
        "src/utils/a/b/c",
        "src/utils/a/b/c/d",
    ],
}

context_more_than_5_expected = "Found 6 files and 6 directories\nFirst 5 files: ['src/__init__.py', 'src/app.py', 'src/utils/__init__.py', 'src/python.py', 'src/java.py']\nFirst 5 directories: ['src', 'src/utils', 'src/utils/a', 'src/utils/a/b', 'src/utils/a/b/c']\n"

context_empty = {"all_files": [], "all_dirs": []}
context_empty_expected = "Found 0 files and 0 directories\n"


@pytest.mark.parametrize(
    "context, expected",
    [
        (context_dict, context_dict_expected),
        (context_more_than_5, context_more_than_5_expected),
        (context_empty, context_empty_expected),
    ],
)
def test_show_preview(context, expected, capsys):
    show_preview(context)
    captured = capsys.readouterr()
    assert captured.out == expected
