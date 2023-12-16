from libqtile import widget
from qtile_extras import widget as ex_widget
from conf.colors import WalColors

decor_left = {
    "decorations": [
        PowerLineDecoration(path="forward_slash", shift=5),
        BorderDecoration(
            colour=WalColors.color7, border_width=[0, 0, 4, 0], padding_x=5
        ),
    ],
}

decor_right = {
    "decorations": [
        PowerLineDecoration(path="back_slash"),
        BorderDecoration(
            colour=WalColors.color7, border_width=[0, 0, 4, 0], padding_x=5
        ),
    ],
}


def get_widget_list():
    widget_list = []
    widget_list.append(
        ex_widget.CurrentLayoutIcon(
            **decor_left,
            background=WalColors.color1,
        )
    )
    widget_list.append(
        widget.GroupBox(
            **decor_left,
            background=(0.0, 0.0, 0.0, 0.0),
            highlight_method="block",
            highlight=WalColors.color8 + ".5",
            block_border=WalColors.color1,
            highlight_color=[WalColors.color8 + ".5", WalColors.color8 + ".5"],
            block_highlight_text_color="000000",
            foreground="ffffff",
            rounded=True,
            this_current_screen_border="ffffff",
            active="ffffff",
        )
    )
    widget_list.append(
        widget.TextBox(
            **decor_left,
            background=WalColors.color1 + ".8",
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
            background=WalColors.color1 + ".6",
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
            background=WalColors.color1 + ".4",
            width=400,
            padding=10,
        )
    )
    widget_list.append(widget.Spacer())
    widget_list.append(
        widget.Spacer(decorations=[PowerLineDecoration(path="back_slash")], length=30)
    )
    widget_list.append(
        widget.CPU(
            **decor_right,
            background=WalColors.color6 + ".4",
            padding=10,
            format="CPU {freq_current}GHz {load_percent}%",
        )
    )
    widget_list.append(
        widget.CPUGraph(
            **decor_right,
            background=WalColors.color6 + ".4",
            border_color=WalColors.color3 + ".8",
            graph_color=WalColors.color3,
            padding=10,
            type="box",
        )
    )
    widget_list.append(
        widget.Memory(
            **decor_right,
            background=WalColors.color6 + ".6",
            padding=10,
            measure_mem="G",
            format="{MemUsed:.0f}{mm}/{MemTotal:.0f}{mm}({MemPercent}%)",
        )
    )
    widget_list.append(
        widget.MemoryGraph(
            **decor_right,
            background=WalColors.color6 + ".6",
            border_color=WalColors.color6 + ".6",
            graph_color=WalColors.color5,
            padding=10,
            type="box",
        )
    )
    widget_list.append(
        widget.Volume(
            **decor_right,
            background=WalColors.color6 + ".8",
            padding=10,
            fmt="Vol: {}",
        )
    )
    widget_list.append(
        widget.DF(
            **decor_right,
            padding=10,
            background=WalColors.color6 + ".8",
            visible_on_warn=False,
            format="{p} {uf}{m} ({r:.0f}%)",
        )
    )
    widget_list.append(
        widget.Clock(
            **decor_right,
            background=WalColors.color6,
            padding=10,
            format="%Y-%m-%d / %I:%M %p",
        ),
    )
    widget_list.append(
        ex_widget.UPowerWidget(
            background=WalColors.color6,
            battery_height=15,
            battery_name="BAT1",
            battery_width=40,
            border_charge_colour=WalColors.color6,
            border_colour=WalColors.color6,
            border_critical_colour=WalColors.color6,
            fill_charge="#348502.9",
            fill_critical="#cc0000.9",
            fill_low="#F1D70B.9",
            fill_normal=WalColors.color6,
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
        ex_widget.Systray(background=WalColors.color6, padding=0),
    )
    widget_list.append(
        widget.TextBox(
            background=WalColors.color6,
            padding=2,
        )
    )
    return widget_list
