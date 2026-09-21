def checkEvenOdd (num):
  if num % 2 ==0:
    return f"{num} is even"
  else:
    return f"{num} is odd"          

number = int (input("enter a number:"))                 
result = checkEvenOdd(number)
print(result)
    