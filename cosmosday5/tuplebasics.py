#1 creation & type 
fruits = ("apple", "banana", "mango")
single = (10,) #comma required for single item
mixed = ("Ram", 25, "Developer")
#2 Accessing & slicng 
print(fruits[0], fruits[-1]) 
print(fruits[0:2])
#3 unpackig
name, age, role = mixed
print(f"{name} is {age} as {role}")
#4 operation & methods
nums = (4, 2, 7, 2)
print("count of 2:", nums.count(2))
combined = fruits + ("cherry",)
print("total items:", len(combined))
#5 nested tuple
nested = ("point", (3, 4))
print("X:", nested[1][0]) 