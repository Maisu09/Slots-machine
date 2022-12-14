class UserClass:

    def __init__(self, name, user_amount):
        self.__name = name
        self.__user_amount = user_amount

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def user_amount(self):
        return self.__user_amount

    @user_amount.setter
    def user_amount(self, user_amount):
        self.__user_amount = user_amount

    def view_user(self):
        print(
            "Name: " + self.__name + "\n" +
            "Money: " + str(self.__user_amount)
        )
