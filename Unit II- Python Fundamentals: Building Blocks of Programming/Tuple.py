#Tuple:Tuples are used to store multiple items in a single variable.
#A tuple is a collection which is ordered and unchangeable.
#Tuples are written with round brackets.
thistuple = ("mahesh", "Kishor", "anand", "apple", "cherry","Kiwi", "melon")
print(thistuple)
#length of tupple
print("Length of tuple is: ",len(thistuple))
#data type
print(type(thistuple))
#negative indexing
print(thistuple[-1])#prints last element
print(thistuple[-2])#prints last second element
#ranges
print(thistuple[2:6])#prints elements from index 2 to 6
print(thistuple[:4])#prints elements before index 4
print(thistuple[4:])#prints elements after index 4
#changing tuple
List = list(thistuple)
List.append("Yoo")
print(List)
print(type(List))
thistuple = tuple(List)
print(type(thistuple))
