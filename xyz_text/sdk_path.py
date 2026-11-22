# SPDX-License-Identifier: MIT
"""Locate the repository-level ``SDK/`` and import its text module.

Only the text geometry is used by this package. ``hanzi_data.py`` alone is
~1.9 MB, so vendoring a second copy would be wasteful and would drift from
the SDK. Instead the skill imports it from the repo's ``SDK/`` directory.

Resolution order:

1. ``ROBONIX_XYZ_SDK`` environment variable (used by ``scripts/start.sh``);
2. ``<repo root>/SDK`` computed from this file's location.

The SDK package needs numpy + Pillow because its ``__init__`` imports the
image pipeline; see ``requirements.txt``.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

ENV_VAR = "ROBONIX_XYZ_SDK"


def sdk_root() -> Path:
    override = os.environ.get(ENV_VAR, "").strip()
    root = (
        Path(override).expanduser()
        if override
        else Path(__file__).resolve().parents[4] / "SDK"
    )
    if not (root / "robonix_sdk" / "text.py").is_file():
        raise RuntimeError(
            f"Robonix XYZ SDK not found at {root}; set {ENV_VAR} to the "
            "directory that contains robonix_sdk/"
        )
    return root


def ensure_sdk_on_path() -> None:
    root = str(sdk_root())
    if root not in sys.path:
        sys.path.insert(0, root)


def text_module():
    ensure_sdk_on_path()
    from robonix_sdk import text

    return text