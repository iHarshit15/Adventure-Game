# input from user that the game will use to address the user
name = input("what's your name?: ")
print("Hello " + name + " Welcome to the adventure!")

answer = input("You have two option where do you want to go mountains or beaches? (mountain/beach): ").lower()
if answer == "mountain":
    answer = input("You're on mountain so now you want to climb or camp? (climb/camp): ").lower()
    if answer == "climb":
        print("You climbed at the top of mountain but you ran out of oxygen and you lost!")
    elif answer == "camp":
        answer = input("You did camping and you met a stranger. Do you talk to them? (yes/no): ").lower()
        if answer == "yes":
            print("Nice you become friends and you win, Yayyy!!")
        elif answer == "no":
            print("It felt so rude so they killed you and you lost!!")
        else:
            print("Not a valid option!")
    else:
        print("Not a valid option")

elif answer == "beach":
    answer = input("You're on beach so now you want to swim or party? (swim/party): ").lower()
    if answer == "swim":
        print("You are under water and a shark attacks on you and you lost!!")
    elif answer == "party":
        answer = input("you are partying and met some people, Do you talk to them? (yes/no): ").lower()
        if answer == "yes":
            print("Nice you become friends and you win, Yayyy!!")
        elif answer == "no":
            print("It felt so rude so they killed you and you lost!!")
        else:
            print("Not a valid option")

    else:
        print("Not a valid option")
else:
    print("Not a valid option!")
