from libqtile import widget
from qtile_extras import widget as ex_widget
from qtile_extras.widget.decorations import BorderDecoration, PowerLineDecoration
from conf.colors import WalColors
from conf.autorandr import get_autorandr_profile
from libqtile.log_utils import logger

wal_colors = WalColors()
decor_left = {
    "decorations": [
        PowerLineDecoration(path="forward_slash"),
        BorderDecoration(
            colour=str(wal_colors.color7), border_width=[0, 0, 4, 0], padding_x=5
        ),
    ],
}

decor_right = {
    "decorations": [
        PowerLineDecoration(path="back_slash"),
        BorderDecoration(
            colour=str(wal_colors.color7), border_width=[0, 0, 4, 0], padding_x=5
        ),
    ],
}


def get_widget_list():
    logger.warning(str(wal_colors.color1))
    profile = get_autorandr_profile()
    widget_list = []
    widget_list.append(
        ex_widget.CurrentLayoutIcon(
            **decor_left,
            background=str(wal_colors.color1),
        )
    )
    widget_list.append(
        widget.GroupBox(
            **decor_left,
            background=str(wal_colors.color1),
            highlight_method="block",
            highlight=str(wal_colors.color1),
            block_border=str(wal_colors.color1),
            highlight_color=[
                str(wal_colors.color1),
                str(wal_colors.color1),
            ],
            block_highlight_text_color=str(wal_colors.color1),
            foreground="ffffff",
            rounded=True,
            this_current_screen_border="ffffff",
            active="ffffff",
        )
    )
    widget_list.append(
        widget.TextBox(
            **decor_left,
            background=str(wal_colors.color1),
            text="  ",
            foreground="ffffff.6",
            fontsize=18,
            mouse_callbacks={
                "Button1": lambda: qtile.spawn(
                    "sh " + home + "/dotfiles/.settings/browser.sh"
                )
            },
        )
    )
    widget_list.append(
        widget.TextBox(
            **decor_left,
            background=str(wal_colors.color1),
            text="   ",
            foreground="ffffff.6",
            fontsize=18,
            mouse_callbacks={
                "Button1": lambda: qtile.spawn(
                    "sh " + home + "/dotfiles/.settings/filemanager.sh"
                )
            },
        )
    )
    widget_list.append(
        widget.WindowName(
            **decor_left,
            max_chars=50,
            background=str(wal_colors.color1),
            width=400,
            padding=10,
        )
    )
    widget_list.append(widget.Spacer())
    widget_list.append(
        widget.Spacer(decorations=[PowerLineDecoration(path="back_slash")], length=30)
    )
    if profile != "mobile":
        widget_list.append(
            widget.CPU(
                **decor_right,
                background=str(wal_colors.color1),
                padding=10,
                format="CPU {freq_current}GHz {load_percent}%",
            )
        )
    widget_list.append(
        widget.CPUGraph(
            **decor_right,
            background=str(wal_colors.color1),
            border_color=str(wal_colors.color3),
            graph_color=str(wal_colors.color3),
            padding=10,
            type="box",
        )
    )
    if profile != "mobile":
        widget_list.append(
            widget.Memory(
                **decor_right,
                background=str(wal_colors.color1),
                padding=10,
                measure_mem="G",
                format="{MemUsed:.0f}{mm}/{MemTotal:.0f}{mm}({MemPercent}%)",
            )
        )
    widget_list.append(
        widget.MemoryGraph(
            **decor_right,
            background=str(wal_colors.color1),
            border_color=str(wal_colors.color1),
            graph_color=str(wal_colors.color5),
            padding=10,
            type="box",
        )
    )
    widget_list.append(
        widget.Volume(
            **decor_right,
            background=str(wal_colors.color1),
            padding=10,
            fmt="Vol: {}",
        )
    )
    if profile != "mobile":
        widget_list.append(
            widget.DF(
                **decor_right,
                padding=10,
                background=str(wal_colors.color1),
                visible_on_warn=False,
                format="{p} {uf}{m} ({r:.0f}%)",
            )
        )
    widget_list.append(
        widget.Clock(
            **decor_right,
            background=str(wal_colors.color1),
            padding=10,
            format="%Y-%m-%d / %I:%M %p",
        ),
    )
    widget_list.append(
        ex_widget.UPowerWidget(
            battery_height=15,
            battery_name="BAT1",
            battery_width=40,
            border_charge_colour="#348502",
            border_colour="#348502",
            border_critical_colour="#348502",
            fill_charge="#348502",
            fill_critical="#cc0000",
            fill_low="#F1D70B",
            fill_normal="#348502",
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
    )
    widget_list.append(
        ex_widget.Systray(background=str(wal_colors.color1), padding=0),
    )
    widget_list.append(
        widget.TextBox(
            background=str(wal_colors.color1),
            padding=2,
        )
    )
    return widget_list
