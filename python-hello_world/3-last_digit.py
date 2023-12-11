import random
number = random.randint(-10000, 10000)
if number >= 5:
    last_digit= number % 10
else :
    last_digit= -(-number % 10)        

if last_digit >5:
    out_put ="and is greater than 5"
elif last_digit ==0:
    out_put="and is 0"
else :
    out_put="and is less than 6 not 0"    

print ("last_digit",number,"is",last_digit)        