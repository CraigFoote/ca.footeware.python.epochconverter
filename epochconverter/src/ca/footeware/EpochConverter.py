#!/usr/local/bin/python

'''
Created on Sep 2, 2017

@author: footeware.ca
'''

import datetime as dt
import tkinter as tk
from tkinter import messagebox

class EpochConverter(object):
    """Converts to and from ISO8601 formatted date and milliseconds since epoch."""

    def __init__(self):
        """Creates the GUI"""

        self.root = tk.Tk()
        self.root.title("Epoch Converter")
        self.root.resizable(0, 0)

        self.label_epoch = tk.Label(self.root, text="millis since Epoch")
        self.label_epoch.grid(row=0, column=0, padx=5, pady=5)
        self.label_iso8601 = tk.Label(self.root, text="ISO8601")
        self.label_iso8601.grid(row=1, column=0, padx=5, pady=5)

        self.millis = tk.StringVar()
        self.millis_text = tk.Entry(self.root, width=25, textvariable=self.millis)
        self.millis_text.grid(row=0, column=1, padx=5, pady=5)
        self.millis_text.config(font=("Courier", 16))

        self.iso8601 = tk.StringVar()
        self.iso8601_text = tk.Entry(self.root, width=25, textvariable=self.iso8601)
        self.iso8601_text.grid(row=1, column=1, padx=5, pady=5)
        self.iso8601_text.config(font=("Courier", 16))

        self.epoch_button = tk.Button(self.root, text='Convert to ISO8601')
        self.epoch_button.grid(row=0, column=2, padx=5, pady=5)
        self.epoch_button.bind("<Button-1>", self.convert_to_iso8601)

        self.iso8601_button = tk.Button(self.root, text='Convert to Epoch millis')
        self.iso8601_button.grid(row=1, column=2, padx=5, pady=5)
        self.iso8601_button.bind("<Button-1>", self.convert_to_epoch)


    def convert_to_iso8601(self, event=None):
        """Converts to ISO8601 datetime"""

        try:
            self.iso8601.set(dt.datetime.utcfromtimestamp(float(self.millis.get())).isoformat())
        except ValueError as value_error:
            messagebox.showerror("Error", value_error)


    def convert_to_epoch(self, event=None):
        """Converts to millis since epoch"""

        try:
            utc_time = dt.datetime.strptime(self.iso8601.get(), "%Y-%m-%dT%H:%M:%S")
            epoch_time = (utc_time - dt.datetime(1970, 1, 1)).total_seconds()
            self.millis.set(int(epoch_time))
        except ValueError as value_error:
            messagebox.showerror("Error", value_error)


if __name__ == "__main__":
    EPOCH_CONVERTER = EpochConverter()
    EPOCH_CONVERTER.root.mainloop()
