# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 00:43:54 2018

@author: Albert
"""

########################
# PART B - Saving, with a raise
""" 
This program calculates how long it will take to save enough money for 
a down payment on a house. IT factors in a raise every 6 months.
"""
########################

# Get user input
annual_salary= int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = int(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

portion_down_payment = 0.25
current_savings = 0
rate_of_return = 0.04

# Precalculate some variables for better program readability
monthly_rate_of_return = rate_of_return / 12
down_payment_cost = total_cost * portion_down_payment
number_of_months = 0

# Calculate how many months it will take to save up for a down payment
# given the current amount saved and the yearly rate of return.
# A pay raise is factored into this calculation.
while current_savings < down_payment_cost:
    if number_of_months > 0 and number_of_months % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise
    monthly_salary = annual_salary / 12
    monthly_savings = portion_saved * monthly_salary
    current_savings += current_savings * monthly_rate_of_return
    current_savings += monthly_savings
    number_of_months += 1
    
    
print("Number of months: %d" % number_of_months)