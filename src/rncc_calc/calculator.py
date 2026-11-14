"""Five operators. Later labs add more through conventional commits."""

OPERATORS = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
    "^": lambda a, b: a ** b,
}


def calculate(left: float, operator: str, right: float) -> float:
    """Apply one binary operator to two numbers."""
    if operator not in OPERATORS:
        raise ValueError(f"unknown operator {operator!r}; expected one of {sorted(OPERATORS)}")
    try:
        return OPERATORS[operator](left, right)
    except ZeroDivisionError:
        raise ValueError("cannot divide by zero") from None
