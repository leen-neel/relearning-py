i = 1

while i < 6: 
    print(i)
    i += 1

i = 0
print()

while i < 6: 
    i += 1
    if i == 3:
        continue
    print(i)
else:
    print("dead lol")
    