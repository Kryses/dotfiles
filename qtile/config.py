#   ___ _____ ___ _     _____    ____             __ _
#  / _ \_   _|_ _| |   | ____|  / ___|___  _ __  / _(_) __ _
# | | | || |  | || |   |  _|   | |   / _ \| '_ \| |_| |/ _` |
# | |_| || |  | || |___| |___  | |__| (_) | | | |  _| | (_| |
#  \__\_\|_| |___|_____|_____|  \____\___/|_| |_|_| |_|\__, |
#                                                      |___/

# Icons: https://fontawesome.com/search?o=r&m=free

import os
import subprocess
import json
from libqtile import hook
from libqtile import qtile
from typing import List
from libqtile import bar, layout, widget
from libqtile.config import (
    Click,
    Drag,
    Group,
    Key,
    Match,
    Screen,
    DropDown,
    KeyChord,
    ScratchPad,
)
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.widget import Spacer, Backlight
from libqtile.widget.image import Image
from libqtile.dgroups import simple_key_binder
from pathlib import Path
from libqtile.log_utils import logger
from libqtile.backend.wayland import InputConfig

from qtile_extras import widget as ex_widget
from qtile_extras.widget.decorations import BorderDecoration, PowerLineDecoration


def get_autorandr_profile():
    return subprocess.check_output("autorandr --current", shell=True, text=True).strip()


keyboard_layout = "us"
# --------------------------------------------------------
# Your configuration
# --------------------------------------------------------

# Keyboard layout in conf/keyboard.py

# Show wlan status bar widget (set to False if wired network)
# show_wlan = True
autorandr_profile = get_autorandr_profile() or "docked"
show_wlan = True

# Show bluetooth status bar widget
# show_bluetooth = True
show_bluetooth = True

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
if core_name == "x11":
    try:
        wm_bar = Path(home + "/.cache/.qtile_bar_x11.sh").read_text().replace("\n", "")
    except Exception:
        wm_bar = "qtile"
elif qtile.core.name == "wayland":
    wm_bar = "qtile"
else:
    raise ValueError(f"{qtile.core.name} is invalid.")

logger.warning("Status bar: " + wm_bar)

# --------------------------------------------------------
# Check for Desktop/Laptop
# --------------------------------------------------------

# 3 = Desktop
platform = int(os.popen("cat /sys/class/dmi/id/chassis_type").read())

# --------------------------------------------------------
# Set default apps
# --------------------------------------------------------

terminal = "alacritty"

# --------------------------------------------------------
# Keybindings
# --------------------------------------------------------

mod = "mod4"  # SUPER KEY
alt_mod = "mod1"  # Alt Key

if core_name == "x11":
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
        Key(
            [mod, "control"], "Up", lazy.layout.grow(), desc="Grow window to the right"
        ),
        # Floating
        Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating"),
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
            [alt_mod],
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
elif qtile.core.name == "wayland":
    logger.warning("Using keys with wayland")

    keys = [
        # Focus
        Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
        Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
        Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
        Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
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
        Key(
            [mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"
        ),
        Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),
        # Swap
        Key([mod, "shift"], "h", lazy.layout.swap_left()),
        Key([mod, "shift"], "l", lazy.layout.swap_right()),
        Key(
            [mod],
            "Print",
            lazy.spawn(home + "/dotfiles/qtile/scripts/wayland/screenshot.sh"),
        ),
        # Size
        Key(
            [mod, "control"],
            "Down",
            lazy.layout.shrink(),
            desc="Grow window to the left",
        ),
        Key(
            [mod, "control"], "Up", lazy.layout.grow(), desc="Grow window to the right"
        ),
        Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
        Key(
            [mod], "m", lazy.layout.maximize(), desc="Toggle between min and max sizes"
        ),
        Key(
            [mod],
            "equal",
            lazy.layout.grow_left().when(layout=["bsp", "columns"]),
            lazy.layout.grow().when(layout=["monadtall", "monadwide"]),
            desc="Grow window to the left",
        ),
        Key(
            [mod],
            "minus",
            lazy.layout.grow_right().when(layout=["bsp", "columns"]),
            lazy.layout.shrink().when(layout=["monadtall", "monadwide"]),
            desc="Grow window to the left",
        ),
        # Floating
        Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating"),
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
        # Apps
        Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
        Key(
            [mod, "control"],
            "Return",
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
            lazy.spawn(home + "/dotfiles/qtile/scripts/wayland/wallpaper.sh"),
            desc="Update Theme and Wallpaper",
        ),
        Key(
            [mod, "control"],
            "w",
            lazy.spawn(home + "/dotfiles/qtile/scripts/wayland/wallpaper.sh select"),
            desc="Select Theme and Wallpaper",
        ),
        Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl -q s +20%")),
        Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl -q s 20%-")),
    ]

# --------------------------------------------------------
# Groups
# --------------------------------------------------------

groups = [
    Group("1", layout="monadtall"),
    Group("2", layout="monadtall"),
    Group("3", layout="monadtall"),
    Group("4", layout="monadtall"),
    Group("5", layout="monadtall"),
]

dgroups_key_binder = simple_key_binder(mod)

# --------------------------------------------------------
# Scratchpads
# --------------------------------------------------------

scratch_pad_postions = {
    "docked": {
        "chatgpt": {
            "x": 0.3,
            "y": 0.1,
            "width": 0.40,
            "height": 0.7,
        },
        "notes": {
            "x": 0.69,
            "y": 0.05,
            "width": 0.3,
            "height": 0.7,
        },
        "terminal": {
            "x": 0.3,
            "y": 0.1,
            "width": 0.40,
            "height": 0.7,
        },
        "vit": {
            "x": 0.05,
            "y": 0.05,
            "width": 0.20,
            "height": 0.6,
        },
        "scrcpy": {
            "x": 0.8,
            "y": 0.05,
            "width": 0.15,
            "height": 0.6,
        },
        "slack": {
            "x": 0.69,
            "y": 0.05,
            "width": 0.3,
            "height": 0.7,
        },
    },
    "mobile": {
        "chatgpt": {
            "x": 0.05,
            "y": 0.05,
            "width": 0.9,
            "height": 0.6,
        },
        "notes": {
            "x": 0.05,
            "y": 0.05,
            "width": 0.9,
            "height": 0.6,
        },
        "terminal": {
            "x": 0.05,
            "y": 0.05,
            "width": 0.9,
            "height": 0.6,
        },
        "vit": {
            "x": 0.05,
            "y": 0.05,
            "width": 0.9,
            "height": 0.6,
        },
        "scrcpy": {
            "x": 0.8,
            "y": 0.05,
            "width": 0.15,
            "height": 0.6,
        },
        "slack": {
            "x": 0.05,
            "y": 0.05,
            "width": 0.9,
            "height": 0.6,
        },
    },
}

current_scratch_pad_postions = scratch_pad_postions[autorandr_profile]
groups.append(
    ScratchPad(
        "6",
        [
            DropDown(
                "chatgpt",
                "qutebrowser --target window -R https://chat.openai.com",
                on_focus_lost_hide=False,
                **current_scratch_pad_postions["chatgpt"],
            ),
            DropDown(
                "notes",
                f"alacritty -e nvim '{home}/notes/kryses/index.norg'",
                on_focus_lost_hide=False,
                **current_scratch_pad_postions["notes"],
            ),
            DropDown(
                "terminal",
                "alacritty",
                on_focus_lost_hide=True,
                **current_scratch_pad_postions["terminal"],
            ),
            DropDown(
                "vit",
                "alacritty -e vit",
                on_focus_lost_hide=True,
                **current_scratch_pad_postions["vit"],
            ),
            DropDown(
                "scrcpy",
                "scrcpy -d",
                on_focus_lost_hide=False,
                **current_scratch_pad_postions["scrcpy"],
            ),
            DropDown(
                "slack",
                "slack",
                on_focus_lost_hide=False,
                **current_scratch_pad_postions["slack"],
            ),
        ],
    )
)

keys.extend(
    [
        Key([mod], "c", lazy.group["6"].dropdown_toggle("chatgpt")),
        Key([mod], "x", lazy.group["6"].dropdown_toggle("notes")),
        Key([mod], "z", lazy.group["6"].dropdown_toggle("terminal")),
        Key([mod], "v", lazy.group["6"].dropdown_toggle("vit")),
        Key([mod], "a", lazy.group["6"].dropdown_toggle("scrcpy")),
        Key([mod], "s", lazy.group["6"].dropdown_toggle("slack")),
    ]
)


# --------------------------------------------------------
# Pywal Colors
# --------------------------------------------------------
def hex_to_rgba(hex):
    logger.info(f"hex_to_rgba: {hex}")
    hex = hex.lstrip("#")
    hlen = len(hex)
    return tuple(int(hex[i : i + hlen // 3], 16) for i in range(0, hlen, hlen // 3))


colors = os.path.expanduser("~/.cache/wal/colors.json")
colordict = json.load(open(colors))
Color0 = hex_to_rgba(colordict["colors"]["color0"])
Color1 = hex_to_rgba(colordict["colors"]["color1"])
Color2 = hex_to_rgba(colordict["colors"]["color2"])
Color3 = hex_to_rgba(colordict["colors"]["color3"])
Color4 = hex_to_rgba(colordict["colors"]["color4"])
Color5 = hex_to_rgba(colordict["colors"]["color5"])
Color6 = hex_to_rgba(colordict["colors"]["color6"])
Color7 = hex_to_rgba(colordict["colors"]["color7"])
Color8 = hex_to_rgba(colordict["colors"]["color8"])
Color9 = hex_to_rgba(colordict["colors"]["color9"])
Color10 = hex_to_rgba(colordict["colors"]["color10"])
Color11 = hex_to_rgba(colordict["colors"]["color11"])
Color12 = hex_to_rgba(colordict["colors"]["color12"])
Color13 = hex_to_rgba(colordict["colors"]["color13"])
Color14 = hex_to_rgba(colordict["colors"]["color14"])
Color15 = hex_to_rgba(colordict["colors"]["color15"])


# --------------------------------------------------------
# Setup Layout Theme
# --------------------------------------------------------

layout_theme = {
    "border_width": 3,
    "margin": 10,
    "border_focus": "#ffffff",
    "border_normal": Color6,
    "single_border_width": 3,
}

# --------------------------------------------------------
# Layouts
# --------------------------------------------------------

layouts = [
    layout.Max(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
    layout.RatioTile(**layout_theme),
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

decor_left = {
    "decorations": [
        PowerLineDecoration(path="forward_slash", shift=5),
        BorderDecoration(colour=Color7, border_width=[0, 0, 4, 0], padding_x=5),
    ],
}

decor_right = {
    "decorations": [
        PowerLineDecoration(path="back_slash"),
        BorderDecoration(colour=Color7, border_width=[0, 0, 4, 0], padding_x=5),
    ],
}

# --------------------------------------------------------
# Widgets
# --------------------------------------------------------

widget_list = [
    ex_widget.CurrentLayoutIcon(
        **decor_left,
        background=Color1,
    ),
    widget.GroupBox(
        **decor_left,
        background=(0.0, 0.0, 0.0, 0.0),
        highlight_method="block",
        highlight=Color8 + ".5",
        block_border=Color1,
        highlight_color=[Color8 + ".5", Color8 + ".5"],
        block_highlight_text_color="000000",
        foreground="ffffff",
        rounded=True,
        this_current_screen_border="ffffff",
        active="ffffff",
    ),
    widget.TextBox(
        **decor_left,
        background=Color1 + ".8",
        text="  ",
        foreground="ffffff.6",
        fontsize=18,
        mouse_callbacks={
            "Button1": lambda: qtile.spawn(
                "sh " + home + "/dotfiles/.settings/browser.sh"
            )
        },
    ),
    widget.TextBox(
        **decor_left,
        background=Color1 + ".6",
        text="   ",
        foreground="ffffff.6",
        fontsize=18,
        mouse_callbacks={
            "Button1": lambda: qtile.spawn(
                "sh " + home + "/dotfiles/.settings/filemanager.sh"
            )
        },
    ),
    widget.WindowName(
        **decor_left, max_chars=50, background=Color1 + ".4", width=400, padding=10
    ),
    widget.Spacer(),
    widget.Spacer(decorations=[PowerLineDecoration(path="back_slash")], length=30),
    widget.CPU(
        **decor_right,
        background=Color6 + ".4",
        padding=10,
        format="CPU {freq_current}GHz {load_percent}%",
    ),
    widget.CPUGraph(
        **decor_right,
        background=Color6 + ".4",
        border_color=Color3 + ".8",
        graph_color=Color3,
        padding=10,
        type="box",
    ),
    widget.Memory(
        **decor_right,
        background=Color6 + ".6",
        padding=10,
        measure_mem="G",
        format="{MemUsed:.0f}{mm}/{MemTotal:.0f}{mm}({MemPercent}%)",
    ),
    widget.MemoryGraph(
        **decor_right,
        background=Color6 + ".6",
        border_color=Color6 + ".6",
        graph_color=Color5,
        padding=10,
        type="box",
    ),
    widget.Volume(
        **decor_right,
        background=Color6 + ".8",
        padding=10,
        fmt="Vol: {}",
    ),
    widget.DF(
        **decor_right,
        padding=10,
        background=Color6 + ".8",
        visible_on_warn=False,
        format="{p} {uf}{m} ({r:.0f}%)",
    ),
    widget.Clock(
        **decor_right,
        background=Color6,
        padding=10,
        format="%Y-%m-%d / %I:%M %p",
    ),
    ex_widget.UPowerWidget(
        background=Color6,
        battery_height=15,
        battery_name="BAT1",
        battery_width=40,
        border_charge_colour=Color6,
        border_colour=Color6,
        border_critical_colour=Color6,
        fill_charge="#348502.9",
        fill_critical="#cc0000.9",
        fill_low="#F1D70B.9",
        fill_normal=Color6,
        font="sans",
        fontsize=None,
        foreground="ffffff",
        margin=5,
        mouse_callbacks={},
        percentage_critical=0.1,
        percentage_low=0.2,
        spacing=10,
        text_charging="({percentage:.0f}%) {ttf} until fully charged",
        text_discharging="({percentage:.0f}%) {tte} until empty",
        text_displaytime=5,
    ),
    widget.TextBox(
        **decor_right,
        background=Color6,
        padding=5,
        text=" ",
        fontsize=20,
        mouse_callbacks={
            "Button1": lambda: qtile.spawn(
                home + "/dotfiles/qtile/scripts/powermenu.sh"
            )
        },
    ),
    ex_widget.Systray(background=Color6, padding=0),
    widget.TextBox(
        background=Color6,
        padding=2,
    ),
]

# --------------------------------------------------------
# Screens
# --------------------------------------------------------

if wm_bar == "qtile":
    logger.warning("Loading qtile bar")
    screens = [
        Screen(
            top=bar.Bar(
                widget_list,
                30,
                padding=20,
                opacity=0.7,
                border_width=[0, 0, 0, 0],
                margin=[0, 0, 0, 0],
                background="#000000.3",
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
    border_focus="FFFFFF",
    border_normal=Color2,
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
wl_input_rules = {
    "type:keyboard": InputConfig(kb_layout=keyboard_layout),
}

# --------------------------------------------------------
# Hooks
# --------------------------------------------------------


# HOOK startup
@hook.subscribe.startup_once
def autostart():
    if qtile.core.name == "x11":
        autostartscript = "~/.config/qtile/autostart_x11.sh"
        subprocess.Popen(["setxkbmap", keyboard_layout])
    elif qtile.core.name == "wayland":
        autostartscript = "~/.config/qtile/autostart_wayland.sh"
    else:
        raise ValueError(f"{qtile.core.name} is invalid")

    home = os.path.expanduser(autostartscript)
    subprocess.Popen([home])
