x = int(input("Enter any number:"))
if x % 3 == 0 and x % 5 == 0:
    print("FizzBuzz! number is divided by both 3 and 5.")
elif x % 3 == 0:
    print("FIZZZ! number is divided by 3")
elif x % 5 == 0 :
    print("BUZZZ! number is divided by 5") 
else:
    print("Number is not divisible by 3 and 5.")
    