# Name: Joey and Veroniika
# Prog Purpose: This program computes PVCC college tuition & fees based on number of credits
#   PVCC Fee Rates are from: https://www.pvcc.edu/tuition-and-fees

import datetime

def main():
    outfile = 'tuition.html'
    with open(outfile, "w") as f:
        open_outfile(f)
        more = True

        while more:
            get_user_data()
            perform_calculations()
            create_output_file(f)
            yesno = input("\nWould you like to calculate tuition & fees for another student? (y/n): ")
            if yesno.lower() != "y":
                more = False

def open_outfile(file):
    file.write('<html> <head> <title> PVCC Tuition and Scholarship Report </title>\n')
    file.write('<style> td{text-align: center} </style> </head>\n')
    file.write('<body style ="background-color: #985b45; background-image: url(wp-tuition.png); color: #f8dd61;">\n')

def get_user_data():
    global inout, numcredits, scholarshipamt
    inout = int(input("Enter a 1 for IN-STATE; enter a 2 for OUT-OF-STATE: "))
    numcredits = int(input("Number of credits registered for: "))
    scholarshipamt = float(input("Scholarship amount received: "))

def perform_calculations():
    global institution_fee, tuition, cap_fee, stu_act_fee, total, balance, numcredits
    RATE_TUITION_IN = 156.71
    RATE_TUITION_OUT = 336.21
    RATE_CAPITAL_FEE = 23.50
    RATE_INSTITUTION_FEE = 1.75
    RATE_ACTIVITY_FEE = 2.90

    if inout == 1:
        tuition = RATE_TUITION_IN * numcredits
        cap_fee = 0
    else:
        tuition = RATE_TUITION_OUT * numcredits
        cap_fee = RATE_CAPITAL_FEE * numcredits

    institution_fee = RATE_INSTITUTION_FEE * numcredits
    stu_act_fee = RATE_ACTIVITY_FEE * numcredits
    total = tuition + institution_fee + stu_act_fee + cap_fee
    balance = total - scholarshipamt

def create_output_file(file):
    currency = '8,.2f'
    today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    tr = '<tr><td>'
    endtd = '</td><td>'
    endtr = '</td></tr>\n'
    sp = " "

    file.write('\n<table border="3" style ="background-color: #47161a; font-family: arial; margin: auto;">\n')
    file.write('<tr><td colspan = 2>\n')
    file.write('<h2>Piedmont Virginia Community College</h2></td></tr>')
    file.write('<tr><td colspan = 2>\n')
    file.write('*** Tuition and Scholarship Report ***\n')

    file.write(tr + 'Tuition Fee' + endtd + sp + format(tuition, currency) + endtr)
    file.write(tr + 'Institutional Fee' + endtd + sp + format(institution_fee, currency) + endtr)
    file.write(tr + 'Student Activity Fee' + endtd + sp + format(stu_act_fee, currency) + endtr)
    file.write(tr + 'Capital Fee' + endtd + sp + format(cap_fee, currency) + endtr)
    file.write(tr + 'Scholarship Amount' + endtd + sp + format(scholarshipamt, currency) + endtr)
    file.write(tr + 'Total' + endtd + sp + format(total, currency) + endtr)
    file.write(tr + 'Balance' + endtd + sp +  format(balance, currency) + endtr)

    file.write('<tr><td colspan= "2">Date/Time: ')
    file.write(today)
    file.write(endtr)
    file.write('</table>')

# Call on the main program to execute
main()