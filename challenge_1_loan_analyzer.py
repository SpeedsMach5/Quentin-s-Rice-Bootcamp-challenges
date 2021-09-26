import csv
from pathlib import Path

loan_costs = [500, 600, 200, 1000, 450]
number_of_loans = loan_costs
print(f"this is the number of loans : {len(loan_costs)}")

total_loan_amount=loan_costs
print(f"this is the amount  of loans:${sum(total_loan_amount)}")

average_loan_price = (sum(total_loan_amount) / len(loan_costs))
print(f"this is the average cost of loans:${average_loan_price}")
    

 loan = {
      "loan_price": 500,
      "remaining_months": 9,
      "repayment_interval": "bullet",
      "future_value": 1000,
  }

present_value = 1000 / (1+.2)**9
print(f"This is the present value:${present_value: .2f}")

def get():
    print (f"this is the future_value", 1000)
    print(f"these are the numbe of remaining_months", 9)

get()

fair_value = 1000 / (1+.2/12)**9
print(f"fair value of the loan is: ${fair_value: .2f}")

if present_value >= fair_value:
    print("the loan is a good buy")
else:
    print ("don't buy the loan")

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    }
]

"""I give up. I have been working on this challenge for too long (over a week with 90% of that time stuck at this level) and cannot get past the loop aspect.
 Can you please provide a resource outside of this course for me to reseach to try and understand what I am doing wrong? My Google and Youtube searches have
  not been helpful. Thank you"""


loan_price = [700,500,200,900]

inexpensive_loans = []

for inexpensive_loans in loan_price:

    if inexpensive_loans <=500:
        inexpensive_loans.append(inexpensive_loans)





   
