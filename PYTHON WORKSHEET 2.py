#PYTHON WORKSHEET 2
#SUBMITTED BY ARMAAN TAYAL (1024230087)

# Question 1: Manipulating lists
L = [10, 15, 13, 14, 11]

L.append(50)
L.append(60)
print("List after adding 50 and 60:", L)

L.sort()
print("List sorted in ascending order:", L)

L.sort(reverse=True)
print("List sorted in descending order:", L)

if 13 in L:
    print("13 is present in the list.")
else:
    print("13 is not present in the list.")

print("Number of elements in the list:", len(L))

S = sum(L)
print("Sum of all elements in the list:", S)

odd_total = 0
for value in L:
    if value % 2 != 0:
        odd_total += value
print("Sum of odd elements:", odd_total)

even_total = 0
for value in L:
    if value % 2 == 0:
        even_total += value
print("Sum of even elements:", even_total)

print("Largest element in the list:", max(L))

L.clear()
print("List after clearing all elements:", L)

# ---
# Question 2: Sum all elements in a list without using built-in function
list_a = [10, 20, 30, 40]
sum_val = 0
for item in list_a:
    sum_val += item
print("Sum of elements without using sum() function:", sum_val)

# ---
# Question 3: Multiply all elements in a list without using built-in function
list_b = [2, 3, 4, 5]
product_val = 1
for item in list_b:
    product_val *= item
print("Product of elements without using a built-in function:", product_val)

# ---
# Question 4: Create a 3*4*6 3D array
r = 3
c = 4
d = 6

array3d = []
for i in range(r):
    layer = []
    for j in range(c):
        row_list = []
        for k in range(d):
            row_list.append('*')
        layer.append(row_list)
    array3d.append(layer)

print("3D array generated successfully. Here's one slice of it:")
print(array3d[0])

# ---
# Question 5: Dictionary manipulation
my_dict = {1:5, 2:7, 3:6, 4:8, 5:7}

my_dict[8] = 8.8
print("Dictionary after adding new entry:", my_dict)

my_dict[9] = 9.9
print("Dictionary after adding another entry:", my_dict)

if 8 in my_dict:
    print("Key 8 is present in the dictionary.")
else:
    print("Key 8 is not present in the dictionary.")

if 7 in my_dict.values():
    print("Value 7 is present in the dictionary.")
else:
    print("Value 7 is not present in the dictionary.")

my_dict[3] = 7.1
print("Dictionary after updating value of key 3:", my_dict)

my_dict.clear()
print("Dictionary after clearing all elements:", my_dict)

# ---
# Question 6: Set manipulation
set_one = {10, 20, 30, 40, 50, 60}
set_two = {40, 50, 60, 70, 80, 90}

set_one.add(55)
set_one.add(66)
print("Set one after adding 55 and 66:", set_one)

set_one.remove(10)
set_one.remove(30)
print("Set one after removing 10 and 30:", set_one)

intersection_result = set_one.intersection(set_two)
print("Intersection of set one and set two:", intersection_result)

union_result = set_one.union(set_two)
print("Union of set one and set two:", union_result)

difference_result = set_one.difference(set_two)
print("Difference set one - set two:", difference_result)

# ---
# Question 7: Write the following program. (Text is cut off in image)
print("This is a placeholder for Question 7, which is not fully visible.")

# ---
# Question 8: Print 100 random strings
import random
import string

for _ in range(100):
    str_len = random.randint(6, 8)
    random_str = ''.join(random.choice(string.ascii_letters) for _ in range(str_len))
    print(random_str)

# ---
# Question 9: Check if a number is odd or even
number_to_check = int(input("Enter an integer: "))
is_even_flag = (number_to_check % 2 == 0)
if is_even_flag:
    print("The number", number_to_check, "is even.")
else:
    print("The number", number_to_check, "is odd.")

# ---
# Question 10: Find how many times substring "Emma" appears
text_string = "Emma is a good student. Emma likes to read. Emma studies hard."
count_val = text_string.count("Emma")
print("The substring 'Emma' appears", count_val, "times.")

# ---
# Question 11: Create a new list with only odd numbers
original_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = []
for num_val in original_numbers:
    if num_val % 2 != 0:
        odd_numbers.append(num_val)
print("Original list:", original_numbers)
print("New list with only odd numbers:", odd_numbers)

# ---
# Question 12: Robot's legal positions
robot_positions = [(2, 3), (6, 7), (7, 8)]
valid_positions = []
for coordinates in robot_positions:
    if coordinates[1] % 2 == 0:
        valid_positions.append(coordinates)
print("Positions with even y-coordinate:", valid_positions)

# ---
# Question 13: Robot's sensor readings
sensor_data_dict = {1: 2.3, 2: 4.5, 3: 1.8, 4: 3.6}
max_sensor_val = max(sensor_data_dict.values())
print("The maximum sensor value is:", max_sensor_val)

# ---
# Question 14: Robot's commands
all_cmds = ["MOVE", "TURN_LEFT", "TURN_RIGHT", "STOP", "DODGE", "JUMP"]
executed_cmds = ["MOVE", "TURN_LEFT", "STOP"]

all_cmds_set = set(all_cmds)
executed_cmds_set = set(executed_cmds)

not_executed_list = list(all_cmds_set.difference(executed_cmds_set))
print("Commands not executed:", not_executed_list)


