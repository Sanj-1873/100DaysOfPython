print('Welcome to the tip calculator') 
bill_total = float(input('What was the total bill?'))
num_of_people = float(input('How many people is the bill going to be split between?'))
tip_percentage = float(input('What percentage of tip would you like to give?'))

tip_total = (tip_percentage/100) * bill_total
total_amount_due = bill_total + tip_total 
payment_per_person = total_amount_due / num_of_people

print('Each person owes: {:.2f}'.format(payment_per_person))

