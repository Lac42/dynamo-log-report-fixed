import json
from pathlib import Path

REPORT = Path("/app/report.json")


def load_report():
    assert REPORT.exists(), "no /app/report.json found"
    assert REPORT.stat().st_size > 0, "report.json is empty"
    return json.loads(REPORT.read_text())


def test_schema():
    """report.json is a single JSON object with exactly the three required keys."""
    data = load_report()
    assert isinstance(data, dict)
    assert set(data.keys()) == {"total_requests", "unique_ips", "top_path"}


def test_total_requests():
    """total_requests equals the 6 non-empty request lines in the log."""
    assert load_report()["total_requests"] == 6


def test_unique_ips():
    """unique_ips equals the 3 distinct client IP addresses."""
    assert load_report()["unique_ips"] == 3


def test_top_path():
    """top_path is the most-requested path, /index.html (3 hits)."""
    assert load_report()["top_path"] == "/index.html"
