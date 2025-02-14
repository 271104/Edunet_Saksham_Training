import random
name = ["Mahesh", "Tirth", "Tejas", "Pravin", "Uday", "Shlok", "Yogesh"]
n = random.randint(0,6)
if n == 0:
    print("Bill has to paid by ",name[0])
elif n == 1:
    print("Bill has to paid by ",name[1])
elif n == 2:
    print("Bill has to paid by ",name[2])
elif n == 3:
    print("Bill has to paid by ",name[3])
elif n == 4:
    print("Bill has to paid by ",name[4])
elif n == 5:
    print("Bill has to be paid by ",name[5])
else:
    print("Bill has to be paid by ",name[6])

