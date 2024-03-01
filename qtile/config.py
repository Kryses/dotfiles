#   ___ _____ ___ _     _____    ____             __ _
#  / _ \_   _|_ _| |   | ____|  / ___|___  _ __  / _(_) __ _
# | | | || |  | || |   |  _|   | |   / _ \| '_ \| |_| |/ _` |
# | |_| || |  | || |___| |___  | |__| (_) | | | |  _| | (_| |
#  \__\_\|_| |___|_____|_____|  \____\___/|_| |_|_| |_|\__, |
#                                                      |___/

# Icons: https://fontawesome.com/search?o=r&m=free

import os
import subprocess
import sys
from pathlib import Path

from kryslib.colors.wal_colors import WalColors
from libqtile import bar, hook, layout, qtile
from libqtile.config import (Click, Drag, DropDown, Group, Key, Match,
                             ScratchPad, Screen)
from libqtile.dgroups import simple_key_binder
from libqtile.lazy import lazy
from libqtile.log_utils import logger

qtile_path = Path.home() / ".config" / "qtile"
sys.path.append(str(qtile_path))

from conf.keyboard import keyboard_layout
from conf.widget_list import get_widget_list

# --------------------------------------------------------
# Your configuration
# --------------------------------------------------------

# Keyboard layout in conf/keyboard.py

# Show wlan status bar widget (set to False if wired network)
# show_wlan = True
wal_colors = WalColors(walcolor_json=Path.home() / ".cache/wal/colors.json")


# --------------------------------------------------------
# General Variables
# --------------------------------------------------------

# Get home path
home = str(Path.home())

# Get Core name: x11 or wayland
core_name = qtile.core.name
logger.warning("Using config.py with " + core_name)

# --------------------------------------------------------
# Define Status Bar
# --------------------------------------------------------
try:
    wm_bar = Path(home + "/.cache/.qtile_bar_x11.sh").read_text().replace("\n", "")
except Exception:
    wm_bar = "qtile"

logger.warning("Status bar: " + wm_bar)


# --------------------------------------------------------
# Set default apps
# --------------------------------------------------------

terminal = "alacritty"

# --------------------------------------------------------
# Keybindings
# --------------------------------------------------------

mod = "mod4"  # SUPER KEY
alt_mod = "mod1"  # Alt Key

logger.warning("Using keys with x11")
keys = [
    # Focus
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    # Monitors
    Key([mod], "period", lazy.next_screen(), desc="Move focus to next monitor"),
    Key([mod], "comma", lazy.prev_screen(), desc="Move focus to prev monitor"),
    Key(
        [mod],
        "space",
        lazy.layout.next(),
        desc="Move window focus to other window around",
    ),
    # Move
    Key(
        [mod, "shift"],
        "Left",
        lazy.layout.shuffle_left(),
        desc="Move window to the left",
    ),
    Key(
        [mod, "shift"],
        "Right",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod], "m", lazy.layout.maximize(), desc="maximize"),
    Key([mod], "n", lazy.layout.normalize(), desc="normalize"),
    Key([mod, "shift"], "n", lazy.layout.reset(), desc="normalize"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Swap
    Key([mod, "shift"], "h", lazy.layout.swap_left()),
    Key([mod, "shift"], "l", lazy.layout.swap_right()),
    Key(
        [mod],
        "Print",
        lazy.spawn(home + "/dotfiles/qtile/scripts/x11/screenshot.sh"),
    ),
    # Size
    Key(
        [mod, "control"],
        "Down",
        lazy.layout.shrink(),
        desc="Grow window to the left",
    ),
    Key([mod, "control"], "Up", lazy.layout.grow(), desc="Grow window to the right"),
    # Floating
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating"),
    Key(
        [mod, "shift"],
        "f",
        lazy.layout.client_to_next().when(layout="stack"),
        desc="move to next",
    ),
    Key(
        [mod, "shift"],
        "a",
        lazy.layout.client_to_previous().when(layout="stack"),
        desc="move to previous",
    ),
    # Split
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    # Toggle Layouts
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    # Fullscreen
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    # System
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),
    Key(
        [mod, "control"],
        "q",
        lazy.spawn(home + "/dotfiles/qtile/scripts/powermenu.sh"),
        desc="Open Powermenu",
    ),
    Key(
        [mod, "shift"],
        "s",
        lazy.spawn(home + "/dotfiles/qtile/scripts/x11/barswitcher.sh"),
        desc="Switch Status Bar",
    ),
    # Apps
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key(
        [mod, "shift"],
        "space",
        lazy.spawn("rofi -show drun"),
        desc="Launch Rofi",
    ),
    Key(
        [mod],
        "b",
        lazy.spawn("sh " + home + "/dotfiles/.settings/browser.sh"),
        desc="Launch Browser",
    ),
    Key(
        [mod, "shift"],
        "w",
        lazy.spawn(home + "/dotfiles/qtile/scripts/x11/wallpaper.sh"),
        desc="Update Theme and Wallpaper",
    ),
    Key(
        [mod, "control"],
        "w",
        lazy.spawn(home + "/dotfiles/qtile/scripts/x11/wallpaper.sh select"),
        desc="Select Theme and Wallpaper",
    ),
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl -q s +20%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl -q s 20%-")),
]
logger.warning("Bindings")

# --------------------------------------------------------
# Groups
# --------------------------------------------------------

groups = [
    Group("1", layout="monadthreecol"),
    Group("2", layout="ratiotile"),
    Group("3", layout="ratiotile"),
    Group("4", layout="monadtall"),
    Group("5", layout="monadtall"),
]

dgroups_key_binder = simple_key_binder(mod)

# --------------------------------------------------------
# Scratchpads
# --------------------------------------------------------

logger.warning("Scratchpads")
scratch_pad_postions = {
    "docked": {
        "terminal": {
            "x": 0.3,
            "y": 0.1,
            "width": 0.40,
            "height": 0.7,
        },
        "slack": {
            "x": 0.69,
            "y": 0.05,
            "width": 0.3,
            "height": 0.7,
        },
        "spotify": {
            "x": 0.69,
            "y": 0.05,
            "width": 0.3,
            "height": 0.7,
        },
    },
    "mobile": {
        "terminal": {
            "x": 0.05,
            "y": 0.05,
            "width": 0.9,
            "height": 0.6,
        },
        "slack": {
            "x": 0.05,
            "y": 0.05,
            "width": 0.9,
            "height": 0.6,
        },
        "spotify": {
            "x": 0.05,
            "y": 0.05,
            "width": 0.9,
            "height": 0.6,
        },
    },
}

current_scratch_pad_postions = scratch_pad_postions["docked"]
groups.append(
    ScratchPad(
        "6",
        [
            DropDown(
                "terminal",
                "alacritty",
                on_focus_lost_hide=False,
                **current_scratch_pad_postions["terminal"],
            ),
            DropDown(
                "slack",
                "slack",
                on_focus_lost_hide=False,
                **current_scratch_pad_postions["slack"],
            ),
            DropDown(
                "spotify",
                "spotify",
                on_focus_lost_hide=False,
                **current_scratch_pad_postions["spotify"],
            ),
        ],
    )
)

keys.extend(
    [
        Key([mod], "z", lazy.group["6"].dropdown_toggle("terminal")),
        Key([mod], "s", lazy.group["6"].dropdown_toggle("slack")),
        Key([mod, "Shift"], "s", lazy.group["6"].dropdown_toggle("spotify")),
    ]
)

# --------------------------------------------------------


def hex_to_rgba(hex):
    hex = hex.lstrip("#")
    hlen = len(hex)
    return tuple(int(hex[i : i + hlen // 3], 16) for i in range(0, hlen, hlen // 3))


# --------------------------------------------------------
# Setup Layout Theme
# --------------------------------------------------------

layout_theme = {
    "border_width": 3,
    "margin": 10,
    "border_focus": "#ffffff",
    "border_normal": str(wal_colors.color0),
    "single_border_width": 3,
}

# --------------------------------------------------------
# Layouts
# --------------------------------------------------------

layouts = [
    layout.MonadThreeCol(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.RatioTile(**layout_theme),
    layout.Stack(**layout_theme),
    layout.Max(**layout_theme),
    layout.Floating(),
]

# --------------------------------------------------------
# Setup Widget Defaults
# --------------------------------------------------------

widget_defaults = dict(font="HackNerdFont SemiBold", fontsize=14, padding=3)
extension_defaults = widget_defaults.copy()

# --------------------------------------------------------
# Decorations
# https://qtile-extras.readthedocs.io/en/stable/manual/how_to/decorations.html
# --------------------------------------------------------
widget_list = get_widget_list()

# --------------------------------------------------------
# Screens
# --------------------------------------------------------

if wm_bar == "qtile":
    logger.warning("Loading qtile bar")
    screens = [
        Screen(
            top=bar.Bar(
                widget_list,
                40,
                opacity=0.95,
                border_width=[0, 0, 0, 0],
                margin=[0, 0, 0, 0],
                background=str(wal_colors.color0),
            ),
        ),
    ]
else:
    screens = [Screen(top=bar.Gap(size=28))]
    if core_name == "x11":
        screens = [Screen(top=bar.Gap(size=28))]
    else:
        screens = [Screen(top=bar.Gap(size=0))]

# --------------------------------------------------------
# Drag floating layouts
# --------------------------------------------------------

mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

# --------------------------------------------------------
# Define floating layouts
# --------------------------------------------------------

floating_layout = layout.Floating(
    border_width=3,
    border_focus=str(wal_colors.color7),
    border_normal=str(wal_colors.color0),
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ],
)

# --------------------------------------------------------
# General Setup
# --------------------------------------------------------

dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.

# --------------------------------------------------------
# Windows Manager Name
# --------------------------------------------------------

wmname = "QTILE"

# --------------------------------------------------------
# Set wayland properties
# --------------------------------------------------------

# Keyboard layout

# --------------------------------------------------------
# Hooks
# --------------------------------------------------------


# HOOK startup
@hook.subscribe.startup_once
def autostart():
    autostartscript = "~/.config/qtile/autostart_x11.sh"
    subprocess.Popen(["setxkbmap", keyboard_layout])

    home = os.path.expanduser(autostartscript)
    subprocess.Popen([home])
