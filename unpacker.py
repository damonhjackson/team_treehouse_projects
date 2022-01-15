#unpack a tuple inside of a function

def unpacker():
    return (1, 2, 3)

var1, var2, var3 = unpacker()

print(var1)
print(var2)
print(var3)

# seperate user first and last name using packer

# split first and last name by space
full_name = input('Enter your full name: \n').split(' ')
print(full_name)
