# -*- coding: utf-8 -*-
from libqtile.dgroups import simple_key_binder
import os
import re
import socket
import subprocess
from libqtile import qtile
from libqtile.config import Click, Drag, Group, KeyChord, Key, Match, Screen
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from typing import List  # noqa: F401from typing import List  # noqa: F401

mod = "mod1"              # Sets mod key to SUPER/WINDOWS
myTerm = "alacritty"      # My terminal of choice
myBrowser = "brave"  # My terminal of choice

keys = [
    # The essentials
    Key([mod], "Return",
        lazy.spawn(myTerm+" -e zsh"),
        desc='Launches My Terminal'
        ),
    Key([mod, "shift"], "Return",
        lazy.spawn("dmenu_run -p 'Run: '"),
        desc='Run Launcher'
        ),
    Key([mod], "b",
        lazy.spawn(myBrowser),
        desc='brave'
        ),
    Key([mod], "v",
        lazy.spawn("thunar"),
        desc='Launch File Browser'
        ),
    Key([mod], "Tab",
        lazy.next_layout(),
        desc='Toggle through layouts'
        ),
    Key([mod], "w",
        lazy.window.kill(),
        desc='Kill active window'
        ),
    Key([mod, "shift"], "r",
        lazy.restart(),
        desc='Restart Qtile'
        ),
    Key([mod, "shift"], "q",
        lazy.shutdown(),
        desc='Shutdown Qtile'
        ),
    # Window controls
    Key([mod], "j",
        lazy.layout.down(),
        desc='Move focus down in current stack pane'
        ),
    Key([mod], "k",
        lazy.layout.up(),
        desc='Move focus up in current stack pane'
        ),
    Key([mod, "shift"], "j",
        lazy.layout.shuffle_down(),
        lazy.layout.section_down(),
        desc='Move windows down in current stack'
        ),
    Key([mod, "shift"], "k",
        lazy.layout.shuffle_up(),
        lazy.layout.section_up(),
        desc='Move windows up in current stack'
        ),
    Key([mod], "h",
        lazy.layout.shrink(),
        lazy.layout.decrease_nmaster(),
        desc='Shrink window (MonadTall), decrease number in master pane (Tile)'
        ),
    Key([mod], "l",
        lazy.layout.grow(),
        lazy.layout.increase_nmaster(),
        desc='Expand window (MonadTall), increase number in master pane (Tile)'
        ),
    Key([mod], "n",
        lazy.layout.normalize(),
        desc='normalize window size ratios'
        ),
    Key([mod], "m",
        lazy.layout.maximize(),
        desc='toggle window between minimum and maximum sizes'
        ),
    Key([mod, "shift"], "f",
        lazy.window.toggle_floating(),
        desc='toggle floating'
        ),
    Key([mod], "f",
        lazy.window.toggle_fullscreen(),
        desc='toggle fullscreen'
        ),
    # Stack controls
    Key([mod, "shift"], "Tab",
        lazy.layout.rotate(),
        lazy.layout.flip(),
        desc='Switch which side main pane occupies (XmonadTall)'
        ),
    Key([mod], "space",
        lazy.layout.next(),
        desc='Switch window focus to other pane(s) of stack'
        ),
    Key([mod, "shift"], "space",
        lazy.layout.toggle_split(),
        desc='Toggle between split and unsplit sides of stack'
        ),
    Key([], "XF86MonBrightnessUp",
        lazy.spawn("brightnessctl -s set +10%"),
        desc='Increase Screen Brightness',
        ),
    Key([], "XF86MonBrightnessDown",
        lazy.spawn("brightnessctl -s set 10%-"),
        desc='Increase Screen Brightness',
        ),
    Key([], "XF86AudioLowerVolume",
        lazy.spawn("pulseaudio-ctl down"),
        desc='Decrease Volume by 5%',
        ),
    Key([], "XF86AudioRaiseVolume",
        lazy.spawn("pulseaudio-ctl up"),
        desc='Increase Volume up 5%',
        ),
    Key([], "XF86AudioMute",
        lazy.spawn("pulseaudio-ctl mute"),
        desc='Mute Audio',
        )
]

groups = [Group("1", layout='monadtall'),
          Group("2", layout='monadtall'),
          Group("3", layout='monadtall'),
          Group("4", layout='monadtall'),
          Group("5", layout='monadtall')]

# Allow MODKEY+[0 through 9] to bind to groups, see https://docs.qtile.org/en/stable/manual/config/groups.html
# MOD4 + index Number : Switch to Group[index]
# MOD4 + shift + index Number : Send active window to another Group
dgroups_key_binder = simple_key_binder(mod)

layout_theme = {"border_width": 2,
                "margin": 8,
                "border_focus": "5E81AC",
                "border_normal": "1D2330"
                }

layouts = [
    # layout.MonadWide(**layout_theme),
    # layout.Bsp(**layout_theme),
    #layout.Stack(stacks=2, **layout_theme),
    #layout.Columns(**layout_theme),
    # layout.RatioTile(**layout_theme),
    #layout.Tile(shift_windows=True, **layout_theme),
    # layout.VerticalTile(**layout_theme),
    # layout.Matrix(**layout_theme),
    # layout.Zoomy(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.Floating(**layout_theme)
]

colors = [["#2E3440","#2E3440"],
          ["#3B4252", "#3B4252"],
          ["#E5E9F0", "#E5E9F0"],
          ["#434C5E", "#434C5E"],
          ["#4C566A", "#4C566A"],
          ["#da8548", "#da8548"],
          ["#88C0D0", "#88C0D0"],
          ["#5E81AC", "#5E81AC"],
          ["#3B4252","#3B4252"],
          ["#2E3440","#2E3440"]]

prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

##### DEFAULT WIDGET SETTINGS #####
widget_defaults = dict(
    font="Ubuntu Bold",
    fontsize=12,
    padding=2,
    background=colors[2]
)
extension_defaults = widget_defaults.copy()


def init_widgets_list():
    widgets_list = [
        widget.Sep(
            linewidth=0,
            padding=6,
            foreground=colors[2],
            background=colors[0]
        ),
        widget.Image(
            filename="~/.config/qtile/icons/python-white.png",
            scale="False",
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(myTerm)}
        ),
        widget.Sep(
            linewidth=0,
            padding=6,
            foreground=colors[2],
            background=colors[0]
        ),
        widget.GroupBox(
            font="Ubuntu Bold",
            fontsize=14,
            margin_y=4,
            margin_x=5,
            padding_y=5,
            padding_x=3,
            borderwidth=2,
            active=colors[2],
            inactive=colors[7],
            rounded=False,
            highlight_color=colors[1],
            highlight_method="line",
            this_current_screen_border=colors[6],
            this_screen_border=colors[4],
            other_current_screen_border=colors[6],
            other_screen_border=colors[4],
            foreground=colors[2],
            background=colors[0]
        ),
        widget.TextBox(
            text='|',
            font="Ubuntu Mono",
            background=colors[0],
            foreground=colors[7],
            padding=2,
            fontsize=14
        ),
        #widget.CurrentLayout(
        #    foreground=colors[2],
        #    background=colors[0],
        #    padding=5
        #),
        widget.CurrentLayoutIcon(
            background=colors[0],
            scale=0.85
        ),
        widget.WindowName(
            foreground=colors[6],
            background=colors[0],
            fontsize=12,
            padding=20
        ),
        widget.Systray(
            background=colors[0],
            padding=2
        ),
        #widget.TextBox(
        #    text='|',
        #    font="Ubuntu Mono",
        #    background=colors[0],
        #    #foreground=colors[4],
        #    padding=0,
        #    fontsize=37
        #),
     #   widget.BatteryIcon(
     #       background=None,
     #       battery=0,
     #       theme_path='/usr/lib/python3.10/site-packages/libqtile/resources/battery-icons',
     #       update_iterval=60
     #   ),
        widget.Sep(
            linewidth=0,
            padding=8,
            foreground=colors[0],
            background=colors[0]
        ),
        #widget.TextBox(
        #    text='\uE0B2',
        #    font="Ubuntu Mono",
        #    background=colors[3],
        #    foreground=colors[0],
        #    padding=0,
        #    fontsize=37
        #),
        #widget.Net(
        #    interface="wlo1",
        #    format='Net: {down} ↓↑ {up}',
        #    foreground=colors[1],
        #    background=colors[3],
        #    padding=5
        #),
        widget.TextBox(
            text='|',
            font="Ubuntu Mono",
            background=colors[0],
            foreground=colors[6],
            padding=2,
            fontsize=14
        ),
        widget.ThermalSensor(
            foreground=colors[6],
            background=colors[0],
            threshold=90,
            fmt='Temp: {}',
            padding=5
        ),
        widget.TextBox(
            text='|',
            font="Ubuntu Mono",
            background=colors[0],
            foreground=colors[6],
            padding=2,
            fontsize=14
        ),
        widget.CryptoTicker(
            background=colors[0],
            foreground=colors[6],
            font="Ubuntu Bold",
            fontsize = 12,
            crypto='BTC',
            symbol='$',
            format='{crypto}: {symbol}{amount:.2f}',
            update_interval=600
        ),
        widget.TextBox(
            text='|',
            font="Ubuntu Mono",
            background=colors[0],
            foreground=colors[6],
            padding=2,
            fontsize=14
        ),
        widget.Memory(
            foreground=colors[6],
            background=colors[0],
            mouse_callbacks={
                'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e htop')},
            fmt='Mem: {}',
            padding=5
        ),
        widget.TextBox(
            text='|',
            font="Ubuntu Mono",
            background=colors[0],
            foreground=colors[6],
            padding=2,
            fontsize=14
        ),
        widget.Volume(
            foreground=colors[6],
            background=colors[0],
            fmt='Vol: {}',
            padding=5
        ),
        #widget.TextBox(
        #    text='\uE0B2',
        #    font="Ubuntu Mono",
        #    background=colors[7],
        #    foreground=colors[8],
        #    padding=0,
        #    fontsize=37
        #),
        #widget.KeyboardLayout(
        #    foreground=colors[1],
        #    background=colors[8],
        #    fmt='Keyboard: {}',
        #    padding=5
        #),
        widget.TextBox(
            text='|',
            font="Ubuntu Mono",
            background=colors[0],
            foreground=colors[6],
            padding=2,
            fontsize=14
        ),
        widget.Clock(
            foreground=colors[6],
            background=colors[0],
            format="%A, %B %d - %H:%M "
        )
    ]
    return widgets_list

def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    del widgets_screen1[9:10]               # Slicing removes unwanted widgets (systray) on Monitors 1,3
    return widgets_screen1

def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2                 # Monitor 2 will display all widgets in widgets_list

def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=1.0, size=20)),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), opacity=1.0, size=20)),
            Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=1.0, size=20))]

if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()
    widgets_screen2 = init_widgets_screen2()

def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)


def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)


mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    # default_float_rules include: utility, notification, toolbar, splash, dialog,
    # file_progress, confirm, download and error.
    *layout.Floating.default_float_rules,
    Match(title='Confirmation'),      # tastyworks exit box
    Match(title='Qalculate!'),        # qalculate-gtk
    Match(wm_class='kdenlive'),       # kdenlive
    Match(wm_class='pinentry-gtk-2'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True


@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
