# the clear() method removes all items from a list
# remove() removes the first element in the list that has a value of x
# pop() method removes AND returns the last element from a list. pop(idx) accepts an index

nums = [1,2,3, "tuna", 4,5,6, "hello",]
added_nums = [7,8,9,10]
print(nums)
print(added_nums)

nums.extend(added_nums)
nums.remove("hello")
nums.remove('tuna')
added_nums.append(11)
print(added_nums)

print(nums)

# pop(idx) will remove and return from the index of 0
next_person = nums.pop()
print(nums.pop(0))

# 2 should be removed
print(nums)

# the del statement (it's not a method!) can be used to delete
# an item from a specific index in a list
del nums[4:]
print(nums)

# list will now be cleared
print(nums.clear())

