"""."""
from typing import Sequence

from .cmd_line import get_cmd_line
from binary_classification_ratios import BinaryClassificationRatios


def run(args: Sequence[str] | None = None) -> float:
    """."""
    cli = get_cmd_line(args)
    bcr = BinaryClassificationRatios(tp=cli.tp, tn=cli.tn, fp=cli.fp, fn=cli.fn)
    print(bcr.get_summary())
    return bcr.get_f1_score()


def main() -> None:
    """."""
    run()  # pragma: no cover
