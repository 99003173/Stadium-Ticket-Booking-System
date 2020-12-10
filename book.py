def match:
    print("Which stadium to book tickets")
    print("1)Mumbai")
    print("2)Kolkata")
    print("3)Chennai")
    stadium=input("Choose stadium")
    

    
class stadium:
    
    total_capacity
    total_seat_available
    total_seats_booked
    cost=1000
    total_cost
    
    def seats_available():
        total_seat_available=total_capacity-total_seats_booked
        return total_seat_available
    
    def book_ticket():
        bookings=input("Total no. of tickets to book")
        if seats_available() < bookings:
            print("Enough tickets not available")
            match_schedule()
        else:
            total_cost=cost*bookings
            total_seats_booked+=bookings
            total_seat_available=total_capacity-total_seats_booked
        
    def match_schedule():
        print("Schedule is")
        print("1) IND V/s AUS 1st ODI on ")
        print("2) IND V/s AUS 2nd T20")
        print("3) IND V/s AUS 3rd T20")
        match_booked=int(input("Enter match to book for:"))
        print("Seat Available:",seats_available())
        book_ticket()
    


def login:
    uname=input("Enter username")
    pword=input("Enter password")
    match()
