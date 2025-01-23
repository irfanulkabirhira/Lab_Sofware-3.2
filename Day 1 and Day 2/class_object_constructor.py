class User:
    def __init__(self, user_id , username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers +=1
        self.following +=1

user_1 = User("001", "Hira" )
user_2 = User("002", "Pira")

# Usr_1 is following to User_2
user_1.follow(user_2)

print(f"User_1 initially following was={user_1.followers} person")
print(f"User_1's Currently Following={user_1.following} Person")
print(f"After user_1 following to User_2 , the user_2's Current Followers={user_2.followers} person")
print(f"As in the User_2 doesn't follow anyone that's why user_2 following is={user_2.following} person")
