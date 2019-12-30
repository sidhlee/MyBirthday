#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk
import datetime


class App(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        master.grid()
        self.master.title(u'내 생일')
        self.days = tk.StringVar()
        self.days.set('?')
        self.create_widgets()

    def create_widgets(self):

        bday = Birthday()
        ethan = ttk.Button(self.master, text=u"이이든",
                           command=lambda: self.days.set(bday.days_to_bday(bday.ethan))
                           )
        erae = ttk.Button(self.master, text=u"이이래",
                          command=lambda: self.days.set(bday.days_to_bday(bday.erae)))
        mom = ttk.Button(self.master, text=u"엄마",
                         command=lambda: self.days.set(bday.days_to_bday(bday.mom)))
        dad = ttk.Button(self.master, text=u"아빠",
                         command=lambda: self.days.set(bday.days_to_bday(bday.dad)))
        pannel = tk.Frame(self.master,
                          height=150,
                          relief=tk.RIDGE,
                          borderwidth=10)
        days_remain = tk.Label(pannel,
                               textvariable=self.days,
                               font=('', 70, 'bold'))
        ethan.grid(row=0, column=0)
        erae.grid(row=0, column=1)
        mom.grid(row=1, column=0)
        dad.grid(row=1, column=1)
        pannel.grid(row=2, column=0, columnspan=2,
                    sticky=tk.W+tk.E+tk.N+tk.W)
        days_remain.pack(expand=1)


class Birthday:
    def __init__(self):
        self.today = datetime.date.today()
        self.ethan = datetime.date(2013, 11, 2)
        self.erae = datetime.date(2017, 10, 31)
        self.mom = datetime.date(1980, 7, 16)
        self.dad = datetime.date(1980, 6, 11)

    def get_age(self, birthday):
        age = (self.today - birthday).days
        return age // 365

    def get_k_age(self, birthday):
        age = self.today.year - birthday.year + 1
        return age

    def days_to_bday(self, birthday):
        my_birthday = birthday.replace(year=self.today.year)
        if my_birthday < self.today:
            my_birthday = my_birthday.replace(year=self.today.year + 1)

        time_to_bday = abs(my_birthday - self.today)
        return time_to_bday.days


root = tk.Tk()
App(root)
tk.mainloop()

