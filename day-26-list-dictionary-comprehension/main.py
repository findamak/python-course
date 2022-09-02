
# numbers = [1, 2, 3]
# new_list =[]
# for n in numbers:
#     y = n + 1
#     new_list.append(y)
# # with list comprehension, the above can be done with:
# new_list = [n + 1 for n in numbers]
# print(new_list)
#
# # List comprehension.
# name = "Allan"
# name_list = [letter for letter in name]
# print(name_list)
#
# # Range as list
# square_list = [n * 2 for n in range(1, 4)]
# print(square_list)
#
# # Conditional comprehension
# names = ['Alex', 'Beth', 'Caroline', 'Freddie']
# short_names = [name for name in names if len(name) < 5]
# print(short_names)
#
# # Create a dictionary using dictionary comprehension.
import random
names = ['Alex', 'Beth', 'Caroline', 'Freddie']
student_scores = {student:random.randint(1, 100) for student in names}
print(student_scores)
passed_students = {student:score for (student, score) in student_scores.items() if score >= 60}
print(passed_students)

# How to iterate over a Pandas Dataframe
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionary
# for (key, value) in student_dict.items():
#     print(value)

import pandas

# Create dataframe from dictionary
student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# Loop through a dataframe
# for (key, value) in student_data_frame.items():
#     print(value)

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
# Loop through rows of dataframe using iterrows. You then have access to the index and row data
for (index, row) in student_data_frame.iterrows():
    # print(index)
    # print(row)
    # print(row.score)
    if row.student == "Angela":
        print(row.score)
