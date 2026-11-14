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
    return OPERATORS[operator](left, right)
