shopping_List = ["Milk", "Pasta", "Eggs", "spam", "Bread", "Rice"]

for item in shopping_List:
    if item == "spam":
        # print("I am igoring " + item)
        # continue
        break

    print("Buy " + item)

print("==============")

for i in range(0, 100, 7):
    print(i)
    if (i != 0) and (i % 11) == 0:
        break
        # print ("encontre uno")

print("==============")

for i in range(1, 21):
    if (i % 3) == 0 or (i % 5) == 0:
        continue
    print(i)

print("==============")

number = 5
multiplier = 8
answer = 0

# add your loop after this comment
for i in range(0, multiplier):
    answer += 5

print(answer)
