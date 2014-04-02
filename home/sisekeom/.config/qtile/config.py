from libqtile.config import Key, Screen, Group
from libqtile.command import lazy
from libqtile import bar, hook, layout, widget
from subprocess import call
import subprocess, re

mod = "mod4"

def is_running(process):
    s = subprocess.Popen(["ps", "axw"], stdout=subprocess.PIPE)
    for x in s.stdout:
        if re.search(process, x):
            return True
    return False

def execute_once(process):
    if not is_running(process):
        return subprocess.Popen(process.split())



keys = [
    # Switch between windows in current stack pane
    Key(
        [mod], "k",
        lazy.layout.down()
    ),
    Key(
        [mod], "j",
        lazy.layout.up()
    ),

    # Move windows up or down in current stack
    Key(
        [mod, "control"], "k",
        lazy.layout.shuffle_down()
    ),
    Key(
        [mod, "control"], "j",
        lazy.layout.shuffle_up()
    ),

    # Switch window focus to other pane(s) of stack
    Key(
        [mod], "space",
        lazy.layout.next()
    ),

    # Swap panes of split stack
    Key(
        [mod, "shift"], "space",
        lazy.layout.rotate()
    ),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"], "Return",
        lazy.layout.toggle_split()
    ),
    Key([mod], "Return", lazy.spawn("termite")),

    # Toggle between different layouts as defined below
    Key([mod], "Tab",    lazy.nextlayout()),
    Key([mod], "w",      lazy.window.kill()),

    Key([mod, "control"], "r", lazy.restart()),
    Key([mod], "r", lazy.spawncmd()),
    # Brightness
    Key([],"XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 7")),
    Key([],"XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 7")),
]

groups = [
    Group("1"),
    Group("2"),
    Group("3"),
    Group("4"),
    Group("5"),
    Group("6"),
    Group("7"),
    Group("8"),
]
for i in groups:
    # mod1 + letter of group = switch to group
    keys.append(
        Key([mod], i.name, lazy.group[i.name].toscreen())
    )

    # mod1 + shift + letter of group = switch to & move focused window to group
    keys.append(
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name))
    )

dgroups_key_binder = None
dgroups_app_rules = []

layouts = [
    layout.Max(),
    layout.Stack(stacks=2)
]

default_data = dict(fontsize=12,
                    foreground="FFFFFF",
                    background="1D1D1D",
                    font="ttf-droid")

data_clock = dict(fontsize=12,
                    foreground="4EE9FE",
                    background="1D1D1D",
                    font="ttf-droid")

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(**default_data),
                widget.Prompt(**default_data),
                widget.WindowName(**default_data),
                widget.Sep(**default_data),
#                widget.TaskList(),
                widget.Sep(**default_data),
                widget.Systray(**default_data),
                widget.Clock('%d-%m-%Y   ||   %I:%M %p',**data_clock),
            ],
            27,
        ),
    ),
]

main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating()
mouse = ()
auto_fullscreen = True
widget_defaults = {}


@hook.subscribe.client_new
def floating_dialogs(window):
    dialog = window.window.get_wm_type() == 'dialog'
    transient = window.window.get_wm_transient_for()
    if dialog or transient:
        window.floating = True


@hook.subscribe.startup
def setWmname():
    execute_once("wmname LG3D")
    execute_once("setxkbmap es")

@hook.subscribe.startup
def init_brightness():
    execute_once("xbacklight -set 15")

@hook.subscribe.startup
def setWallpaper():
    execute_once("feh --bg-scale /home/sisekeom/Wallpapers/Arch.jpeg")
