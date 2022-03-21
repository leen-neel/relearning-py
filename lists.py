mylist = ["apple", "banana", "cherry"]

print(mylist)

# length of list
print(len(mylist))

# looping thru list
for x in mylist: 
    print(x)

print()

# negative indexing
print(mylist[-1])

# range of indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
print(thislist[:4])
print(thislist[4:])

print()

# adding and removing
thislist.append("test") # append
print(thislist)

thislist.remove("cherry")
print(thislist)
