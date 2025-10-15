# day5.py
# Basic array example using the statistics library, It will get the mean, median, and variance of 5 numbers entered by the user

import statistics

numbers = []

print("Enter 5 numbers:")

for i in range(5):
    while True:
        try:
            num = float(input(f"Number {i+1}: "))
            numbers.append(num)
            break
        except ValueError:
            print("Please enter a valid number.")

print("\nThe numbers you entered are:", numbers)

# Use statistics library functions
mean = statistics.mean(numbers)
median = statistics.median(numbers)
variance = statistics.variance(numbers)

print(f"\nMean: {mean}")
print(f"Median: {median}")
print(f"Variance: {variance}")
