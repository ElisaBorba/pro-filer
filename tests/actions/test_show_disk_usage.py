from pro_filer.actions.main_actions import show_disk_usage  # NOQA
from unittest.mock import Mock
import pytest


@pytest.fixture
def tmp_files(monkeypatch, tmp_path):
    file_1 = tmp_path / "file_1.py"
    file_2 = tmp_path / "file_2.py"
    file_1.write_text("Hello")
    file_2.write_text("Goodbye")

    mock_function = "pro_filer.actions.main_actions._get_printable_file_path"

    mock_return = Mock(return_value="file.py")
    monkeypatch.setattr(mock_function, mock_return)

    context = {"all_files": [str(file_1), str(file_2)]}
    return context


def test_show_disk_usage(capsys, tmp_files):
    show_disk_usage(tmp_files)
    captured = capsys.readouterr().out
    expected = f"""'file.py':{''.ljust(60)} 7 (58%)
'file.py':{''.ljust(60)} 5 (41%)
Total size: 12\n"""
    assert captured == expected


def test_show_disk_usage_empty(capsys):
    context = {"all_files": []}
    show_disk_usage(context)
    captured = capsys.readouterr()
    assert "Total size: 0" in captured.out
