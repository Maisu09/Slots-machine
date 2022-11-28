from user.UserClass import UserClass
from house_setup.ValueOfCards import ValueOfCards
from house_setup.options import OPTIONS

def view_option(user1:UserClass):
    #Display the user and the remained amount in the game.
    print(f"Username: {user1.name} , Amount: {user1.user_amount}")

def interaction():
    #Selecting the option for the user.
    for option in OPTIONS:
        print(f"{option.name} : {option.value}")

    selected_option = int(input("Select an option"))
    return selected_option

def game_logic(user_name, user_value):
    # The flow of the program. 
    user_return = interaction()



def creating_user(user_name:str, user_value:float):
    #Asking the user for it's credential and money. Creating the user.
    return UserClass(user_name, user_value)

def main():
    user_name = input("Insert player name: ")
    user_value = float(input("Insert money amount: "))
    user1 = creating_user(user_name, user_value)
    interaction()


if __name__ == '__main__':
    main()
