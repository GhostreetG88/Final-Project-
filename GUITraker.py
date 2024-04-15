"""
Program: GUITraker.py
Author: Adrian Valdez
Date: 4/15/24

The purpose of this GUI is to keep track of your habits, in which the user can integrate the 
habits he/she would like and each time he/she logs in, record his/her progress.
"""

import tkinter as tk
from tkinter import messagebox
import datetime


class HabitEntry(tk.Frame):
    def create_widgets(self):
        # Create a frame to hold the habit name entry and checkboxes
        habit_frame = tk.Frame(self)
        habit_frame.pack(pady=10)

        # Create a label and entry for the habit name
        habit_label = tk.Label(habit_frame, text="Habit Name:")
        habit_label.grid(row=0, column=0)
        self.habit_entry = tk.Entry(habit_frame)
        self.habit_entry.grid(row=0, column=1)

        # Create a frame to hold the checkboxes for each day of the week
        days_frame = tk.Frame(habit_frame)
        days_frame.grid(row=1, column=0, columnspan=2)

        # Create a variable for each checkbox
        self.days = []
        for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
            var = tk.BooleanVar()
            cb = tk.Checkbutton(days_frame, text=day, variable=var)
            cb.grid(row=0, column=self.days.index(var) if self.days else 0, sticky="w")
            self.days.append(var)

        # Create a button to add the habit
        add_button = tk.Button(self, text="Add Habit", command=self.add_habit)
        add_button.pack(pady=10)

    def add_habit(self):
        # Get the habit name and days of the week from the widgets
        habit_name = self.habit_entry.get()
        days = [day.get() for day in self.days]

        # Add the habit to the list of habits
        self.habits.append((habit_name, days))

#continue 






class WeeklyReport(tk.Frame):
    def __init__(self, master, habits, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.habits = habits
        self.create_widgets()

    def create_widgets(self):
        # Create a label for the report title
        title_label = tk.Label(self, text="Weekly Report", font=("Arial", 16, "bold"))
        title_label.pack(pady=10)

# I neeed more time like 3328409283409238e years and maybe I can done whit this code, I dont wanna code more 
# I think is a good start 