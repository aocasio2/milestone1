import mod1
mod1.get_user_name()




def FinalChapterIntr(name):
    print(f"{name}! Intro \n previously after finding yourself outmatched a villager helped you in your time of need. you contemplate what to do")
    print(f" {name}! Scene  \n After some days in the village you figure that you have a decision to make to stay or to go ")

def yourDecision():
    user_name = get_user_name()
    introduction2(user_name)

    print(f" {name}! This is your decision stay at the village or move on ")
    print("1. Stay at the village") # here is a secret ending
    print("2. Continue your travels") # story continues on a bit more

    user_choice = input("Type 1 for choice 1 or type 2 for choice 2: ")

    if user_choice == '1':
        print("You have decided to stay at the village that saved you")
        print("You decide to live your life at the village")
    elif user_choice == '2':
        print("You decide to leave the village and say your goodbyes to those who helped you")
        print("Now where do you go. you rethink what happened to you")
        print(" you find your self wandering until night that is ")
        print(" the night sky is beautiful ")
        print(" there is something about walking aimlessly at night , yet with every step you walk with purpose")
        print("You know deep down that you cant let this go. the adventure keeps you alive")
        # Decision time one last time


        print(f" {name}! Make the call ")
        print("1. Stay at the village")


        user_choice = input("Type 1 for choice 1")

        if user_choice == '1':
            print("True ending \nThe man who I am")
