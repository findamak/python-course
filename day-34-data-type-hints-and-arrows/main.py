# Declare data type for variable
# age: int
# name: str
# height: float
# is_human: bool

# Here we declare that the age input must be an int and the function must return a bool. This is called type hints.
def police_check(age: int) -> bool:
    if age >= 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive
