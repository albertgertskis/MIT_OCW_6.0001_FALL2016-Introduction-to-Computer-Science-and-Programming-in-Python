# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 00:54:58 2018

@author: Albert
"""

########################
# PART C - Finding the right amount to save away
""" 
This program calculates the best rate of savings to 
achieve a down payment on a house within a certain
time frame. 
"""
########################

# Get user input for starting salary
starting_salary= int(input("Enter the starting salary: "))

semi_annual_raise = 0.07
total_cost = 1_000_000
portion_down_payment = 0.25
current_savings = 0
rate_of_return = 0.04
total_months = 36

# Precalculate some variables for better program readability
monthly_rate_of_return = rate_of_return / 12
down_payment_cost = total_cost * portion_down_payment

# Bisection search step counter
number_of_steps = 0

# Allowable difference between down payment value and amount of down payment 
# paid in a time period of 36 months.
epsilon = 100

low = 0.0
high = 1.0

# Guess savings rate as a percentage
guess_savings_rate = (high + low) / 2

while abs(down_payment_cost - current_savings) > epsilon:
    # Calculate how much will be saved up for a down payment within 36 months
    # given the user's salary and other preset information (e.g. semi-annual raise percentage, etc.)
    current_salary = starting_salary
    current_savings = 0
    
    for month_count in range(36):
        if month_count > 0 and month_count % 6 ==0:
            current_salary += current_salary * semi_annual_raise
        monthly_salary = current_salary / 12
        monthly_savings = guess_savings_rate * monthly_salary
        current_savings += current_savings * monthly_rate_of_return
        current_savings += monthly_savings
        
    if current_savings < down_payment_cost:
        low = guess_savings_rate
    else:
        high = guess_savings_rate
    
    guess_savings_rate = (high + low) / 2
    
    if 1.0 - guess_savings_rate <= 0.0001:
        break
        
    number_of_steps += 1

if 1.0 - guess_savings_rate <= 0.0001:
    print("It is not possible to pay the down payment in three years.")
else:
    print("Best savings rate: %.4f" % guess_savings_rate)
    print("Steps in bisection search: %d" % number_of_steps)