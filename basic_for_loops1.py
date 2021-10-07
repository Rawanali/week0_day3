
# Basic
for x in range(1,151):
    print(x)



# Multiples of Five
for x in range(5,5001):
    print(5*x)


# Counting, the Dojo Way
for x in range (1,101,1):
        if x % 5 == 0:
            print ('Coding')
        if x % 10 == 0:
            print ('Dojo')


# Whoa. That Sucker's Huge 
sum = 0 
for x in range(0,50001):
    if x % 2 != 0: 
        sum = sum + x
        
print("the sum of all odd number from 0 to 50000 is {} ".format(sum))


# Countdown by Fours
for x in range(2018,0,-4):
    print(x)
