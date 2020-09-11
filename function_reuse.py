# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 18:54:40 2020

@author: J
"""

# REPLACE THIS STARTER CODE WITH YOUR FUNCTION
month_days = 30
print("June has " + str(month_days) + " days.")
month_days = 31
print("July has " + str(month_days) + " days.")

#function to pass month and dates represting code reuse
def month_days(month, days):
    print(month, "has " + str(days) + " " + " days.")

month_days("July", 31)


# 1) Complete the function to return the result of the conversion
def convert_distance(miles):
	return miles * 1.6  # approximately 1.6 km in 1 mile

my_trip_miles = 55

convert_distance(my_trip_miles)
print(convert_distance(my_trip_miles))

# 2) Convert my_trip_miles to kilometers by calling the function above
my_trip_km = convert_distance(my_trip_miles)

# 3) Fill in the blank to print the result of the conversion
print("The distance in kilometers is " + str(my_trip_km))
round_trip = my_trip_km * 2
# 4) Calculate the round-trip in kilometers by doubling the result,
#    and fill in the blank to print the result
print("The round-trip in kilometers is " + str(round_trip))

#branching if statements
def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long")
    else: 
        print("Good username.")
hint_username("REDDY")

#adding elif

def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long")
    elif len(username) > 15:
        print("Invalid username. Must be at most 15 characters long")
    else:
        print("Vaild username")
hint_username("NEODMSEOGSLCIDDKE")

#check if number positive or negative
def number_group(number):
  if number > 0:
    return "Positive"
  elif number < 0:
    return "Negative"
  else:
    return "Zero"
print(number_group(10)) #Should be Positive
print(number_group(0)) #Should be Zero
print(number_group(-5)) 

print("big">"small")
print (11 % 5)

def sum(x,y):
    return(x+y)
print(sum(sum(1,2),sum(3,4)))

def sum(x, y):
		return(x+y)
print(sum(sum(1,2), sum(3,4)))