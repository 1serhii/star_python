# Solution for test assigment

Here you can find task and solution for assigment

## Task

Using Python, design and implement an object-oriented approach capable of representing different types of customers for a company.

Types:
The employer for this project has 3 types of customers:   Subscription, Cash, and Account

Longevity:
All customers have a period of time they have been engaged

Sales:
All customers will have sales that can be three types:
Subscription,
Product,
Upgrade
Cash customers cannot buy subscription products

Exercise:   Write a program to output to screen information about a list of customers.   For each customer, print the name of the customer with a suffix indicating whether the customer is a subscription[s], Cash[C], or Account[A], Duration of time as a customer, and list of purchases in the last 1 year.

Example:
Customer Name:  US government
Customer Type:  Account
Longevity:  3 years
Expected output:
Name:  US government [A], Duration:  3 years, Purchases in the last year: Product A [S],  3 x Product B [C]

### Prerequisites
1. Python 3.6+
2. Install requirements by following command
```
pip install -r requirements.txt
```

### Run Tests

All tests are stored in file test_app.py
To execute all of them, navigate to project root directory
and run following command:

```
pytest test_app.py
```

and if you want to see report:
```
pytest test_app.py --html=report.html --self-contained-html
```