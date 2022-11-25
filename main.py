from user.user_class import user_class
from houseSetup.value_of_cards import value_of_cards


def main():
    user1 = user_class("Angela", 5)
    print(user1.name, user1.user_amount)
    
    user1.user_amount = 500
    user1.name = "Cristina"
    print(user1.name, user1.user_amount)

    print(value_of_cards.EIGHT._name_)

if __name__ == '__main__':
    main()