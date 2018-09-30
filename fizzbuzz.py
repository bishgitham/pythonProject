for item in range(1,50):
    if (item % 5) == 0 and (item % 3) == 0 :
        print (item , ":", "fizzbuzz")
    elif (item % 3) == 0 :
        print (item , ":", "fizz")
    elif (item % 5) == 0 :
        print (item , ":", "buzz")
