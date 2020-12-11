# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 10:38:32 2020

@author: TRAINING
"""
import pandas as pd


pd.set_option("display.max_columns",None)

# File to view match schedule
df=pd.read_csv("schedule.csv")

# Input file to see user booking details
bd=pd.read_csv("booking_details.csv")


class seat:
    tot_seat_available = 0
    tot_seats_booked = 0
    def seats_available(self, tot_capacity):
        self.tot_seat_available = tot_capacity - self.tot_seats_booked
        return self.tot_seat_available

class user(seat):
    name=""
    bookings=0
    tot_cost=0
    match_booked=0
    def book_ticket(self,cost,tot_capacity):
        self.bookings=int(input("Tickets to Book:"))
        if self.bookings <= self.seats_available(tot_capacity):
            tot_cost=cost*self.bookings
            print(f"Total cost for {self.bookings} tickets :{tot_cost}")
            self.tot_seats_booked += self.bookings
            self.tot_seat_available = tot_capacity - self.tot_seats_booked

u1=user()

class stadium:
    tot_capacity = 0
    cost = 1000

    def details(self,tot_capacity):
        self.tot_capacity=tot_capacity

    def match_schedule(self):
        print("\nSchedule is")
        print(f"1){df.AWAY[0]} X {df.HOME[0]} {df.FORMAT[0]} on {df.DATE[0]}")
        print(f"2){df.AWAY[1]} X {df.HOME[1]} {df.FORMAT[1]} on {df.DATE[1]}")
        print(f"3){df.AWAY[2]} X {df.HOME[2]} {df.FORMAT[2]} on {df.DATE[2]}")
        u1.match_booked=int(input("Match to be booked:"))
        print("Seat Available:", u1.seats_available(self.tot_capacity))
        u1.name=(input("Enter Username"))
        u1.book_ticket(self.cost,self.tot_capacity)
        print("Seat Available:",u1.seats_available(self.tot_capacity))

mumbai=stadium()
kolkata=stadium()
chennai=stadium()
shriram=user()

def match():
    print("\n\nWhich stadium to book tickets")
    print("1)Mumbai")
    print("2)Kolkata")
    print("3)Chennai")
    selected_stadium=int(input("Choose Stadium:"))
    if selected_stadium == 1:
        mumbai.details(50000)
        mumbai.match_schedule()
        match()
    elif selected_stadium == 2:
        kolkata.details(60000)
        kolkata.match_schedule()
        match()
    elif selected_stadium == 3:
        chennai.details(70000)
        chennai.match_schedule()
        match()
    else:
        return 0

match()
