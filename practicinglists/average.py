lando_2021_results = [4,3,5,8,3,5,5,5,3,4,14,10,2,7,7,8,10,10,9,10,7]

def average(nums):
    total = 0
    for num in nums:
        total += num
    return total/len(nums)

print(average(lando_2021_results))

# find the lowest number in lando_2021_results
min = lando_2021_results[0]
for num in lando_2021_results:
    if num < min:
        min = num
print(min)

# find maximum
max = 4
for worst in lando_2021_results:
    if worst > max:
        max = worst
print(max)