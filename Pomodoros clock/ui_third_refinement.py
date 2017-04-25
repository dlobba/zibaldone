import timeout
import tkinter as tk

class TimeEntryException (Exception):
    """Define an exception that is  thrown for invalid time strings."""

class TimeoutUI (tk.Frame):

    ERROR_STYLE = "Times"
    CLOCK_STYLE = "Verdana 64"
    
    def __init__ (self, parent):

        self.parent = parent
        tk.Frame.__init__ (self, self.parent)
        self.grid (row = 0, column = 0)
        
        self.inputs = dict() # set up a dictionary to contain references to \
                      # dynamic variables (stringvar and so on)
        
        self._job = None # define the timer job

        self.label_clock = tk.Label (self, font = self.CLOCK_STYLE, text = "D:H:m:s")
        self.label_time = tk.Label (self, text = "Enter a time:")

        self.inputs["entry_time"] = tk.StringVar (self)
        self.inputs["entry_time"].set ("D:H:M:s")
        self.entry_time = tk.Entry (self, width = 25, textvariable = self.inputs["entry_time"])

        self.inputs["error_entry_time"] = tk.StringVar ()
        self.inputs["error_entry_time"].set ("Error")
        self.label_error_entry_time = tk.Label (self, textvariable = self.inputs["error_entry_time"], foreground = "red", font = self.ERROR_STYLE)
        
        self.button_ok_time = tk.Button (self, text = "Ok", command = self.activate_timeout)

        self.label_clock.grid (row = 0, column = 0, columnspan = 3, sticky = tk.N + tk.S + tk.E + tk.W)
        self.label_time.grid (row = 1, column = 0, sticky = tk.N + tk.S + tk.E + tk.W) 
        self.entry_time.grid (row = 1, column = 1, sticky = tk.N + tk.S + tk.E + tk.W)
        self.label_error_entry_time.grid (row = 1, column = 2, sticky = tk.N + tk.S + tk.E + tk.W)
        self.label_error_entry_time.grid_forget ()
        self.button_ok_time.grid (row = 2, column = 1, sticky = tk.N + tk.S + tk.E + tk.W)

        # configure resize behaviour
        self.parent.rowconfigure (0, weight = 10)
        self.parent.rowconfigure (1, weight = 1)
        self.parent.rowconfigure (2, weight = 1)
        
        self.parent.columnconfigure (0, weight = 10)
        self.parent.columnconfigure (1, weight = 1)
        self.parent.columnconfigure (2, weight = 1)
        
        
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

        except TimeEntryException:
            self.inputs["error_entry_time"].set ("Timeout has maximum 4 fields")
            self.label_error_entry_time.grid (row = 1, column = 2)

        except ValueError:
            self.inputs["error_entry_time"].set ("You entered a character input")
            self.label_error_entry_time.grid (row = 1, column = 2)

            
    def update_clock (self):
        if self._job:
            self.parent.after_cancel (self._job)
        
        _timeout = self.timeout.update ()
        if _timeout:
            self.label_clock.configure (text = self.strftime (_timeout))
            self._job = root.after (100, self.update_clock)
        else:
            self.label_clock.configure (text = "Timeout...")
            self.show_timeout_popup ()

            
    def strftime (self, timeout_datetime):
        # thanks to http://stackoverflow.com/questions/538666/python-format-timedelta-to-string
        hour, remainder = divmod (timeout_datetime.seconds, 3600)
        minutes, seconds = divmod (remainder, 60)
        return str (timeout_datetime.days) + ":" + \
            str (hour) + ":" + \
            str (minutes) + ":" + \
            str (seconds)

    
    def show_timeout_popup(self):
        popup_root = tk.Toplevel ()
        popup_root.title ("Step finished")
        popup_root.resizable (False, False)

        popup_label = tk.Label (popup_root, text = "Time has expired...\nEnjoy your pause!", \
                                font = "Verdana 24")                            

        popup_button = tk.Button (popup_root, text = "Done!", \
                                  command = popup_root.destroy)
        
        popup_label.grid (row = 0, column = 0, sticky = tk.N + tk.S + tk.E + tk.W)
        popup_button.grid (row = 1, column = 0, sticky = tk.N + tk.S + tk.E + tk.W)
        popup_root.mainloop ()
        
        
root = tk.Tk()
root.wm_title ("Pomodoro clock")
root.minsize (450, 180)
app = TimeoutUI (root)
root.mainloop ()
