import json
from pathlib import Path


class WalColors:
    WALCOLOR_LOCATION = Path.home() / ".cache/wal/colors.json"

    def __init__(self):
        """Manages from pywal"""
        self._colors_raw = json.load(open(self.WALCOLOR_LOCATION))
        for key, value in self._colors_raw["colors"].items():
            setattr(self, key, Color(value))


class Color:
    def __init__(self, color: str):
        """Object for dealing with colors for qtile.

        Args:
            color (str): Color in hex format, e.g. #ffffff
        """
        self.color = color

    def __str__(self) -> str:
        return self.color

    def as_rgba(self) -> tuple:
        """Returns color as a tuple of RGBA values."""

        return hex_to_rgba(self.color)


def hex_to_rgba(hex):
    hex = hex.lstrip("#")
    hlen = len(hex)
    return tuple(int(hex[i : i + hlen // 3], 16) for i in range(0, hlen, hlen // 3))
