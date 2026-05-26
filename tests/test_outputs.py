import subprocess


def test_all_pass():

    result = subprocess.run(
        ["pytest", "tests/test_api.py"],
        capture_output=True,
        text=True
    )

    assert "failed" not in result.stdout.lower()