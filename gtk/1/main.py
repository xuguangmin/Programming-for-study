#!/usr/bin/python

import sys
import gtk
class TutorialTextEditor:
    def on_window_destroy(self, widget, data=None):
        gtk.main_quit()
        def __init__(self):
            builder = gtk.Builder()
            builder.add_from_file("a.xml")
            self.window = builder.get_object("window")
            builder.connect_signals(self)
            if __name__ == "__main__":
                editor = TutorialTextEditor()
                editor.window.show()
                gtk.main()

