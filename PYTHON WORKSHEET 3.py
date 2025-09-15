#PYTHON WORKSHEET 3
#ARMAAN TAYAL (1024230087)
# Question 1:
def calculate_diff(num):
    if num > 17:
        return (num - 17) * 2
    else:
        return abs(num - 17)

print("For 22, the result is:", calculate_diff(22))
print("For 14, the result is:", calculate_diff(14))

# ---
# Question 2:
def check_range(num):
    return (num in range(100, 1001) or num in range(1000, 2001))

print("Is 150 in range?", check_range(150))
print("Is 1500 in range?", check_range(1500))
print("Is 50 in range?", check_range(50))

# ---
# Question 3:
def flip_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

original = "robut"
flipped = flip_string(original)
print("The reversed string is:", flipped)

# ---
# Question 4:
def count_cases(s):
    counts = {'upper': 0, 'lower': 0}
    for char in s:
        if 'a' <= char <= 'z':
            counts['lower'] += 1
        elif 'A' <= char <= 'Z':
            counts['upper'] += 1
    return counts['upper'], counts['lower']

text = "Hello World"
upper_case_count, lower_case_count = count_cases(text)
print("Original String:", text)
print("No. of uppercase characters:", upper_case_count)
print("No. of lowercase characters:", lower_case_count)

# ---
# Question 5:
def get_uniques(input_list):
    return list(set(input_list))

sample_list_1 = [1, 2, 3, 3, 4, 4, 5, 6, 6]
unique_items = get_uniques(sample_list_1)
print("Original list:", sample_list_1)
print("List with distinct elements:", unique_items)

# ---
# Question 6:
def filter_even(input_list):
    return [num for num in input_list if num % 2 == 0]

sample_list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_nums = filter_even(sample_list_2)
print("Original list:", sample_list_2)
print("Even numbers:", even_nums)

# ---
# Question 7:
def create_closure(x):
    def inner_add(y):
        return x + y
    return inner_add

add_five = create_closure(10)
result = add_five(5)
print("The result of the inner function is:", result)

# ---
# Question 8:
def show_args(*args):
    print("The arguments are:")
    for arg in args:
        print(arg)

show_args("Python", 2024, "Coding")

# ---
# Question 9:
def move_pos(x, y, direction):
    if direction == "up":
        y += 1
    elif direction == "down":
        y -= 1
    elif direction == "left":
        x -= 1
    elif direction == "right":
        x += 1
    return (x, y)

x_coord, y_coord = 0, 0
new_coords = move_pos(x_coord, y_coord, "up")
print("New position of the robot:", new_coords)

# ---
# Question 10:
def classify_temp(temp):
    if temp < 15:
        return "Moderate"
    elif temp <= 30:
        return "Hot"
    else:
        return "Very Hot"

print("Classifying 10:", classify_temp(10))
print("Classifying 25:", classify_temp(25))
print("Classifying 35:", classify_temp(35))

# ---
# Question 11:
def is_final_position_reached(path):
    x, y = 0, 0
    for move in path:
        if move == "up":
            y += 1
        elif move == "down":
            y -= 1
        elif move == "left":
            x -= 1
        elif move == "right":
            x += 1
    return x == 2 and y == 0

path_list = ["up", "up", "down", "down", "right", "right"]
print("Is the final position (2,0)?", is_final_position_reached(path_list))

# ---
# Question 12:
class Student_Data:
    def __init__(self, s_id, s_name):
        self.student_id = s_id
        self.student_name = s_name
        self.student_class = "Default Class"

    def show_info(self):
        print("Student ID:", self.student_id)
        print("Student Name:", self.student_name)
        print("Student Class:", self.student_class)

student_a = Student_Data(101, "Alice")
student_a.show_info()

# ---
# Question 13:
class Student_Info:
    def __init__(self, s_id, s_name):
        self.id_num = s_id
        self.full_name = s_name

student_one = Student_Info(101, "Bob")
student_two = Student_Info(102, "Charlie")

print("Attributes of student1:")
print("Student ID:", student_one.id_num)
print("Student Name:", student_one.full_name)

print("\nAttributes of student2:")
print("Student ID:", student_two.id_num)
print("Student Name:", student_two.full_name)

# ---
# Question 14:
import math

class CircleCalculations:
    def __init__(self, rad):
        self.radius = rad

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

my_circle = CircleCalculations(5)
print("Area of the circle:", my_circle.calculate_area())
print("Perimeter of the circle:", my_circle.calculate_perimeter())

# ---
# Question 15:
class StringProcessor:
    def __init__(self, text):
        self.data = text

    def get_data(self):
        return self.data

    def show_data(self):
        print("The string is:", self.data)

    def to_upper(self):
        return self.data.upper()

processor = StringProcessor("hello world")
print("Retrieved string:", processor.get_data())
processor.show_data()
print("Uppercase string:", processor.to_upper())

# ---
# Question 16:
class Robot_Status:
    def __init__(self, name, task, level):
        self.name = name
        self.task = task
        self.battery = level

    def perform_task(self):
        self.battery -= 10
        print("The robot is performing the task and the battery decreases by 10%.")
        return self.battery

    def recharge(self):
        self.battery = 100
        print("The robot is recharged and the battery is back to 100%.")
        return self.battery

    def get_status(self):
        print("Robot Name:", self.name)
        print("Current Task:", self.task)
        print("Battery:", self.battery)

robot = Robot_Status("Robot1", "Task1", 50)
robot.perform_task()
robot.recharge()
robot.get_status()





