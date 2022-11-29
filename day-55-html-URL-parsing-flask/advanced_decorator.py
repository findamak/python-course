class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

# Create the decorator that calls the create_blog_post function only if is_logged_in is "True"
def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper

@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s blog post.")

new_user = User("allan")
new_user.is_logged_in = True
create_blog_post(new_user)