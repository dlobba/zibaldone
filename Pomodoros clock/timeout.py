import tkinter as tk
import datetime
import logging

class Timeout:
    """Class Timeout that take account of a small amuount of time that
    notify when it's elapsed."""

    def __init__ (self, timeout = 0):
        """The constructor can be initialized directly with a timeout expressed in seconds."""
        self.precision = 100000 # set precision to 100000 microseconds
        self.timeout = timeout
        self.timeout_datetime # will keep the datetime of the timeout once set

        
    def set_new_timeout (self, \
                         days = 0, \
                         hours = 0, \
                         minutes = 0, \
                         seconds = 0):
        """Set a new timeout, can be set with different precision
    (days, hours, minutes, seconds)."""

        self.timeout = days * 86400 + \
                       hours * 3600 + \
                       minutes * 60 + \
                       seconds
        

    def update (self):
        if self.timeout:
            delta = self.timeout_datetime - datetime.datetime.now ()
            
            if delta.days <= 0 \
               and delta.seconds <= 0 \
               and delta.microseconds <= self.precision:
                self.timeout = 0
                # logging.debug ("Time out...")
                print ("Time out...")
                return False
                
            else:
                # logging.debug ("Time elapsed " + str (delta))
                print ("Time elapsed " + str (delta))
                return delta
            
    def activate_timeout (self):
        self.timeout_datetime = datetime.datetime.now () + \
                                datetime.timedelta (seconds = self.timeout)
