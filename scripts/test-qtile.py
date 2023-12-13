#!python3
from icecream import ic
from libqtile.core.manager import Qtile

manager = Qtile
ic(manager.list_widgets())
