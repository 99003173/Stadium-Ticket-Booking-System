# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd

pd.set_option("display.max_columns",None)
df=pd.read_csv("schedule.csv")
bd=pd.read_csv("booking_details.csv")
cd=open("confirmation_details.txt","w")

class stadium:

    tot_capacity=0
    tot_seat_available=0
    tot_seats_booked=0
    cost=1000
    tot_cost=0
    
    def details(self,tot_capacity):
        self.tot_capacity=tot_capacity
    
    def seats_available(self):
        tot_seat_available=self.tot_capacity-self.tot_seats_booked
        return tot_seat_available
    
    def book_ticket(self,match_booked):
        print("Total no. of tickets to book",bd.no_of_tickets[0])
        bookings=bd.no_of_tickets[0]
        if self.seats_available() < bookings:
            print("Enough tickets not available")
            self.match_schedule()
        else:
            self.tot_cost=self.cost*bookings
            self.tot_seats_booked+=bookings
            print(f"Total cost for {bookings} tickets are {self.tot_cost}")
            self.tot_seat_available=self.tot_capacity-self.tot_seats_booked
            cd.writelines(str(bd.audience_id[0]))
            cd.writelines(str(bookings))
            cd.writelines(str(self.tot_cost))
            cd.writelines(str("1001 plus "+str(bookings)))
        
    def match_schedule(self,tot_capacity):
        self.tot_capacity=tot_capacity
        print("Schedule is")
        print(f"1){df.AWAY[0]} X {df.HOME[0]} {df.FORMAT[0]} on {df.DATE[0]}")
        print(f"2){df.AWAY[1]} X {df.HOME[1]} {df.FORMAT[1]} on {df.DATE[1]}")
        print(f"3){df.AWAY[2]} X {df.HOME[2]} {df.FORMAT[2]} on {df.DATE[2]}")
        print("Match to be booked:",bd.match_number[0])
        match_booked=bd.match_number[0]
        print("Seat Available:",self.seats_available())
        self.book_ticket(match_booked)

mumbai=stadium()
kolkata=stadium()
chennai=stadium()

def match():
    print("Which stadium to book tickets")
    print("1)Mumbai")
    print("2)Kolkata")
    print("3)Chennai")
    print("Choose Stadium:",bd.city[0])
    selected_stadium=bd.city[0]
    if selected_stadium == 1:
        mumbai.match_schedule(50000)
    elif selected_stadium == 2:
        kolkata.match_schedule(60000)
    elif selected_stadium == 3:
        chennai.match_schedule(70000)

def login():
    log=pd.read_csv("login_details.csv")
    for id,pw in log.original_id,log.original_password:
        #if pw == bd.given_password[0] and id == bd.audience_id[0]:
            match()
        #else:
            #print("No ID found")


    
login()
