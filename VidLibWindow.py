import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class VidLibWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="VidLib")

        self.button = Gtk.Button(label="Click Here")
        self.button.connect("clicked", self.on_button_clicked)
        self.add(self.button)

    def on_button_clicked(self, widget):
        print("Hello World")