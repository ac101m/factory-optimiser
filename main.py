#!/usr/bin/env python3
"""Root entry point for the factory optimizer (docopt CLI).

Run either as `python main.py ...` or as `factory-optimiser ...` after
`pip install -e .`.
"""

from factory_optimiser.cli import main

if __name__ == "__main__":
    raise SystemExit(main())
