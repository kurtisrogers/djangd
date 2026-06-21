"""Pytest entry point — ensures the workspace root is on sys.path so that
`tests.settings` resolves for pytest-django."""
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tests.settings")
