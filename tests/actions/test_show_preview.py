from faker import Faker
import pytest
from pro_filer.actions.main_actions import show_preview  # NOQA

fake = Faker()

context_dict = {
    "all_files": ["src/__init__.py", "src/app.py", "src/utils/__init__.py"],
    "all_dirs": ["src", "src/utils"],
}

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

context_empty = {"all_files": [], "all_dirs": []}


def generate_expected(files, dirs):
    return (
        f"Found {len(files)} files and {len(dirs)} directories\n"
        f"First 5 files: {files[:5]}\n"
        f"First 5 directories: {dirs[:5]}\n"
    )


context_dict_expected = generate_expected(
    context_dict["all_files"], context_dict["all_dirs"]
)
context_more_than_5_expected = generate_expected(
    context_more_than_5["all_files"], context_more_than_5["all_dirs"]
)
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
