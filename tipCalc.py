def info():
    value1 = input("How much is your bill? ")
    value2 = input("What percentage would you like to tip? Please enter a decimal value: ")
    integerCheck(value1,value2)

def integerCheck(value1,value2):
    try: 
        x = (int(value1))
        y = (float(value2))
        if type(x) == int and type(y) == float:
            if x < 0 or y < 0:
                print("Please no negative numbers!  Try again...")
                info()
            else:
                calculator(x,y)
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
        info()

def calculator(x,y):
    total = x + (x*y)
    print ("Your new total with tip is", total)

print("Tip calculator app.")
info()
