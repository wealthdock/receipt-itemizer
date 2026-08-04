"""Smoke tests for the package."""

import re

import receipt_itemizer as pkg


def test_package_importable() -> None:
    assert pkg is not None


def test_version_is_semver() -> None:
    assert re.match(r"^\d+\.\d+\.\d+$", pkg.__version__)
