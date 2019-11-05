import numpy as np
import noshmishmosh as nosh
'''
Script is to find sample size in AB testing, this requires a calculator to input the outcome of this file.
'''


all_visitors = nosh.customer_visits
paying_visitors = nosh.purchasing_customers

total_visitor_count = len(all_visitors)
paying_visitor_count = len(paying_visitors)

baseline_percent = paying_visitor_count * 100.0 / total_visitor_count

print(baseline_percent)

payment_history = nosh.money_spent
average_payment = np.mean(payment_history)
new_customers_needed = np.ceil(1240 / average_payment)

percentage_point_increase = new_customers_needed * 100.0 / total_visitor_count

print(percentage_point_increase)

minimum_detectable_effect = (percentage_point_increase / baseline_percent ) * 100

print(minimum_detectable_effect)

ab_sample_size = 290