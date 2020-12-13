# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 19:16:42 2020

@author: Shriram M.S
"""
import pandas as pd
from datetime import datetime

pd.set_option("display.max_columns", None)

# File to view match schedule's
mf = pd.read_csv("mumbai_schedule.csv")
kf = pd.read_csv("kolkata_schedule.csv")
cf = pd.read_csv("chennai_schedule.csv")


# Class to update seat availability for all the matches
class seat:
    # Function to initialize attributes
    def __init__(self):
        self.tot_seats_available_1 = 0
        self.tot_seats_booked_1 = 0
        self.tot_seats_available_2 = 0
        self.tot_seats_booked_2 = 0
        self.tot_seats_available_3 = 0
        self.tot_seats_booked_3 = 0

    # Function to update seat availability
    def seats_available(self, tot_capacity, match_booked):
        if match_booked == 1:
            self.tot_seats_available_1 = tot_capacity - self.tot_seats_booked_1
            return self.tot_seats_available_1
        elif match_booked == 2:
            self.tot_seats_available_2 = tot_capacity - self.tot_seats_booked_2
            return self.tot_seats_available_2
        elif match_booked == 3:
            self.tot_seats_available_3 = tot_capacity - self.tot_seats_booked_3
            return self.tot_seats_available_3

    # Function to display stadium seat availability details
    def display_stadium_detail(self, tot_capacity):
        print(f"\nTotal Capacity:{tot_capacity}")
        if self.match_booked == 1:
            print(f"Total Seats Booked:{self.tot_seats_booked_1}")
            print(f"Total Seats Available: {self.seats_available(tot_capacity, self.match_booked)}")
        elif self.match_booked == 2:
            print(f"Total Seats Booked:{self.tot_seats_booked_2}")
            print(f"Total Seats Available: {self.seats_available(tot_capacity, self.match_booked)}")
        elif self.match_booked == 3:
            print(f"Total Seats Booked:{self.tot_seats_booked_3}")
            print(f"Total Seats Available: {self.seats_available(tot_capacity, self.match_booked)}")


# Class to update the audience member's name
class name:
    # Function to initialize attributes
    def __init__(self):
        self.username = ""

    def name_entry(self, username):
        self.username = username


# Class to save details about an audience member's ticket bookings
class user(seat, name):
    # Function to initialize attributes
    def __init__(self, stadium_name):
        self.stadium_name = stadium_name
        self.bookings = 0
        self.tot_cost = 0
        self.match_booked = 0
        self.date = 0
        self.time = 0
        super().__init__()

    # Function to display booking details
    def booking_details(self):
        print(f"\nUsername   : {self.username}")
        print(f"Stadium    : {self.stadium_name}")
        print(f"Match      : {self.match_booked}")
        print(f"Tickets    : {self.bookings}")
        print(f"Total Cost : {self.tot_cost}")
        print(f"Booked on  : {self.date} {self.time}")
        if self.stadium_name == "Mumbai":
            temp_output = [[self.username, self.stadium_name,
                            str(f"{mf.AWAY[self.match_booked-1]} X
                                {mf.HOME[self.match_booked-1]}
                                {mf.FORMAT[self.match_booked-1]}"),
                            str(f"{mf.DATE[self.match_booked-1]}"),
                            self.bookings, self.tot_cost,
                            self.date, self.time]]
        if self.stadium_name == "Kolkata":
            temp_output = [[self.username, self.stadium_name,
                            str(f"{kf.AWAY[self.match_booked-1]} X
                                {kf.HOME[self.match_booked-1]}
                                {kf.FORMAT[self.match_booked-1]}"),
                            str(f"{kf.DATE[self.match_booked-1]}"),
                            self.bookings, self.tot_cost,
                            self.date, self.time]]
        if self.stadium_name == "Chennai":
            temp_output = [[self.username, self.stadium_name,
                            str(f"{cf.AWAY[self.match_booked-1]} X
                                {cf.HOME[self.match_booked-1]}
                                {cf.FORMAT[self.match_booked-1]}"),
                            str(f"{cf.DATE[self.match_booked-1]}"),
                            self.bookings, self.tot_cost,
                            self.date, self.time]]
        output = pd.DataFrame(temp_output)
        # Output file that shows booking confirmation details
        output.to_csv("booking_details.csv",
                      index=False, mode="a", header=False)

    # Function to book tickets
    def book_ticket(self, cost, tot_capacity):
        self.bookings = int(input(f"Tickets(Rs{cost}) to Book:"))
        self.date = datetime.now().date()
        self.time = datetime.now().time()
        print(f"Booked on {self.date} at {self.time}")
        if self.match_booked == 1:
            if self.bookings <= self.seats_available(tot_capacity,
                                                     self.match_booked):
                self.tot_cost = cost*self.bookings
                self.booking_details()
                self.tot_seats_booked_1 += self.bookings
                self.tot_seats_available_1 =
                tot_capacity - self.tot_seats_booked_1
        elif self.match_booked == 2:
            if self.bookings <= self.seats_available(tot_capacity,
                                                     self.match_booked):
                self.tot_cost = cost*self.bookings
                self.booking_details()
                self.tot_seats_booked_2 += self.bookings
                self.tot_seats_available_2 =
                tot_capacity - self.tot_seats_booked_2
        elif self.match_booked == 3:
            if self.bookings <= self.seats_available(tot_capacity,
                                                     self.match_booked):
                self.tot_cost = cost*self.bookings
                self.booking_details()
                self.tot_seats_booked_3 += self.bookings
                self.tot_seats_available_3 =
                tot_capacity - self.tot_seats_booked_3

# Objects of user pertaining to particular stadiums
u1 = user("Mumbai")
u2 = user("Kolkata")
u3 = user("Chennai")


# Class to update cost of each stadiums
class cost:
    # Function to initialize attributes
    def __init__(self):
        self.cost = 0

    def cost_detail(self, cost):
        self.cost = cost


# Class to save details about stadiums
class stadium(cost):
    # Function to initialize attributes
    def __init__(self):
        self.tot_capacity = 0
        super().__init__()

    # Function to update stadium capacity and ticket cost
    def capacity_detail(self, tot_capacity, cost):
        self.tot_capacity = tot_capacity
        self.cost_detail(cost)

    # Function to see schedule of matches
    def match_schedule(self, u):
        if u.stadium_name == "Mumbai":
            print("\nSchedule is")
            print(f"1.{mf.AWAY[0]} X {mf.HOME[0]}
                  {mf.FORMAT[0]} on {mf.DATE[0]}")
            print(f"2.{mf.AWAY[1]} X {mf.HOME[1]}
                  {mf.FORMAT[1]} on {mf.DATE[1]}")
            print(f"3.{mf.AWAY[2]} X {mf.HOME[2]}
                  {mf.FORMAT[2]} on {mf.DATE[2]}")
            u1.match_booked = int(input("Match to be booked:"))
            u1.display_stadium_detail(self.tot_capacity)
            u1.name_entry(input("Enter Username"))
            u1.book_ticket(self.cost, self.tot_capacity)
            u1.display_stadium_detail(self.tot_capacity)
        if u.stadium_name == "Kolkata":
            print("\nSchedule is")
            print(f"1.{kf.AWAY[0]} X {kf.HOME[0]}
                  {kf.FORMAT[0]} on {kf.DATE[0]}")
            print(f"2.{kf.AWAY[1]} X {kf.HOME[1]}
                  {kf.FORMAT[1]} on {kf.DATE[1]}")
            print(f"3.{kf.AWAY[2]} X {kf.HOME[2]}
                  {kf.FORMAT[2]} on {kf.DATE[2]}")
            u2.match_booked = int(input("Match to be booked:"))
            u2.display_stadium_detail(self.tot_capacity)
            u2.name_entry(input("Enter Username"))
            u2.book_ticket(self.cost, self.tot_capacity)
            u2.display_stadium_detail(self.tot_capacity)
        if u.stadium_name == "Chennai":
            print("\nSchedule is")
            print(f"1.{cf.AWAY[0]} X {cf.HOME[0]}
                  {cf.FORMAT[0]} on {cf.DATE[0]}")
            print(f"2.{cf.AWAY[1]} X {cf.HOME[1]}
                  {cf.FORMAT[1]} on {cf.DATE[1]}")
            print(f"3.{cf.AWAY[2]} X {cf.HOME[2]}
                  {cf.FORMAT[2]} on {cf.DATE[2]}")
            u3.match_booked = int(input("Match to be booked:"))
            u3.display_stadium_detail(self.tot_capacity)
            u3.name_entry(input("Enter Username"))
            u3.book_ticket(self.cost, self.tot_capacity)
            u3.display_stadium_detail(self.tot_capacity)

# Objects of stadium created for user access
mumbai = stadium()
kolkata = stadium()
chennai = stadium()


# Function acting as a menu to show stadiums available for booking
def match():
    print("\n\nWhich stadium to book tickets")
    print("1)Mumbai")
    print("2)Kolkata")
    print("3)Chennai")
    selected_stadium = int(input("Choose Stadium:"))
    if selected_stadium == 1:
        mumbai.capacity_detail(50000, 1200)
        mumbai.match_schedule(u1)
        match()
    elif selected_stadium == 2:
        kolkata.capacity_detail(60000, 1100)
        kolkata.match_schedule(u2)
        match()
    elif selected_stadium == 3:
        chennai.capacity_detail(70000, 1000)
        chennai.match_schedule(u3)
        match()
    else:
        return 0

match()
