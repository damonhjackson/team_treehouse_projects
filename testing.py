# determine if a sequence contains a particular value 
docs = "tuples are immutable sequences.tuple"

if 'tuple' in docs:
    print('tuple is here')
else:
    print('tuple is not here')

# count how many times tuple appears in document 
print(docs.count('tuple'))

# indexing 
my_pets = ('dog', 'cat', 'cat', 'chicken', 'dog')

my_pets.index('dog') # 0
my_pets.index('chicken') # 3
my_pets.index('lizard') # ValueError: 'lizard' is not in list
