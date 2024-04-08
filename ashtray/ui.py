import subprocess

import gi  # noqa
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk  # noqa
from gi.repository import GdkPixbuf  # noqa


class TrayItem:
    def __init__(self, icon_path, command):
        self._proc = None
        self._icon_path = icon_path
        self._command = command.split()

        self._tray = self._build_status_icon()
        self._menu = self._build_popup_menu()
        self._tray.connect("popup-menu", self.on_popup__activate)

    def _build_status_icon(self):
        img = GdkPixbuf.Pixbuf.new_from_file(self._icon_path)
        tray = Gtk.StatusIcon.new_from_pixbuf(img)
        tray.connect("activate", self.on_activate)
        return tray

    def _build_popup_menu(self):
        menu = Gtk.Menu()

        show = Gtk.MenuItem.new_with_label("Show")
        show.connect("activate", self.on_activate)
        menu.append(show)

        quit = Gtk.MenuItem.new_with_label("Quit")
        quit.connect("activate", self.on_popup__quit)
        menu.append(quit)

        menu.show_all()
        return menu

    def on_activate(self, *args):
        if self._proc is not None:
            self._proc.poll()

        if self._proc is None or self._proc.returncode is not None:
            self._proc = subprocess.Popen(self._command)

    def on_popup__activate(self, icon, button, time):
        self._menu.popup(None, None, None, self._tray, button, time)

    def on_popup__quit(self, *args):
        self.cleanup()
        Gtk.main_quit()

    def cleanup(self):
        if self._proc:
            self._proc.terminate()

    def start(self):
        try:
            Gtk.main()
        except KeyboardInterrupt:
            self.cleanup()
