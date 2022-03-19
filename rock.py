from tkinter import *
from PIL import ImageTk, Image
import random
def display_pic1(a):
    if(a=="stone"):
        canvas1 = Canvas(root, width = 300, height = 300)  
        canvas1.place(x=80,y=90)  
        img1 = ImageTk.PhotoImage(Image.open("stone.jpg"))  
        canvas1.create_image(20, 20, anchor=NW, image=img1) 
    elif(a=="paper"):
        canvas1 = Canvas(root, width = 300, height = 300)  
        canvas1.place(x=80,y=90)  
        img1 = ImageTk.PhotoImage(Image.open("paper.jpg"))  
        canvas1.create_image(20, 20, anchor=NW, image=img1)
    else:
        canvas1 = Canvas(root, width = 300, height = 300)  
        canvas1.place(x=80,y=90)  
        img1 = ImageTk.PhotoImage(Image.open("scissor.jpg"))  
        canvas1.create_image(20, 20, anchor=NW, image=img1)  
def display_pic2(a):
    if(a=="stone"):
        canvas1 = Canvas(root, width = 300, height = 300)  
        canvas1.place(x=500,y=90)  
        img1 = ImageTk.PhotoImage(Image.open("stone.jpg"))  
        canvas1.create_image(20, 20, anchor=NW, image=img1) 
    elif(a=="paper"):
        canvas1 = Canvas(root, width = 300, height = 300)  
        canvas1.place(x=500,y=90)  
        img1 = ImageTk.PhotoImage(Image.open("paper.jpg"))  
        canvas1.create_image(20, 20, anchor=NW, image=img1)
    else:
        canvas1 = Canvas(root, width = 300, height = 300)  
        canvas1.place(x=500,y=90)  
        img1 = ImageTk.PhotoImage(Image.open("scissor.jpg"))  
        canvas1.create_image(20, 20, anchor=NW, image=img1)  

d={1:"rock",2:"paper",3:"scissor"}
root=Tk()
root.geometry('900x600')
root.resizable(0,0)
root.title("Rock Paper Scissor")    
title = Label(root, text="Rock Paper Scissor",width=20,font=("Comic Sans MS",20,"underline"),fg="red",)
title.place(x=250,y=45)
# canvas1 = Canvas(root, width = 300, height = 300)  
# canvas1.place(x=80,y=90)  
# img1 = ImageTk.PhotoImage(Image.open("paper.jpg"))  
# canvas1.create_image(20, 20, anchor=NW, image=img1) 
# canvas2 = Canvas(root, width = 300, height = 300)  
# canvas2.place(x=500,y=90)  
# img2 = ImageTk.PhotoImage(Image.open("stone.jpg"))  
# canvas2.create_image(20, 20, anchor=NW, image=img2) 
display_pic1("stone")

# while True:
#     user_choice=input("Enter rock/paper/scissor : ")
#     display_pic1(user_choice)
#     computer_choice=random.randint(1,3)
#     display_pic2(d[computer_choice])
#     print("Computer Choice : ",d[computer_choice])
#     if(user_choice==d[computer_choice]):
#         print("Draw :(")
#     elif(user_choice=="rock"):
#         if(d[computer_choice]=="scissor"):
#             print("User Win")
#         elif(d[computer_choice]=="paper"):
#             print("User Lose") 
#     elif(user_choice=="paper"):
#         if(d[computer_choice]=="rock"):
#             print("User Win")
#         elif(d[computer_choice]=="scissor"):
#             print("User Lose")
#     elif(user_choice=="scissor"):
#         if(d[computer_choice]=="rock"):
#             print("User Lose")
#         elif(d[computer_choice]=="paper"):
#             print("User win")
#     elif(user_choice=="0"):
#         break
root.mainloop()