# dictionary
course = {'teacher':'Ashley', 'title':'Introducing Dictionaries', 'level':'Beginner'}

print(course['teacher'])

# assigning a dictionary a new vlaue
course['level'] = 'intermediate'
print(course)

# adding a value to a dictionary
course['stages'] = 2
print(course)

# deleting a value from a dictionary
del(course['stages'])
print(course)

# iterate over dictionaries
for key,value in course.items():
    print(key)
    print(value)
