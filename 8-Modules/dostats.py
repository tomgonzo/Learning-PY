#Playing with Statistics Module! Challenge 1
#Revised after Chapter 8 - added lists and exception handling

#import statistics module
import statistics

#Create an empty list
numbers = []
i = 5

#Ask user for 5 numbers.
while i > 0:
    try: #In case some smartass tries to give it non-numericals.
        digit = input("Enter a number, or type quit to exit: ")
        if digit == "quit": #Exit plan!
            break
        digit = float(digit) #The input needs to be convertible to a float
        numbers.append(digit)
        i -= 1 #decrease x by one
    except ValueError:
        print("This program only accepts numbers. Please enter a number: ")


if digit != "quit": #do this only if the user doesn't quit
    #First, print all the numbers in the list
    print("Our numbers are: " + str(numbers))

    #Print the Mean
    meanresult = str(statistics.mean(numbers))
    print("Mean: " + meanresult)

    #Print the Mode - with Exception Handling
    try:
        moderesult = str(statistics.mode(numbers))
        print("Mode: " + moderesult)
    except statistics.StatisticsError:
        print("Mode: No Mode - All Values Unique")

    #Print the Standard Deviation
    pstdev = str(statistics.pstdev(numbers))
    print("Standard Deviation: " + pstdev)

    #Print the Variance
    pvariance = str(statistics.pvariance(numbers))
    print("Variance: " + pvariance)
