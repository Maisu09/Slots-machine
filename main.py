from user.UserClass import UserClass
from house_setup.ValueOfCards import ValueOfCards


def main():
    user1 = UserClass("Angela", 5)
    user1.view_user()

    user1.user_amount = 500
    user1.name = "Cristina"
    user1.view_user()

    print(ValueOfCards.EIGHT._name_)


if __name__ == '__main__':
    main()
