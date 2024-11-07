# Kaden Billin
# UWYO COSC 1010
# 11-7-2024
# Lab 08
# Lab Section: 12
# Sources, people worked with, help given to:
# your
# comments
# here


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 

thing = input("Enter a string here: ")

def check():
    if (thing).lstrip("-").isdigit() == True:
        print("True (int)")
        print(int(thing))
    elif "." in thing:
        stuff = thing.split(".")
        if stuff[0].lstrip("-").isdigit() == True and stuff[1].isdigit() == True and thing.count(".") == 1:
            print("True (float)")
            print(float(thing))
        else:
            print("False")
    else:
            print("False")

check()

print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

def slope_intercept(m, b, xlower, xupper):
     for all num in range(float(xlower),float(xupper)):
        print(i)
    return m
# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null
