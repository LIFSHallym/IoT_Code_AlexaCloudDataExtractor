import datetime
from datetime import timezone
import dateutil.tz
import iso8601
import json


class Utils:
    def __init__(self):
        return
    
    @staticmethod
    def save_to_file(path, data):
        """Save data to a file

        Args:
            path (str): The output path including its extension
            data (bytes): The data to be saved
        """
        try:
            # with open(path + '.json',"wb") as json_file:
            #     json_file.write(data)
            with open(path + '.json', 'w') as outfile:  
                json.dump(data, outfile)
        except:
            pass
    
    @staticmethod
    def to_human_timestamp(timestamp):
        """Convert a unix millisecond to string
        Args:
            timestamp (int): Unix millisecond time

        Returns:
            The converted date (str)
        """
        if timestamp:
            new_timestamp = datetime.datetime.utcfromtimestamp(float(timestamp) / 1000)
            return new_timestamp.strftime("%Y-%m-%d %H-%M-%S.%f")[:-3]
        else:
            return ""

    @staticmethod
    def showMessage(type, message):          
        #import tkinter as tk
        from tkinter import messagebox
        #root = tk.Tk()
        if type == 'error':
            messagebox.showerror(type, message)
        else:
            messagebox.showinfo(type, message)
        #exit()


