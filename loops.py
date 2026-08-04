#for loop usage
values = ["Areen", "Anshula", 23, "Sri Lankan", True]
fruits = ["Apple", "Orange", "Banana", "Grapes", "Pine apple"]

for val in values:
    print(f"Value {val}")

for fruit in range(len(fruits)):
    print(fruit, end=", ")    

print("\n")

text = "AreenAnshula"
for letter in text:
    print(letter, end="")    

print("\n")

num = [1, 2, 3, 4, 5]
res = [n ** 2 for n in num]
print(res)    

#using map
mapIsHere = list(map(lambda a: a * 2, num))
print(mapIsHere)