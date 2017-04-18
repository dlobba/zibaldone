import tkinter as tk
import datetime

timeout = None

def set_new_timeout (n_minutes):
        global timeout
        timeout = datetime.datetime.now () + datetime.timedelta (minutes = n_minutes)

def update ():
    global timeout
    if timeout:
        delta = timeout - datetime.datetime.now ()
        
        if delta.days <= 0 and delta.seconds <= 0 and delta.microseconds <= 100000:
            timeout = None
            print ("Timeout elapsed...")
            return 0
            
        else:
            print (str (delta))
            return 1

def flow ():
    DUMMY = True
    while DUMMY:
        DUMMY = update ()
