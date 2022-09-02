# using "with" allows python to manage closing the file.
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

with open("my_file.txt", mode="a") as file:
    file.write("\nHello darling.")
