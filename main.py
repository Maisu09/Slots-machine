from user.UserClass import UserClass
from house_setup.ValueOfCards import ValueOfCards


def main():
    user1 = UserClass("Angela", 5)
    print(user1.name, user1.user_amount)
    
    user1.user_amount = 500
    user1.name = "Cristina"
    print(user1.name, user1.user_amount)

    print(ValueOfCards.EIGHT._name_)

if __name__ == '__main__':
    main()