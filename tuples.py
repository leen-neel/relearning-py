thistuple = ("apple", "banana", "cherry", "banana", "cherry")

print(thistuple)

(test1, test2, *test3) = thistuple
print(test1, test2, test3)
