from server.tools.data_tools import analyze_file


def test_analyze_csv(tmp_path):
    (tmp_path / "sample.csv").write_text(
        "name,amount\nAlice,100\nBob,200\n", encoding="utf-8"
    )
    result = analyze_file(tmp_path, "sample.csv")
    assert "Rows: 2" in result
    assert "Alice" in result


def test_missing_file(tmp_path):
    assert "not found" in analyze_file(tmp_path, "missing.csv").lower()


def test_unsupported_extension(tmp_path):
    assert "Unsupported" in analyze_file(tmp_path, "sample.txt")
