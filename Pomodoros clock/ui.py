import timeout
import tkinter as tk

class TimeoutUI:

    def __init__ (self, parent):
        self.container = tk.Frame (parent)
        self.container.pack ()
        self.parent = parent
        self.clock_format = "%D:%H:s"
        self.label_clock = tk.Label (font = "Verdana 64")
        self.label_clock.pack ()
        self.button_activate = tk.Button (text = "Activate", command = self.activate_timeout)
        self.button_activate.pack ()
        self._job = None
        

    def activate_timeout (self):
        self.timeout = timeout.Timeout ()
        self.timeout.set_new_timeout (minutes = 25)
        self.timeout.activate_timeout ()
        self.update_clock ()

        
    def update_clock (self):

        if self._job:
            root.after_cancel (self._job)
        
        _timeout = self.timeout.update ()
        if _timeout:
            self.label_clock.configure (text = self.strftime (_timeout))
            self._job = root.after (100, self.update_clock)
        else:
            self.label_clock.configure (text = "Timeout...")

            
    def strftime (self, timeout_datetime):
        # thanks to http://stackoverflow.com/questions/538666/python-format-timedelta-to-string
        hour, remainder = divmod (timeout_datetime.seconds, 3600)
        minutes, seconds = divmod (remainder, 60)
        return str (timeout_datetime.days) + ":" + \
            str (hour) + ":" + \
            str (minutes) + ":" + \
            str (seconds)
    
        


root = tk.Tk()
app = TimeoutUI (None)
root.mainloop ()
