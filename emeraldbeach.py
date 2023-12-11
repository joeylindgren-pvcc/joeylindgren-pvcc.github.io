import csv
from datetime import datetime

# Room Codes and Room Rates
room_rates = {'SR': 195.00, 'DR': 250.00, 'SU': 350.00}

# Tax Rates
sales_tax_rate = 6.5 / 100
occupancy_tax_rate = 11.25 / 100

# Read data from CSV file
guests = []
with open('emerald.csv', 'rt') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        guests.append(row)
        
# Function to calculate total amount
def calculate_total(room_type, num_nights):
    room_rate = room_rates.get(room_type, 0)
    subtotal = room_rate * int(num_nights)
    sales_tax = subtotal * sales_tax_rate
    occupancy_tax = subtotal * occupancy_tax_rate
    total = subtotal + sales_tax + occupancy_tax
    return subtotal, sales_tax, occupancy_tax, total

# HTML file
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Hotel Sales Report</title>
    <style>
        body {{
            background-image: url('wp-wallpaperbeach.jpeg');
            background-size: cover;
            font-family: Arial, sans-serif;
        }}
        table {{
            width: 60%;
            margin: 50px auto;
            border-collapse: collapse;
            border: 2px solid #ddd;
            background-color: white;
            opacity: 0.9;
        }}
        th, td {{
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }}
        th {{
            background-color: #4caf50;
            color: white;
        }}
        h2 {{
            text-align: center;
            color: #4caf50;
        }}
        p {{
            text-align: center;
        }}
    </style>
</head>
<body>
    <h2>Emerald Beach Hotel & Resort</h2>
    <p>Sales Report Date/Time: {datetime.now().strftime('%Y-%m-%d %H:%M')}</p>
    <table>
        <tr>
            <th>Last Name</th>
            <th>First Name</th>
            <th>Number of Nights</th>
            <th>Subtotal</th>
            <th>Sales Tax</th>
            <th>Occ. Tax</th>
            <th>Total</th>
        </tr>
"""

# Calculate totals and append to HTML content
grand_total = 0
for guest in guests:
    last_name, first_name, room_type, num_nights = guest
    subtotal, sales_tax, occupancy_tax, total = calculate_total(room_type, num_nights)
    grand_total += total
    html_content += f"""
        <tr>
            <td>{last_name}</td>
            <td>{first_name}</td>
            <td>{num_nights}</td>
            <td>${subtotal: .2f}</td>
            <td>${sales_tax: .2f}</td>
            <td>${occupancy_tax: .2f}</td>
            <td>${total: .2f}</td>
        </tr>
"""

#Grand Total
html_content += f"""
        <tr>
            <th colspan="6">Grand Total</th>
            <td>${grand_total: .2f}</td>
        </tr>
    </table>
</body>
</html>
"""

with open('hotelsalesrep.html', 'w') as html_file:
    html_file.write(html_content)

print("Sales report generated successfully.")



