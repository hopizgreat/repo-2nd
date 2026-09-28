# -*- coding: utf-8 -*-
"""
Created on Sun Nov  9 20:07:45 2025

@author:  Thomas Abera
@Title:   Project 3
@#Source: From Project 2 pseudocode
@AI:      No AI was used for this python program

"""
print("Project 3 by Thomas Abera")

def Main():
    global more
    InitInitials()
    ClientInput()
    more = input("Enter 'Y' to start, or 'N' to end: ")
    
    while more == "Y":
        LeapYear()
        more = input("Enter 'Y' to continue, or 'N' to end: ")
        
    CalcPercent()
    OutputSummary()
    
def InitInitials():
    global count, count_ly, most_recent_ly
    count = count_ly = most_recent_ly = 0
    
def ClientInput():
     global client_nr
     client_nr = input("Enter Client Number: ")
     
def LeapYear():
    LeapYearProcess()
    WSupdate()
    
def LeapYearProcess():
    global mdy_date, year, leap_year
    mdy_date = input("Enter the date to be calculated: ")
    year = int(mdy_date[-4:])
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        leap_year = "TRUE"
    else:
        leap_year = "FALSE"

def WSupdate():
    global count, leap_year, count_ly, most_recent_ly
    count += 1
    if leap_year == "TRUE":
        count_ly += 1
        if year > most_recent_ly:
            most_recent_ly = year
    print ("The extracted year is", year)
    print ("Leap year or not?", leap_year)

def CalcPercent():
    global percent_ly, count_not_ly
    percent_ly = (count_ly / count)*100
    count_not_ly = count - count_ly       
    
def OutputSummary():
    print("Client Number is:", client_nr)
    print("The total number of the years that are leap years are:", count_ly)
    print("The total number of years that are not leap years are:", count_not_ly)
    print("The most recent leap year is: ", most_recent_ly)
    print(percent_ly, "% is the percentage of the leap years.")
count = count_ly = count_not_ly = 0

Main()
    
     
    
    
        
        