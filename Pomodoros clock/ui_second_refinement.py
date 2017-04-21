import timeout
import tkinter as tk

class TimeEntryException (Exception):
    """Define an exception that is  thrown for invalid time strings."""

class TimeoutUI:

    def __init__ (self, parent):

        self.inputs = dict() # set up a diction to contain references to \
                      # dynamic variables (stringvar and so on)
        
        self.container = tk.Frame (parent)
        self.container.grid ()
        self.parent = parent
        self.clock_format = "%D:%H:s"
        self._job = None # define the timer job

        self.label_clock = tk.Label (font = "Verdana 64", text = "D:H:m:s")
        self.label_clock.grid (row = 0, column = 0, columnspan = 3)
        
        self.label_time = tk.Label (text = "Enter a time:")
        self.label_time.grid (row = 1, column = 0) 

        self.inputs["entry_time"] = tk.StringVar ()
        self.inputs["entry_time"].set ("D:H:M:s")
        self.entry_time = tk.Entry (width = 25, textvariable = self.inputs["entry_time"])
        self.entry_time.grid (row = 1, column = 1)

        self.inputs["error_entry_time"] = tk.StringVar ()
        self.inputs["error_entry_time"].set ("Error")
        self.label_error_entry_time = tk.Label (textvariable = self.inputs["error_entry_time"], foreground = "red", font = "Times")
        self.label_error_entry_time.grid (row = 1, column = 2)
        self.label_error_entry_time.grid_forget ()

        self.button_ok_time = tk.Button (text = "Ok", command = self.activate_timeout)
        self.button_ok_time.grid (row = 2, column = 1)
        

    def get_time_entry (self):
        tmp = self.inputs["entry_time"].get().split (":")

        if len (tmp) > 4:
            raise TimeEntryException ("Time string cannot have more than 4 time slots (D:H:M:s).")

        tmp.reverse ()
        timeout = [0] * 4
        
        for el in range (0, len(tmp)):
            timeout[el] = int(tmp[el])

        return timeout[3], timeout[2], timeout[1], timeout[0]
        
        
    def activate_timeout (self):

        try:
            days, hours, minutes, seconds = self.get_time_entry ()
            
            self.label_error_entry_time.grid_forget ()
            
            self.timeout = timeout.Timeout ()
            self.timeout.set_new_timeout (days, hours, minutes, seconds)
            self.timeout.activate_timeout ()
            self.update_clock ()

        except Exception:
            self.label_error_entry_time.grid (row = 1, column = 2)
            

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
root.wm_title ("Pomodoro clock")
app = TimeoutUI (None)
root.mainloop ()
