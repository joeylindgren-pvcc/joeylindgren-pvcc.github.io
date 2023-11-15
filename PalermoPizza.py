# Name: Joey Lindgren
# Program Purpose: This program finds the cost of a meal at Palermo Pizza
#
# 
# Pizza Menu Pricing
#-----------------------------
# Pizza:
#  1. Small Pizza $9.99
#  2. Medium Pizza $12.99
#  4. Large Pizza $17.99
#  5. Extra Large Pizza $21.99
#  Drinks: $3.99
#  Breadsticks: $6.99
#  Sales Tax Rate: 5.5% (0.055)

import datetime

############## define global variables ###############
# define pizza prices
PR_SMA = 9.99
PR_MED = 12.99
PR_LAR = 17.99
PR_XLR = 21.99

PR_NONE = 0

PR_DRINK = 3.99
PR_BREAD = 6.99

SALES_TAX_RATE = 0.055

def main():
    more=True
    while more:
        get_user_data()

        if pizza_size.upper()=="Y":
            get_pizza_data()
            perform_pizza_calculations()
            perform_calculations()
            display_results()
        else:
            get_user_data()
            perform_calculations()
            display_results()
        askAgain = input("\nWould you like to make another order (Y/N)?: ")
        if askAgain.upper() == "N" :
            more = False
            print('Thank you for dining at Palermo Pizza! ')

def get_user_data():
    global size_pizza, amt_drinks, amt_bread, amt_pizza, pizza_size
    pizza_type = input("Would you like a pizza?: ")
    pizza_size = input("What size pizza would you like?: ")
    amt_drinks = input("How many drinks would you like?: " )
    amt_bread = input("How many orders of breadsticks?: ")

############### DOG FUNCTIONS ###################

def get_pizza_data():
    global pizza_size, pizza1, pizza2, pizzamenu
    pizza1 = "\n** Pizza Sizes: \n\t1.Small \n\t2.Medium"
    pizza2 = "\n\t3.Large \n\t4.Extra Large \n\t5.NONE"
    pizzamenu = pizza1 + pizza2
    pizza_size = int(input(pizzamenu + "\n** Enter the size of pizza you'd like: "))


def perform_pizza_calculations():
    global cost_pizza, pizza

    ##### pizza sizes

    if pizza_type == 1 :
        cost_pizza = PR_SMA
    
    elif pizza_type == 2 :
        cost_pizza = PR_MED

    elif pizza_type == 3 :
        cost_pizza = PR_LAR
    
    elif pizza_type == 4 :
        cost_pizza = PR_XLR
    
    else:
        cost_pizza= PR_NONE
 
       

    ##### find total
    pizza = cost_pizza

def perform_calculations():
    global subtotal, sales_tax, total, cost_drinks
    cost_pizza = pizza
    cost_breadsticks = amt_bread * PR_BREAD
    cost_drinks = amt_drinks * PR_DRINK
    subtotal = cost_drinks + cost_pizza + cost_breadsticks
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + sales_tax


def display_results():
    moneyf = '10,.2f'
    print('--------------------------------------')
    print('****** PALERMO PIZZA ******')
    print('**** BEST PIZZA IN TOWN! ****')
    print('--------------------------------------')
    print('Pizza(s)      $ ' + format(cost_pizza,moneyf))
    print('Breadsticks   $ ' + format(cost_breadsticks,moneyf))
    print('Drinks        $ ' + format(cost_drinks,moneyf))
    print('--------------------------------------')
    print('Subtotal      $ ' + format(subtotal,moneyf))
    print('Sales Tax     $ ' + format(sales_tax,moneyf))
    print('Total         $ ' + format(total,moneyf))
    print('--------------------------------------')
    print(str(datetime.datetime.now()))

################# call on main program to execute #############
main()
