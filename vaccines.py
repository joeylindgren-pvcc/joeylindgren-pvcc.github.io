# Name: Joey Lindgren
# Program Purpose: This program finds the cost of pet vaccines and medications for dogs and cats
#
# Note: Pet medications prescribed by licensed veterinarians are not subject to sales tax in Virginia
#
# PET CARE MEDS Pricing
#-----------------------------
# Canine Vaccines:
#  1. Bortadella $30.00
#  2. DAPP $35.00
#  3. Influenza $48.00
#  4. Leptospirosis $21.00
#  5. Lyme Disease $41.00
#  6. Rabies $25.00
#  7. Full Vaccine Package (includes all vaccines): 15% discount
#
# Canine Heartworm Preventative Chews (price per chew; one chew per month)
#  Small dogs, Up to 25 lbs: $9.99
#  Medium-sized dogs, 26 to 50 lbs: $11.99
#  Large dogs, 51 to 100lbs: $13.99

# Feline Vaccines:
#  1. Feline Leukemia $35.00
#  2. Feline Viral Rhinotracheitis $30.00
#  3. Rabies (one year) $25.00
#  4. Full Vaccine Package (includes all vaccines): 10% discount
#
# Feline Heartworm Preventative Chews (price per chew; one chew per month)
#  One size : $8.00

import datetime

############## define global variables ###############
# define dog prices
PR_BORD = 30
PR_DAPP = 35
PR_FLU = 48

PR_ALL = 0

PR_CHEWS_SMALL = 9.99
PR_CHEWS_MED = 11.99
PR_CHEWS_LARGE = 13.99

# define cat prices
PR_LUEK = 35
PR_VIRAL_RHINO = 30
PR_RABIES = 25

PR_F_ALL = 0

PR_F_CHEWS = 8.00

def main():
    more=True
    while more:
        get_user_data()

        if pet_type.upper()=="D":
            get_dog_data()
            perform_dog_calculations()
            display_dog_results()
        else:
            get_cat_data()
            perform_cat_calculations()
            display_cat_results()
        askAgain = input("\nWould you like to process another pet (Y/N)?: ")
        if askAgain.upper() == "N" :
            more = False
            print('Thank you for trusting PET CARE MEDS with your pet vaccines and medications.')

def get_user_data():
    global pet_name, pet_type, pet_weight
    pet_name = input("Pet name: ")
    pet_type = input("Is this pet a dog (D) or cat (C)? " )
    pet_weight = input("Weight of your pet (in pounds): ")

############### DOG FUNCTIONS ###################

def get_dog_data():
    global pet_vax_type, num_chews
    dog1 = "\n** Dog Vaccines: \n\t1.Bortadella \n\t2.DAPP \n\t3.Influenza \n\t4.Lepstospirosis"
    dog2 = "\n\t5.Lyme Disease \n\t6.Rabies \n\t7.Full Vaccine Package \n\t9.NONE"
    dogmenu = dog1 + dog2
    pet_vax_type = int(input(dogmenu + "\n** Enter the vaccine number: "))

    print("\nMonthly heart worm prevention medication is reccommended for all dogs.")
    heart_yesno = input("Would you like to order monthly heartworm medication for " + pet_name + " (Y/N)? ")
    if heart_yesno.upper() == "Y":
        num_chews = int(input("How many heart worm chews would you like to order? "))

def perform_dog_calculations():
    global vax_cost, chews_cost, total, pet_vax_type

    ##### vaccines

    if pet_vax_type == 1 :
        vax_cost = PR_BORD
    
    elif pet_vax_type == 2 :
        vax_cost = PR_DAPP

    elif pet_vax_type == 3 :
        vax_cost = PR_FLU
    
    else:
        PR_F_ALL = PR_BORD + PR_DAPP + PR_FLU
        vax_cost = .85 * PR_F_ALL

    ##### heart worm chews
    if num_chews != 0 :
        if pet_weight < 25:
            chews_cost = num_chews * PR_CHEWS_SMALL
        
        elif pet_weight >= 26 and pet_weight < 50 :
            chews_cost = num_chews * PR_CHEWS_MED

        else:
            chews_cost = num_chews * PR_CHEWS_LARGE

    ##### find total
    total = vax_cost + chews_cost

    
def display_dog_results():
    moneyf = '10,.2f'
    line=('------------------------------')

    print('************* Piedmont Virginia Community College *************')
    print('Tuition and Scholarship Report')
    print(line)
    print('Vaccines for your dog     $ ' + format(vax_cost,moneyf))
    print('Chews for your dog        $ ' + format(chews_cost,moneyf))
    print('Total                     $ ' + format(total,moneyf))
    print(line)
    print(str(datetime.datetime.now()))

############## CAT functions ##################
def get_cat_data():
    global pet_vax_type, num_fchews
    cat1 = "\n** Cat Vaccines: \n\t.1 Feline Leukemia \n\t.2 Feline Viral Rhinotracheitis"
    cat2 = "\n\t.3 Rabies(one year) \n\t.4 Full Vaccine Package"
    catmenu = cat1 + cat2
    pet_vax_type = int(input(catmenu + "\n** Enter the vaccine number: "))

    print("\nMonthly heart worm prevention medication is recommended for all cats. ")
    heart_yesno = input("Would you like to order monthly heartworm medication for " + pet_name + " (Y/N)? ")
    if heart_yesno.upper() == "Y":
        num_fchews = int(input("How many heart worm chews would you like to order? "))
    
    


def perform_cat_calculations():
    global vax_cost, chews_cost, total, num_fchews, pet_vax_type

    ##### vaccines

    if pet_vax_type == 1 :
        vax_cost = PR_LUEK 
    
    elif pet_vax_type == 2 :
        vax_cost = PR_VIRAL_RHINO
    
    elif pet_vax_type == 3 :
        vax_cost = PR_RABIES

    else:
        PR_ALL = PR_LUEK + PR_VIRAL_RHINO + PR_RABIES
        vax_cost = .90 * PR_F_ALL

    chews_cost = num_fchews * PR_F_CHEWS
    total = vax_cost + chews_cost

def display_cat_results():
    moneyf = '10,.2f'
    line=('------------------------------')

    print('************* Piedmont Virginia Community College *************')
    print('Tuition and Scholarship Report')
    print(line)
    print('Vaccines for your cat     $ ' + format(vax_cost,moneyf))
    print('Chews for your cat        $ ' + format(chews_cost,moneyf))
    print('Total                     $ ' + format(total,moneyf))
    print(line)
    print(str(datetime.datetime.now()))

main()