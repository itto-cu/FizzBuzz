# FIZZ BUZZ
# Charlotte Niblett
# feb 10 2022

#print numbers 1-100 replacing numbers dvided by 3 with fizz, numbers dvided by 5 with buzz, and numbers divided both with fizzbuzz
for num in range(1,101):
    if num % 3 == 0 and num %5 ==0:
        print("fizzbuzz")
    elif num % 5 ==0:
        print ("buzz")
    elif num % 3 == 0:
        print ("fizz")
    else:
        print (num)
        