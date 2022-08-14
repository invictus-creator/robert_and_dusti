from tabulate import tabulate

base = float(input("Enter the starting salary: $"))
inc = int(input("Enter the annual % increase: "))
years = int(input("Enter the number of years: "))

print("Year   Salary\n-------------")
multiplier = 1 + inc / 100
salary = base
for years in range(1, years + 1):
    print("%2d%12.2f" % (years, salary))
    salary *= multiplier






