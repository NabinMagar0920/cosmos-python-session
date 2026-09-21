Shopping_list = ["Pen", "Book", "Copy" ]
Shopping_list.append("Phone")
print(f"\nShopping list after append: {Shopping_list}\n")
Shopping_list.remove("Pen")
print(f"\nShopping_list after removel of item: {Shopping_list}")
if "Copy" in Shopping_list: 
   print (True)
length = len("Shopping_list")
print(f"length of the Shopping_list is; {length}\n")
for item in Shopping_list[1:4]:
   print(item)