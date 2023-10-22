List_options = int(input(" Please choose your option from the list below: \n(1) Learn Python \n(2) Learn Java \n(3) Go swimming \n(4) Have dinner \n(5) Go to bed \n(0) Exit \n>>"))

if List_options == 1:
    print("You picked: Learn Python")
elif List_options == 2:
    print("You picked Java")
elif List_options == 3:
    print("You picked swimming ")
elif List_options == 4:
    print("You picked Have dinner")
elif List_options == 5:
    print("You picked Go to bed")
elif List_options == 0:
    print("You picked exit")
else:
    print("Not valid")
