# for in loop
my_name = 'Damon Jackson'
for letter in my_name:
    print(letter)
print

# enumerate function 
groceries = ['roast beef', 'cucumbers', 'lettuce', 'peanut butter', 'bread', 'dog food']

# list the groceries in order starting from 1
for index, item in enumerate(groceries, 1):
    print(f'{index}. {item}')
   
# looping with ranges
for i in range(0, 10, 1):
    print(i)

# slices 

nums = [1, 2, 3, 4, 5, 6, 7, 8]
nums_partial = nums[0::2]
print(nums_partial)

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
colors_partial = colors[3:6]
print(colors_partial)
