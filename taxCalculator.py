"""
Program: taxCalculator.py
Author: Robert Timberlake
Compute a user's estimated income tax.
1. Significant constants
    federal tax percent
    fica tax percent
2. The inputs are
    name
    gross income
    state tax percent
3. Computations:
    federal tax = gross income * 9.45%
    fica tax = gross income * 7.65%
    state tax = gross income * state tax percent
    estimated tax = federal tax + fica tax + state tax
4. The outputs are
    name
    gross income
    estimated tax
"""

# Initialize the constants
FED_TAX_RATE = .0945
FICA_TAX_RATE =  .0765

# Request the inputs
name = input("Please enter your name: ")
grossIncome = float(input("Please enter your gross income: "))
stateTaxRate = float(input("Please enter your state tax rate: "))

# Compute the taxes
fedTax = grossIncome * FED_TAX_RATE
ficaTax = grossIncome * FICA_TAX_RATE
stateTax = grossIncome * FED_TAX_RATE
estimatedTax = fedTax + ficaTax + stateTax

# Display the estimated tax
print(name + "'s estimated tax is $" + round(estimatedTax,2), "based on a gross income of $" + grossIncome)
