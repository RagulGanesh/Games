import random
d={1:"rock",2:"paper",3:"scissor"}
while True:
    user_choice=input("Enter rock/paper/scissor : ")
    computer_choice=random.randint(1,3)
    print("Computer Choice : ",d[computer_choice])
    if(user_choice==d[computer_choice]):
        print("Draw :(")
    elif(user_choice=="rock"):
        if(d[computer_choice]=="scissor"):
            print("User Win")
        elif(d[computer_choice]=="paper"):
            print("User Lose") 
    elif(user_choice=="paper"):
        if(d[computer_choice]=="rock"):
            print("User Win")
        elif(d[computer_choice]=="scissor"):
            print("User Lose")
    elif(user_choice=="scissor"):
        if(d[computer_choice]=="rock"):
            print("User Lose")
        elif(d[computer_choice]=="paper"):
            print("User win")
    elif(user_choice=="0"):
        break



