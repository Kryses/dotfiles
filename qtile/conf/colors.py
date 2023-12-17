import json
from pathlib import Path

from libqtile.log_utils import logger


class WalColors:
    WALCOLOR_LOCATION = Path.home() / ".cache/wal/colors.json"

    def __init__(self):
        """Manages from pywal"""
        self._colors_raw = json.load(open(self.WALCOLOR_LOCATION))
        self.color0 = Color(self._colors_raw["colors"]["color0"])
        self.color1 = Color(self._colors_raw["colors"]["color1"])
        self.color2 = Color(self._colors_raw["colors"]["color2"])
        self.color3 = Color(self._colors_raw["colors"]["color3"])
        self.color4 = Color(self._colors_raw["colors"]["color4"])
        self.color5 = Color(self._colors_raw["colors"]["color5"])
        self.color6 = Color(self._colors_raw["colors"]["color6"])
        self.color7 = Color(self._colors_raw["colors"]["color7"])
        self.color8 = Color(self._colors_raw["colors"]["color8"])
        self.color9 = Color(self._colors_raw["colors"]["color9"])
        self.color10 = Color(self._colors_raw["colors"]["color10"])
        self.color11 = Color(self._colors_raw["colors"]["color11"])
        self.color12 = Color(self._colors_raw["colors"]["color12"])
        self.color13 = Color(self._colors_raw["colors"]["color13"])
        self.color14 = Color(self._colors_raw["colors"]["color14"])
        self.color15 = Color(self._colors_raw["colors"]["color15"])


class Color:
    def __init__(self, color: str):
        """Object for dealing with colors for qtile.

        Args:
            color (str): Color in hex format, e.g. #ffffff
        """
        self.color = color
        self.hex = None

        if isinstance(color, tuple):
            self.hex = rgba_to_hex(color)
        else:
            if color.startswith("#"):
                self.hex = color

    def __str__(self) -> str:
        return self.color

    def as_rgba(self) -> tuple:
        """Returns color as a tuple of RGBA values."""

        return hex_to_rgba(self.hex)

    def __add__(self, other: int) -> tuple:
        """Adds alpha to color.

        Args:
            other (int): Alpha value to add.

        Returns:
            tuple: RGBA tuple.
        """
        logger.warning(self.as_rgba())
        logger.warning(other)
        return Color(add_rgba(self.as_rgba(), other))

    def __mul__(self, other: int) -> tuple:
        """Multiplies alpha to color.

        Args:
            other (int): Alpha value to multiply.

        Returns:
            tuple: RGBA tuple.
        """
        return Color(muliply_rgba(self.as_rgba(), other))


def rgba_to_hex(rgba):
    # Ensure the RGB values are within the 0-255 range
    r, g, b = [max(0, min(255, int(x))) for x in rgba[:3]]

    # Alpha is expected to be between 0.0 and 1.0, convert to 0-255 integer range
    a = int(max(0.0, min(1.0, rgba[3])) * 255)

    # Return the hex color
    return "#{:02x}{:02x}{:02x}{:02x}".format(r, g, b, a)


def hex_to_rgba(hex):
    hex = hex.lstrip("#")
    if "." in hex:
        hex, alpha = hex.split(".")
    else:
        alpha = 1.0
    hlen = len(hex)

    rgba = tuple(int(hex[i : i + hlen // 3], 16) for i in range(0, hlen, hlen // 3)) + (
        float(alpha),
    )
    clampped_rgba = (
        clamp(rgba[0], 0.0, 1.0),
        clamp(rgba[1], 0.0, 1.0),
        clamp(rgba[2], 0.0, 1.0),
        clamp(rgba[3], 0.0, 1.0),
    )
    return clampped_rgba


def clamp(x, min, max):
    if x < min:
        return min
    if x > max:
        return max
    return x


def add_rgba(color1, color2):
    return (
        clamp(color1[0] + color2[0], 0, 255),
        clamp(color1[1] + color2[1], 0, 255),
        clamp(color1[2] + color2[2], 0, 255),
        clamp(color1[3] + color2[3], 0, 255),
    )


def muliply_rgba(color1, color2):
    return (
        clamp(color1[0] * color2[0], 0, 255),
        clamp(color1[1] * color2[1], 0, 255),
        clamp(color1[2] * color2[2], 0, 255),
        clamp(color1[3] * color2[3], 0, 255),
    )
