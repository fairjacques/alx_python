import random
number = random.randint(-10000, 10000) 
if number >= 0:
    last_digit = number %10
else :
    last_digit = -(-number %10)     

if last_digit >5:
    out_put ="and is greater than 5"    
print ("Last digit of", number,"is",last_digit,out_put)        