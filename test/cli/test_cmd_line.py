"""."""

from binary_classification_ratios.cli.cmd_line import get_cmd_line, CmdLine


def test_cmd_line_short_args() -> None:
    """."""
    cli = get_cmd_line(['-tp', '1', '-tn', '2', '-fp', '3', '-fn', '4'])
    assert isinstance(cli, CmdLine)
    assert cli.tp == 1
    assert cli.tn == 2
    assert cli.fp == 3
    assert cli.fn == 4


def test_cmd_line_no_args() -> None:
    """."""
    cli = get_cmd_line([])
    assert cli.tp == 0
    assert cli.tn == 0
    assert cli.fn == 0
    assert cli.fp == 0
    