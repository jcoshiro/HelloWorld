for i in range(1, 13):
    print("No. {0:2} squared is {1:4} and cubed is {2:4}".format(i, i ** 2, i ** 3))

print()

for i in range(1, 13):
    print("No. {0:<2} squared is {1:<3} and cubed is {2:<4}".format(i, i ** 2, i ** 3))

first_name = "john"
last_name = "Cleese"
age = 78
# print(first_name + last_name + age)


a = 45
b = 15
c = 3
print(a - b / c)

days = "Mon, Tue, Wed, Thu, Fri, Sat, Sun"
print(days[::5])

data = "1:A, 2:B, 3:C, 4:D, 5:E, 6:F, 7:G, 8:H"
print(data[::5])

flower = "blue violet"
print('blue' in flower)
