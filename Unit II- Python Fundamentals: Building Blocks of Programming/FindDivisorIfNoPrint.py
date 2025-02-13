#find the divisor of the given numbers.If no print it as prime number
a = int(input("Enter a number: "))
b= []
i = 1
while(i <= a):
    if a%i== 0:
        b.append(i)
    i = i + 1
print(b)
