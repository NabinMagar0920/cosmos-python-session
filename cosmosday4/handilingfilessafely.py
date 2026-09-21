with open("writenote.txt", "w") as f:
     f.write("Ram is good boy")

with open("writenote.txt", "r") as f:
     content = f.read()
     print(content)