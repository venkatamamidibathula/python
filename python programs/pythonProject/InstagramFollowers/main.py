class User:
    def __init__(self,id,name):
        self.id=id
        self.name=name
        self.followers=0
        self.following=0
    def followuser(self,user):
        self.following=1
        user.followers=1

user1=User("001","Mahesh")
user2=User("002","Sarat")
user1.followuser(user2)
print(user1.following)
print(user1.followers)
print(user2.following)
print(user2.followers)