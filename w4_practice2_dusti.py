"""
Teachers in most school districts are paid on a schedule that provides a salary based on their number of years of
teaching experience.

For example, a beginning teacher in the Lexington School District might be paid $30,000 the first year.
For each year of experience after this first year, up to 10 years, the teacher receives a 2% increase over
the preceding value.

Write a program that displays a salary schedule, in tabular format, for teachers in a school district. The inputs are:

Starting salary
Annual percentage increase
Number of years for which to print the schedule
Each row in the schedule should contain the year number and the salary for that year

An example of the program input and output is shown below:

Enter the starting salary: $30000
Enter the annual % increase: 2
Enter the number of years: 10

Year   Salary
-------------
 1    30000.00
 2    30600.00
 3    31212.00
 4    31836.24
 5    32472.96
 6    33122.42
 7    33784.87
 8    34460.57
 9    35149.78
10    35852.78
"""


# TABULATE ===============================================================================================

# from tabulate import tabulate
#
# # get inputs
# starting_salary = int(input("Enter the starting salary: "))
# percent_increase = int(input("Enter the annual % increase: "))
# number_of_years = int(input("Enter the number of years: "))
#
# # convert percent to use in incrementing salary
# percent_increase = 1 + (percent_increase / 100)
#
# # create list to hold data
# data = []
#
# # add data to list
# salary = float(starting_salary)
# for year in range(1, number_of_years + 1):
#     inner_data = [year, f"{salary:.2f}"]  # row in table
#     data.append(inner_data)  # add row to list
#     salary *= percent_increase  # increment salary
#
# print(tabulate(data, headers=["Year", "Salary"]))


# NO TABULATE ================================================================================

# function for formatting output
def tabular_format(col1, col2):
    if type(col2) != str:
        _col2 = f"{col2:.2f}"
    else:
        _col2 = col2
    formatted_string = f"{col1:>4}    {_col2:<8}"
    return formatted_string


# get inputs
starting_salary = int(input("Enter the starting salary: "))
percent_increase = int(input("Enter the annual % increase: "))
number_of_years = int(input("Enter the number of years: "))

# # convert percent to use in incrementing salary
percent_increase = 1 + (percent_increase / 100)

# print table header
header = tabular_format("Year", "Salary")
print(header)
print("-" * len(header))

# print table data
salary = starting_salary
for year in range(1, number_of_years + 1):
    print(tabular_format(year, salary))
    salary *= percent_increase
