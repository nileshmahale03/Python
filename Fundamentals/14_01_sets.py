#sets

#unordered
#unique

my_set = {1, 2, 3}
print(my_set, type(my_set), len(my_set))

my_set = set()
my_set.add(1)
my_set.add(3)
my_set.add(5)
my_set.add(5)
my_set.add(5)

print(my_set, type(my_set), len(my_set))

#remove() 
my_set.remove(3)

print(my_set, type(my_set), len(my_set))

#loop
my_set = {1, 2, 3}

for element in my_set:
    print(element)

#remove duplicate from a list
my_list = [1, 2, 3, 4, 5, 1, 2, 5]

my_set = set(my_list)

print(my_set)  # Output: {1, 2, 3, 4, 5}

my_list_no_duplicates = list(my_set)

print(my_list_no_duplicates)

#in, not in 
my_set = {"Cat", "Dog", "Mouse"}

contains_cat = "Cat" in my_set   # True
contains_lion = "Lion" in my_set # False