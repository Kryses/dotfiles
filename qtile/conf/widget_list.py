from libqtile import widget
from qtile_extras import widget as ex_widget
from qtile_extras.widget.decorations import PowerLineDecoration, BorderDecoration
from qtile_extras.widget import modify
from kryslib.colors.wal_colors import WalColors
from kryslib.colors.color import Color
from pathlib import Path


wal_colors = WalColors(walcolor_json=Path.home() / ".cache/wal/colors.json")
decor_left = {
    "decorations": [
        PowerLineDecoration(
            path="back_slash",
            use_widget_background=True,
            filled=True,
        ),
        BorderDecoration(
            colour=str(wal_colors.color7), border_width=[0, 0, 4, 0], padding_x=1
        ),
    ],
}

decor_right = {
    "decorations": [
        PowerLineDecoration(
            path="forward_slash",
            use_widget_background=True,
            filled=True,
        ),
        BorderDecoration(
            colour=str(wal_colors.color7), border_width=[0, 0, 4, 0], padding_x=1
        ),
    ],
}

FORGROUND = wal_colors.color7
BACKGROUND = wal_colors.color5


def get_widget_list():
    profile = "docked"
    widget_list = []
    widget_list.append(
        ex_widget.CurrentLayoutIcon(
            **decor_left,
            background=str(BACKGROUND.scale(1.0)),
            padding=10,
            scale=0.7,
        )
    )
    widget_list.append(
        modify(
            widget.GroupBox,
            **decor_left,
            padding_x=10,
            padding_y=5,
            background=str(BACKGROUND.scale(0.8)),
            highlight_method="block",
            highlight=str(FORGROUND),
            block_border=str(FORGROUND),
            highlight_color=[
                str(FORGROUND),
                str(FORGROUND),
            ],
            block_highlight_text_color=str(FORGROUND.scale(0.5)),
            other_screen_border=str(BACKGROUND.scale(0.5)),
            foreground=str(FORGROUND),
            rounded=True,
            this_current_screen_border=str(FORGROUND),
            active=str(FORGROUND),
        )
    )
    widget_list.append(
        modify(
            widget.TextBox,
            **decor_left,
            background=str(BACKGROUND.scale(0.6)),
            text="  ",
            foreground=str(FORGROUND),
            fontsize=18,
            mouse_callbacks={
                "Button1": lambda: qtile.spawn(
                    "sh " + home + "/dotfiles/.settings/browser.sh"
                )
            },
        )
    )
    widget_list.append(
        modify(
            widget.TextBox,
            **decor_left,
            background=str(BACKGROUND.scale(0.6)),
            text="  ",
            foreground=str(FORGROUND),
            fontsize=18,
            mouse_callbacks={
                "Button1": lambda: qtile.spawn(
                    "sh " + home + "/dotfiles/.settings/filemanager.sh"
                )
            },
        )
    )
    widget_list.append(
        modify(
            widget.WindowName,
            **decor_left,
            width=350,
            max_chars=40,
            background=str(BACKGROUND.scale(0.4)),
        )
    )
    widget_list.append(widget.Spacer())
    widget_list.append(
        widget.TextBox(
            decorations=[
                PowerLineDecoration(
                    path="forward_slash",
                    use_widget_background=True,
                    filled=True,
                ),
            ],
            background=str(wal_colors.color0),
        )
    )
    if profile != "mobile":
        widget_list.append(
            widget.CPU(
                **decor_right,
                background=str(BACKGROUND.scale(0.4)),
                format="CPU {freq_current}GHz {load_percent}%",
            )
        )
    widget_list.append(
        modify(
            widget.CPUGraph,
            **decor_right,
            background=str(BACKGROUND.scale(0.4)),
            border_color=str(FORGROUND),
            graph_color=str(FORGROUND),
            type="box",
        )
    )
    if profile != "mobile":
        widget_list.append(
            modify(
                widget.Memory,
                **decor_right,
                background=str(BACKGROUND.scale(0.5)),
                padding=10,
                measure_mem="G",
                format="{MemUsed:.0f}{mm}/{MemTotal:.0f}{mm}({MemPercent}%)",
            )
        )
    widget_list.append(
        modify(
            widget.MemoryGraph,
            **decor_right,
            background=str(BACKGROUND.scale(0.5)),
            border_color=str(FORGROUND),
            graph_color=str(FORGROUND),
            padding=10,
            type="box",
        )
    )
    widget_list.append(
        modify(
            widget.Volume,
            **decor_right,
            background=str(BACKGROUND.scale(0.6)),
            padding=10,
            fmt="Vol: {}",
        )
    )
    if profile != "mobile":
        widget_list.append(
            modify(
                widget.DF,
                **decor_right,
                padding=10,
                background=str(BACKGROUND.scale(0.7)),
                visible_on_warn=False,
                format="{p} {uf}{m} ({r:.0f}%)",
            )
        )
    widget_list.append(
        modify(
            widget.Clock,
            **decor_right,
            background=str(BACKGROUND.scale(0.8)),
            padding=10,
            format="%Y-%m-%d / %I:%M %p",
        )
    )
    battery_charge_color = BACKGROUND + Color((0, 255, 0, 255))
    battery_discharge_color = BACKGROUND + Color((0, 100, 255, 255))
    widget_list.append(
        modify(
            ex_widget.UPowerWidget,
            **decor_right,
            battery_height=15,
            battery_name="BAT1",
            battery_width=40,
            background=str(BACKGROUND.scale(0.9)),
            border_charge_colour=str(battery_charge_color.scale(0.5)),
            border_colour=str(battery_discharge_color.scale(0.5)),
            border_critical_colour="#348502",
            fill_charge=str(BACKGROUND + Color((0, 255, 0, 255))),
            fill_critical="#cc0000",
            fill_low="#F1D70B",
            fill_normal=str(battery_discharge_color),
            font="Hack Nerd Font",
            fontsize=None,
            foreground=str(FORGROUND),
            margin=5,
            mouse_callbacks={},
            percentage_critical=0.1,
            percentage_low=0.2,
            spacing=10,
            text_charging="({percentage:.0f}%) {ttf} until fully charged",
            text_discharging="({percentage:.0f}%) {tte} until empty",
            text_displaytime=5,
        )
    )
    widget_list.append(
        modify(
            widget.Systray,
            **decor_right,
            background=str(BACKGROUND),
            padding=0,
        )
    )
    widget_list.append(
        widget.TextBox(
            background=str(BACKGROUND),
            padding=2,
        )
    )
    return widget_list
