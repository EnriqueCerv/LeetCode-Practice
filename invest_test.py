# %%
import numpy as np
import matplotlib.pyplot as plt
# %%
def portfolio_value(invested, price = 1.6527, dividend = 0.0064):
    return invested/price * dividend + invested

init_amount = amount = 5000
deposit = 1000
t = 12
for i in range(t):
    amount = portfolio_value(amount + deposit)
    print(amount)

tot_invested = init_amount + t*deposit
tot_val = amount * 0.9918
tot_gain = tot_val - tot_invested
tot_percentage = tot_gain / tot_invested * 100

print('Total invested', tot_invested)
print('Total value', tot_val)
print('Total gain', tot_gain)
print('Total gain percentage', tot_percentage)


    