
import gi

from VidLibWindow import VidLibWindow

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

win = VidLibWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()