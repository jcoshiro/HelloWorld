#         432109876543210
#         01234567890123
parrot = "Norwegian Blue"


print(parrot[0:8:2])
print(parrot[0:8:3])
print(parrot[0:8:4])

number = "7:999;555.666,333-222,111"
separators = (number[1::4])
print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values]) #print Integer
print(values)   # print Strings


text = "geek for geeks"
parse = text.split()
print(parse[0] + " " + parse[1])

word = "geeks, for, geeks"
print(word.split(','))

word = "geeks:for:geeks"
print(word.split(':'))

word = "CatBatSatFatOra"
print([word[i:(i+3)] for i in range(0,len(word),3)])





"""
print(parrot[0:6])  # Norweg , not including position 6
print(parrot[3:5])
print(parrot[0:9])
print(parrot[:9])
print(parrot[10:14])
print(parrot[10:])

print(parrot[:6])
print(parrot[6:])

print(parrot[:])

print(parrot[:6] + parrot[6:])
"""





"""
print(parrot)
print(parrot[3])    #w print individual character count from zero
print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])

print()

print(parrot)
print(parrot[-11])    #w negative index !
print(parrot[-1])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])

print()
print(parrot[3 - 14])    #w print individual character count from zero
print(parrot[4 - 14])
print(parrot[9 - 14])
print(parrot[3 - 14])
print(parrot[6 - 14])
print(parrot[8 - 14])
"""