bill_amount = int(input("Enter the amount of bill: "))
number_of_persons = int(input("Enter number of persons: "))
PercentOfTipFromBill = int(input("Enter perentage of tip from bill amount: "))
total_amount = bill_amount + (PercentOfTipFromBill/100)*bill_amount
Contri = total_amount/number_of_persons
print("Each should pay: ", round(Contri))

