#List basics

int_list = [1, 2, 3, 4, 5]
string_list = ["John", "Paul", "George", "Ringo"]
mixed_list = [0.87, "hello", True, 17]

print(int_list)
print(string_list)
print(mixed_list)

#populating a list1
my_list = [i for i in range(1, 51)]

print(my_list)

#populating a list2
my_list = [i for i in range(0, 50, 2)]

print(my_list)

#populating a list3
my_list = [i for i in range(50, 0, -1)]

print(my_list)

#list and its index
my_list = [5, 10, 15, 20]

print(my_list[0])

my_list = [5, 10, 15, 20]

print(my_list[3])

#modifying
my_list[1, 2, 3, 4]
my_list[1]=7

#list concatenation
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]

print(list_1 + list_2)

#the In boolean operator in lists
my_list = ["red", "orange", "yellow", "green"]

print("red" in my_list)

#list length
list_1 = [12, 66, 52, 97, 28, 41, 7]
list_2 = [68, True, 34, False, 41.897, "apple"]

if len(list_1) > len(list_2):
    print("list_1 is longer than list_2")
elif len(list_1) == len(list_2):
    print("list_1 and list_2 are the same length")
else:
    print("list_2 is longer than list_1")

#the slice operator
my_list = ["red", "orange", "yellow", "green"]
my_slice = my_list[0:2]

print(my_slice)

my_list = ["red", "orange", "yellow", "green"]
my_slice = my_list[0:len(my_list)]

print(my_slice)

#append method
my_list = [1, 2, 3]
new_element = 4

my_list.append(new_element)
print(my_list)

my_list = [1, 2, 3]
new_element = my_list[0]

my_list.append(new_element)
print(my_list)

my_list = [1, 2, 3]
new_element = len(my_list)

my_list.append(new_element)
print(my_list)

#pop method removes and returns the last element in a list

my_list = [1, 2, 3, 4]
print(my_list)
print(my_list.pop())
print(my_list)

my_list = [1, 2, 3, 4]
for i in range(4):
    print(my_list)
    my_list.pop()

#insert
my_list = [1, 2, 3, 4]
my_list.insert(2, "Hi")
print(my_list)

#remove - removes an element in a list based on a value
my_list = [1, 2, 3, 3, 4]
my_list.remove(2)
print(my_list)

#remove vs. pop - this code does the same thing - prints 1234
list_1 = [1, 2, 3, 4, 5]
list_1.pop()
print(list_1)

list_2 = [1, 2, 3, 4, 5]
list_2.remove(5)
print(list_2)

#count - the count method will count how many times an element appears in a list
my_var = 2
my_list = [2, "red", 2.00000001, my_var, "Red", 8 // 4]
print(my_list.count("red"))

#index
my_list = ["dog", True, 16, "house", 55.9, False, 16]
index = my_list.index("house")
print(index)

#the sort method
my_list = [23, 55, 11, 7, 82.9, -14, 0, 34]
print(my_list)
my_list.sort()
print(my_list)

my_list = ["zebra", "door", "apple", "cat", "deer", "bark"]
print(my_list)
my_list.sort()
print(my_list)

my_list = ["APPLE", "apple", "Apple"]
print(my_list)
my_list.sort()
print(my_list)

#reverse sort
my_list = [23, 55, 11, 7, 82.9, -14, 0, 34]
my_list.sort()
print(my_list)
my_list.sort(reverse=True)
print(my_list)

#reverse method - does not have a parameter and modifies the original list
my_list = ["north", True, 45, 12, "red"]
print(my_list)
my_list.reverse()
print(my_list)

#sum function for a list of numbers
my_list = [1, 2, 3, 4, 5]
total = sum(my_list)
print(total)

my_list = [5, 17, 2, 3, 3]
total = sum(my_list)
num_elements = len(my_list)
avg = total / num_elements
print(avg)

#min function
my_list = [45, 12, 9, 1]
smallest = min(my_list)
print(smallest)

#the min function works with strings - python selects the first that comes alphabetically
my_list = ["apple", "boy", "cat", "aaron"]
smallest = min(my_list)
print(smallest)

#max 
my_list = [50, 11, 0, 72, 102]
largest = max(my_list)
print(largest)

my_list = ["house", "cat", "zebra", "dog", "bike"]
last = max(my_list)
print(last)

#list iteration - numbers
numbers = [1, 2, 3, 4]
for number in numbers:
    print(number)

numbers = ["cat", "dog", "mouse", "bird"]
for number in numbers:
    print(number)

colors = ["red", "green", "blue", "yellow", "black"]
for color in colors:
    print(color)

#iteration with while loops
numbers = [1, 2, 3, 4]
length = len(numbers)
i = 0

while i < length:
    print(numbers[i])
    i += 1

length = len(colors)
i = 0

while i < length:
    print(colors[i])
    i += 1

