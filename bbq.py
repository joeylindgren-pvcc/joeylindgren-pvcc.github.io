# Name: Joey Lindgren
# Prog Purpose: This program finds the cost of a Barbeque Buffet
# Price for one adult meal: $19.95
# Price for one child meal: $11.95
# Service Fee Rate: 10%
# Sales tax rate: 6.2%

import datetime

################ define global variables #################
# define tax rate and prices
ADULT_PRICE = 19.95
CHILD_PRICE = 11.95
PR_DRINK = 2.00
SERVICE_FEE_RATE = 0.10
SALES_TAX_RATE = 0.062

#define global variables
adult_cost = 0
child_cost = 0
num_adults = 0
num_children = 0
num_drinks = 0
subtotal = 0
cost_tickets = 0
cost_popcorn = 0
cost_drinks = 0
sales_tax = 0
total = 0

################ define program functions ##################
def main():

    more_food = True

    while more_food:
        get_user_data()
        perform_calculations()
        display_results()

        askAgain = input("\nWould you like to order again? (Y or N)?: ")
        if askAgain.upper() == "N" or askAgain == "n":
            more_food = False
            print("Thank you for your order. Enjoy your meal!")

def get_user_data():
    global num_adults, num_children, num_drinks
    num_adults = int(input("Number of adults eating today: "))
    num_children = int(input("Number of children eating today: "))
    num_drinks = int(input("Number of drinks:"))

def perform_calculations():
    global subtotal, sales_tax, total, children_cost, adult_cost, cost_drinks
    adult_cost = num_adults * ADULT_PRICE
    child_cost = num_children * CHILD_PRICE
    cost_drinks = num_drinks * PR_DRINK
    subtotal = cost_drinks + adult_cost + child_cost
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + sales_tax

def display_results():
    moneyf = '10,.2f'
    print('--------------------------------------')
    print('****** BRANCH BARBEQUE BUFFET ******')
    print('**** The Best Barbeque in Town! ****')
    print('--------------------------------------')
    print('Adult Meal(s) $ ' + format(adult_cost,moneyf))
    print('Kids Meal(s)  $ ' + format(child_cost,moneyf))
    print('Drinks        $ ' + format(cost_drinks,moneyf))
    print('--------------------------------------')
    print('Subtotal      $ ' + format(subtotal,moneyf))
    print('Sales Tax     $ ' + format(sales_tax,moneyf))
    print('Total         $ ' + format(total,moneyf))
    print('--------------------------------------')
    print(str(datetime.datetime.now()))

################# call on main program to execute #############
main()