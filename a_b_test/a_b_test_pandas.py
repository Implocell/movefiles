import pandas as pd

'''
test different prics to find optimal price
'''

df = pd.read_csv('clicks.csv')

df['is_purchase'] = df.click_day.apply(
  lambda x: 'Purchase' if pd.notnull(x) else 'No Purchase'
)

purchase_counts = df.groupby(['group', 'is_purchase'])\
	.user_id.count().reset_index()

#print purchase_counts

num_visits = len(df)

p_clicks_099 = (1000 / 0.99) / num_visits
p_clicks_199 = (1000 / 1.99) / num_visits
p_clicks_499 = (1000 / 4.99) / num_visits

from scipy.stats import binom_test

pvalueA = binom_test(316, 1666, p_clicks_099)
pvalueB = binom_test(183, 1666, p_clicks_199)
pvalueC = binom_test(83, 1666, p_clicks_499)

final_answer = 4.99

def best_pvalue(a, b, c):
  winner = 0
  value = 100
  
  if(a < value):
    value = a
    winner = 0.99
  if(b < value):
    value = b
    winner = 1.99
  if(c < value):
    value = c
    winner = 4.99
  
  return winner

print(best_pvalue(pvalueA, pvalueB, pvalueC))