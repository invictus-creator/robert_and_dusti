from tabulate import tabulate

base = int(input("Enter the starting salary: $"))
inc = int(input("Enter the annual % increase: "))
years = int(input("Enter the number of years: "))

d = [["Year", 12, 95],["Salary", 11, 88]]

print(tabulate(d, headers=["Year", "Salary"]))


