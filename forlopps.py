#for i in range (1, 20):
#    print("i is now {} ".format(i))

#number = ("1 ,23 , 877, 126, 777, 546, 342, 675, 899")
#print(len(number))
#for i in range(0 , len(number)):
#    print(number[i])


number = ("1 ,23 , 877, 126, 777, 546, 342, 675, 899")
cleanedNumber = ''
print(len(number))
for i in range(0 , len(number)):
    if number[i] in "0123456789":
        cleanedNumber = cleanedNumber + number[i]
        print(number[i],end = " ")
newNumber =int(cleanedNumber)
print("\n The number is {0} ".format(newNumber))


number = ("1 ,23 , 877, 126, 777, 546, 342, 675, 899")
cleanedNumber = ''
for char in number:
    if char in "0123456789":
        cleanedNumber = cleanedNumber + char
newNumber =int(cleanedNumber)
print("\n The number is {0} ".format(newNumber))

for i in range (0, 100, 5):
    print("the number i is {0}".format(i))


quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""

for char in quote:
    if char in "ABCDEFEGHIFGHIJKLMNOPQRSTUVWXYZ":
        print(char)

for i in range (0, 100, 7):
    print(i)
    #print("The number divisible by 7 is {0} ".format(i))