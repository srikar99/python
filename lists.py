
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
print(friends)
# extend allows us to append another list to the end of the first list
# friends.extend(lucky_numbers)
# print(friends)
# append allows us to append to add another item to the list
# append always adds to the end of the list
friends.append("Creed")
print(friends)
# insert allows us to add item to a list at any desired position
friends.insert(1, "Kelly")
print(friends)
# remove allows us to remove item from a list
friends.remove("Jim")
print(friends)
# pop allows us to remove element from the end
friends.pop()
print(friends)
# clears all the elements
# friends.clear()
# print(friends)

# get the index of an element in list
print(friends.index("Kelly"))

friends.insert(2, "Jim")
friends.insert(3, "Jim")
# get the count of elements in the list
print(friends.count("Jim"))
# sort
friends.sort()
print(friends)
# reverse
friends.reverse()
print(friends)
# copy
office_friends = friends.copy()
print(office_friends)



