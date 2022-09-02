# This block will test the excepted error to occur
try:
    file = open("file.txt")
    dict = {"key": "value"}
    print(dict["blah"])

# Catch file not found error and create file
except FileNotFoundError:
    file = open("file.txt", "w")
    file.write("something")

# Catch key error and print error message
except KeyError as error_msg:
    print(f"Key {error_msg} does not exist")

# If everything in the try block succeeds, then execute else block
else:
    content = file.read()
    print(content)

# The finally code block gets executed no matter what happens
finally:
    file.close()
    print("File closed")
    # Raise can be used to raise your own errors
    #raise TypeError("Made up error")

#BMI Example of raising errors

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)