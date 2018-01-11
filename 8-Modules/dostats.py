#Playing with Statistics Module! Challenge 1

#import statistics module
import statistics

#define list of iterables
numbers = [5, 10, 79, 84, 99]

#variable result with return from mean function
meanresult = str(statistics.mean(numbers))

print("Our numbers are: " + str(numbers))

print("Mean: " + meanresult)

try:
	moderesult = statistics.mode(numbers)
	print("Mode: " + moderesult)
except statistics.StatisticsError:
	print("Mode: No Mode - All Values Unique")

pstdev = str(statistics.pstdev(numbers))

print("Standard Deviation: " + pstdev)

pvariance = str(statistics.pvariance(numbers))

print("Variance: " + pvariance)

