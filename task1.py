#! python3

# Have the user input a number. 
# Determine if the number is larger than 100 
# If it is, the output should read "The number is larger than 100" 
# (2 points)
# Inputs:
# number

# Outputs:
# "The number is larger than 100"
# "The number is smaller than 100"
# "The number is 100"
number=float(input("Input a number "))
if number>100:
    print("The number is larger than 100")
if number<100:
    print("The number is smaller than 100")
if number==100:
    print("The number is 100")
