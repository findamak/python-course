class User:
    def __init__(self, userid, username):
        self.id = userid
        self.username = username
        #set attributes that all users will have when created
        self.followers = 0
        self.following = 0

    #create a method that allows a user to follow someone else
    def follow(self, user_in):
        user_in.followers += 1
        self.following += 1

user_1 = User("001", "Allan")
user_2 = User("002", "Syenie")

print(user_1.id)
print(user_1.username)

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
