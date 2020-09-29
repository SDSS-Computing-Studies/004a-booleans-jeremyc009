#! python3

# Have the user enter a number 
# Determine if the number is an integer
# 1 mark

# Inputs:
# a number

# Outputs:
# "the number is an integer"
# "the number is not an integer"
number=float(input("Enter a number "))
secondNumber=number%2
if secondNumber==abs(1) :
    print("the number is an integer")
elif secondNumber==abs(0):
    print("the number is an integer")
else:
    print("the number is not an integer") 
