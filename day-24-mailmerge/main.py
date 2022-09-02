#TODO: Create a letter using starting_letter.txt
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# with open("Input/Letters/starting_letter.txt") as file:
#     contents = file.readlines()
#
# with open("Input/Names/invited_names.txt") as file:
#     names = file.readlines()
#     # Remove the "\n"
#     for i in range(len(names)):
#         names[i] = names[i].strip()
#
# # Create a new list to store the replaced content.
# new_contents = []
#
# # Create a new list with the replaced names.
# for name in names:
#     new_contents.append(contents[0].replace("[name]", name))
#
# # Create the files in append mode and merge the list of replaced names content with the common content.
# for i in range(len(names)):
#     with open(f"Output/ReadyToSend/letter_for_{names[i]}.txt", mode="a") as completed_file:
#         file.write(new_contents[i])
#         for a in range(1, len(contents)):
#             file.write(contents[a])
    
# Below is a more simple solution which is to not use readlines for the content.

with open("Input/Letters/starting_letter.txt") as file:
    contents = file.read()

with open("Input/Names/invited_names.txt") as file:
    names = file.readlines()
    # Remove the "\n"
    for i in range(len(names)):
        names[i] = names[i].strip()

for name in names:
    new_content = contents.replace("[name]", name)
    with open(f"Output/ReadyToSend/letter_for_{name}.txt", mode="a") as completed_file:
        file.write(new_content)
