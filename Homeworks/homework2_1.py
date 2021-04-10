"""
Ask the user to input a single digit integer to variable 'n'.
Then,print out all of the even numbers from 0 to n(including n)
"""

userInput=int(input("Please enter a digit number(0-9):"))

if(userInput>=10):
    print("Oops...The number is not a digit number")
else:
    for i in range(userInput+1):
        if(i%2==0):
            print(i)
        else:
            continue
