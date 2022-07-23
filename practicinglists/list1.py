waitlist = ['tom', 'aria', 'amir']

# update index
waitlist[1] = 'ozzy'

# append adds to end of list
waitlist.append('aria')
waitlist.append('jorge')

# extend accepts an iterable and appends each item from that iterable to the end of the list
people = ['charlie', 'drew', 'emi']
waitlist.extend(people)

# Insert element to be inserted into the list. Index before which to insert the element
# insert(index, element)
waitlist.insert(0, 'arnold')
waitlist.insert(3, 'uma')

#slices [start:stop:step]
print(waitlist[5:7])
print(waitlist[0:7:2])
print(waitlist)

print("*********************************************")

nums = [4,5,6,7]
nums[1:3] = ['a', 'b', 'c', 'd']
print(nums[1:5])

nums[1:5] = [5]
print(nums)