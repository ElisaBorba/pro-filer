import pytest
from pro_filer.actions.main_actions import show_preview  # NOQA
from faker import Faker

fake = Faker()
Faker.seed(0)


def fake_paths(path_quantity, ext_quantity=""):
    paths = []
    for _ in range(path_quantity):
        path = f"src{fake.file_path(depth=2, extension=ext_quantity)}"
        paths.append(path)
    return paths


context_dict = {"all_files": fake_paths(3, "py"), "all_dirs": fake_paths(2)}

context_more_than_5 = {
    "all_files": fake_paths(6, "py"),
    "all_dirs": fake_paths(6),
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
