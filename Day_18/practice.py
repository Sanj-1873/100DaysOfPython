#list comprehension --> new list from a previous list 

numbers = [1,2,3]
new_numbers = [n + 1 for n in numbers]


double_range = [n*2 for n in range(1,5)]
print(double_range)

# Conditional List Comprehension 

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]

short_names = [n for n in names if len(n) < 5]
print(short_names)

long_uppercase = [name.upper() for name in names if len(name) > 5]
print(long_uppercase)

# Squared numbers 
numbers = [1,1,2,3,5,8,13,21,34,55]

squared_numbers = [number * number for number in numbers]

print(squared_numbers)

#only even numbers 

numbers = [1,1,2,3,5,8,13,21,34,55]
result = [number for number in numbers if number %2 ==0]

print(result)
# Common to both files 

file1 = []
file2 = []

with open("file1.txt") as first:
    numbers = first.read()
    file1 = numbers.split('\n')

with open("file2.txt") as second:
    numbers = second.read()
    file2 = numbers .split('\n')

combined = [number for number in file1 if number in file2]
print(combined)


# Dictionary Comprehension 
# new_dict = {new_key:new_value for (key,value) in dict.items()}
import random
students_scores = { student:random.randint(1,100) for student in names}
print(students_scores)


passed_students = {student:score for (student, score) in students_scores.items() if score >= 60   }
print(passed_students)



sentence = "what is the Airspeed Veleocity of an Unladen Swallow?"

words = sentence.split(" ")
result = {word:len(word) for word in words}

print(result)


weather_c = {
    "Moday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day:temp_c*9/5 for (day, temp_c)in weather_c.items()}
print(weather_f)

