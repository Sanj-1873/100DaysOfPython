age = int(input("How old are you?"))
days_lived = age * 365
weeks_lived = age * 52
months_lived = age * 12
print("You have lived {} days, {} weeks, and {} months.".format(days_lived, weeks_lived, months_lived))

days_left = (90 - age) * 365
weeks_left = (90 - age) * 52 
months_left = (90 - age) * 12
print("If you live till 90, you have {} days, {} weeks, and {} months left".format(days_left, weeks_left, months_left))