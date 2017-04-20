import timeout
import tkinter as tk

class TimeoutUI:

    def __init__ (self, parent):

        self.inputs = dict()
        
        self.container = tk.Frame (parent)
        self.container.pack ()
        self.parent = parent
        self.clock_format = "%D:%H:s"
        self._job = None

        self.label_clock = tk.Label (font = "Verdana 64")
        self.label_clock.pack ()
        self.button_activate = tk.Button (text = "Activate", command = self.activate_timeout)
        self.button_activate.pack ()

        self.label_time = tk.Label (text = "Enter a time:")
        self.label_time.pack (side = tk.LEFT)

        self.inputs["entry_time"] = tk.StringVar ()
        self.inputs["entry_time"].set ("D:H:M:s")
        self.entry_time = tk.Entry (width = 25, textvariable = self.inputs["entry_time"])
        # self.entry_time.insert (tk.INSERT
        self.entry_time.pack (side = tk.LEFT)

        self.button_ok_time = tk.Button (text = "Ok", callback = activate_timeout ())
        self.button_ok_time.pack (side = tk.RIGHT)
        

    def get_time_entry ():

        tmp = self.inputs["entry_time"].split (":")

        # if len (tmp) > 4
        
        
        

    def activate_timeout (self):

        self.control_time_entry ()
        
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
