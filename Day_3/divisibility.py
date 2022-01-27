number = input('What number do you want to use?')
divisibility = {}

#Divisibility by  2
if(float(number) % 2 == 0):
    divisibility[2] = True    
else:
    divisibility[2] = False 

# Divisiblity by 3
digit_sum = 0
for i in number:
    digit_sum = int(digit_sum) + int(i)

if(digit_sum % 3 == 0):
    divisibility[3] = True
else:
    divisibility[3] = False



# Divisiblity by 4
if(len(number) == 1):
    sum_last_2_digits = int(number[-1])
else:
    sum_last_2_digits = int(number[-1]) + int(number[-2])

if(sum_last_2_digits % 4 and sum_last_2_digits>4):
    divisibility[4] = True
else:
    divisibility[4] = False


#Divisiblity by 5
if(number[-1] == '0' or number[-1] == '5'):
    divisibility[5] = True
else:
    divisibility[5] = False

# Divisibility by 6 
if(divisibility[2] and divisibility[3]):
    divisibility[6] = True
else:
    divisibility[6] = False

#Divisibility by 7 
remaining = int(number)
while(remaining > 100 ):
    last_digi = int(str(remaining)[-1]) 
    last_digi = last_digi * 2 
    remaining = int(str(remaining)[:-1]) 
    remaining = remaining - last_digi

if(remaining % 7 == 0):
    divisibility[7] = True
else:
    divisibility[7] = False

# Divisiblity by 8 
if(len(number) > 2):
    total_sum = int(number[-1] + number[-2] + number[-3])
else:
    total_sum = int(number)

if(total_sum % 8 == 0):
    divisibility[8] = True
else:
    divisibility[8] = False

#Divisibility by 9
if digit_sum % 9 and digit_sum > 9: 
    divisibility[9] = True
else: 
    divisibility[9] = False

# Divisibility by 10

if(number[-1] == '0' ):
    divisibility[10] = True
else:
    divisibility[10] = False

print(divisibility)
for i in divisibility:
    if divisibility[i]:
        print('Divisible by {}'.format(i))