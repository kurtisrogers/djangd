#!/usr/bin/env python
"""Example Django project for djangd-framework."""
import os
import sys


def main() -> None:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "example_project.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Run `pip install -e ..[dev]` first."
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
