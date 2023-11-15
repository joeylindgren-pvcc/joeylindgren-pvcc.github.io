#Name: Joey Lindgren
#Program Purpose: This program finds the personal property taxes for vehicles in Charlottesville

import datetime

###############define global variables#####################
# define personal property tax rate
PROP_TAX_RATE = 0.042

# define personal property  tax relief
PROP_TAX_REL = 0.33
tax_relief_amt = 0

def main():
    more=True
    while more:
        get_user_data()

        if elig_tax_relief.upper() == "Y":
            perform_prop_relief_calculations()
            display_results()
        else:
            perform_prop_calculations()
            display_results()
        askAgain = input("\n Would you like to process another vehicle (Y/N)?: ")
        if askAgain.upper() == "N" :
            more = False
            print('Please call our office with any questions or concerns, thank you!')
    
def get_user_data():
    global vehicle_value, elig_tax_relief
    vehicle_value = float(input("What is the assessed value of the vehicle you are filing? "))
    elig_tax_relief = input("Some vehicles are eligible for tax relief. Is your vehicle primarily used for non-business purposes (Y/N)? ")


def perform_prop_relief_calculations():
    global annual_tax_amt, tax_relief_amt, vehicle_value, tax_due, total
    annual_tax_amt = vehicle_value * PROP_TAX_RATE
    tax_due = annual_tax_amt / 2
    tax_relief_amt = PROP_TAX_REL * tax_due
    total = tax_due - tax_relief_amt



   
    


def perform_prop_calculations():
    global annual_tax_amt, vehicle_value, bill, total, tax_due, tax_relief_amt
    annual_tax_amt = vehicle_value * PROP_TAX_RATE
    tax_due = annual_tax_amt / 2
    total = tax_due + tax_relief_amt
    
    


def display_results():
    moneyf = '10,.2f'
    print('--------------------------------------------------------------')
    print('****** City Of Charlottesville, Virginia ******')
    print('--------------------------------------------------------------')
    print('Assessed Value                     $ ' + format(vehicle_value,moneyf))
    print('Full Tax Amount (6 Months)         $ ' + format(tax_due,moneyf))
    print('Relief Amount                      $ ' + format(tax_relief_amt,moneyf))
    print('Tax Due                            $ ' + format(total,moneyf))
    print('--------------------------------------------------------------')
    print('Total Amount Due                   $ ' + format(total,moneyf))
    print('--------------------------------------------------------------')
    print(str(datetime.datetime.now()))

################# call on main program to execute #############
main()






