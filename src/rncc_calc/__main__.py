"""Command line entry point: python -m rncc_calc 2 + 3"""
import sys

from rncc_calc import __version__
from rncc_calc.calculator import calculate


def main(argv: list[str] | None = None) -> int:
    args = sys.argv[1:] if argv is None else argv
    if args == ["--version"]:
        print(__version__)
        return 0
    if len(args) != 3:
        print("usage: python -m rncc_calc <left> <operator> <right>", file=sys.stderr)
        return 2
    left, operator, right = args
    print(calculate(float(left), operator, float(right)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
