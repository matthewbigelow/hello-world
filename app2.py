number = int(input("Give me a number:"))

if number < 0: 
    number = -number 
    print("negative number")
    print ("The absolute value of number is", number)
elif number>0: 
    print("Positive number")
    print ("The absolute value of number is", number)

