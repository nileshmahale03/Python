#list
#collection of items
#ordered, mutable, allows duplicate, heterogeneous
#[]

empty_list1 = []
empty_list2 = list()
numbers = list(map(int, input().split()))
words = input().split()

my_list = [1, 2, 3, 4, 5]
print(my_list)
print(type(my_list))

#list indexing - access elements
print(my_list[0])
print(my_list[1])
print(my_list[-1])

#list indexing - modify elements
my_list[0] = 10
print(my_list)

#list indexing - slicing
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numbers[2:5])   #[2, 3, 4]
print(numbers[:4])    #[0, 1, 2, 3] (from start to index 3)
print(numbers[5:])    #[5, 6, 7, 8, 9] (from index 5 to end)
print(numbers[:])     #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9] (entire list)
print(numbers[::2])   #[0, 2, 4, 6, 8] (every 2nd element)
print(numbers[1::3])  #[1, 4, 7] (start at index 1, every 3rd element)
print(numbers[-5:-2]) #[5, 6, 7] (negative indexing from end)

#list methods
nums = [5, 2, 9]

#len()
print(len(nums))        #3

#sum()

#min()

#max()

#.append(element)
nums.append(7)
print(nums)             #[5, 2, 9, 7]

#.extend(list)
nums.extend([3, 8])
print(nums)             #[5, 2, 9, 7, 3, 8]

#.remove(value)
nums.remove(3)
print(nums)             #[5, 2, 9, 7, 8]

#.pop(index)
#By default, pop() removes the last element from the list. We can also specify an index to remove a specific element, as shown below.
nums.pop(4)
print(nums)             #[5, 2, 9, 7]

#.insert(idx, element)
nums.insert(1, 4)
print(nums)             #[5, 4, 2, 9, 7]

#sort(), sorted()
sorted_nums = sorted(nums)
print(sorted_nums, nums)
nums.sort()
print(nums)             #[2, 4, 5, 7, 9]

#reverse(), reversed()
nums.reverse()
print(nums)             #[9, 7, 5, 4, 2]

#index()
#find the index of an 1st element in a list using the index() function, ValueError if no element is present
my_list = [1, 2, 3, 4, 5, 3]

print(my_list.index(3))  # Output: 2

#count()

#.clear
nums.clear()
print(nums)             #[]

#loops on list
#when you only need values
numbers = [10, 20, 30, 40 , 50]
for num in numbers:
    print(num)

#when index is required
for i in range(len(numbers)):
    print(i, numbers[i])

#when both idx, value is needed
for idx, val in enumerate(numbers):
    print(idx, val)

#linear search
numbers = [5, 12, 7, 3, 18, 9]
x = 18

for num in numbers:
    if num == x:
        print(num)
        
