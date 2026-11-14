# rncc-calc

A deliberately small calculator package. It exists so that a release pipeline has something
to version: every lab in the Release Notes and Commit Convention course commits to this
repository, and the version in `pyproject.toml` (mirrored in `src/rncc_calc/__init__.py`)
is what the release tooling bumps.

Usage:

```
python -m rncc_calc 2 + 3
```
