# ashtray

Create tray icons in gnome-shell panel.

For 99% of the users, see [these alternatives](#Alternatives).


Important: the Gtk/Gdk api is deprecated.


## Install

For system dependencies, see [pygobject](https://gnome.pages.gitlab.gnome.org/pygobject/getting_started.html#).

```bash
pipx install git+https://github.com/georgeyk/ashtray
```

## Usage

```bash
ashtray desktop -f /usr/share/applications/org.gnome.Cheese.desktop
```

To autostart, in `~/.config/autostart` create a desktop file similar to:

```
[Desktop Entry]
Type=Application
Exec=ashtray desktop -f /usr/share/applications/org.gnome.Cheese.desktop
Name=Cheese
X-Gnome-AutoStart-enabled=true
```

## Alternatives

- [Gnome extension launcher](https://extensions.gnome.org/extension/5874/launcher/)
- [Tray Icons Reloaded](https://github.com/MartinPL/Tray-Icons-Reloaded)
