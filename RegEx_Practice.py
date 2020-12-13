# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 11:36:39 2020

@author: Shriram M.S
"""
import re

# To find a valid phone number
number=str(input("Phone Number: "))
if re.match("91-\d{10}$",number):
    print("Valid Entry")
else:
    print("Invalid Entry")

# To find a valid mail id
email=str(input("Email: "))
if re.match("[a-zA-Z0-9.+-_]+@[a-z]+\.[a-z]{2,3}",email):
    print("Valid Entry")
else:
    print("Invalid Entry")

# To validate credit card number
credit_card=str(input("Credit Card Number: "))
if re.match("\d{4}[-, ]?\d{4}[-, ]?\d{4}[-, ]\d{4}",credit_card):
    print("Valid Entry")
else:
    print("Invalid Entry")

# To validate credit card number
ip_address=str(input("IP Address: "))
if re.match("(\d{1,3}\.){3}\d{1,3}",ip_address):
    print("Valid Entry")
else:
    print("Invalid Entry")