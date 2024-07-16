import tkinter as tk
from tkinter import ttk
import calendar

class CalendarApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Calendar")

        self.year_var = tk.IntVar(value=2024)
        self.month_var = tk.IntVar(value=7)

        self.create_widgets()
        self.show_calendar()

    def create_widgets(self):
        frame = ttk.Frame(self.root)
        frame.pack(pady=10)

        ttk.Label(frame, text="Year:").grid(row=0, column=0)
        self.year_entry = ttk.Entry(frame, textvariable=self.year_var, width=5)
        self.year_entry.grid(row=0, column=1, padx=5)

        ttk.Label(frame, text="Month:").grid(row=0, column=2)
        self.month_entry = ttk.Entry(frame, textvariable=self.month_var, width=5)
        self.month_entry.grid(row=0, column=3, padx=5)

        show_button = ttk.Button(frame, text="Show Calendar", command=self.show_calendar)
        show_button.grid(row=0, column=4, padx=5)

        self.calendar_text = tk.Text(self.root, width=20, height=10, wrap='none')
        self.calendar_text.pack(pady=10)

    def show_calendar(self):
        year = self.year_var.get()
        month = self.month_var.get()
        cal = calendar.month(year, month)
        self.calendar_text.delete(1.0, tk.END)
        self.calendar_text.insert(tk.END, cal)

if' _name_ '== "_main_":
    root = tk.Tk()
    app = CalendarApp(root)
    root.mainloop()