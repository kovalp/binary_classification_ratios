"""."""

import pytest

from binary_classification_ratios.cli.main import run


def test_run() -> None:
    """."""
    f1 = run(['-tp', '1', '-tn', '2', '-fp', '3', '-fn', '4'])
    assert f1 == pytest.approx(0.222222222222222222)
