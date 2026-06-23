import random as rd
import string as st

print("1= calculator \n2= no guessing game \n3= rock paper scissor game \n4 = random password generator")
prog=int(input())
if prog ==1:
    print("x,func,y respectively,press enter before each input ")
    x,func,y=int(input()),input(),int(input())
    if func == "+":
        print(x,"+",y ,"=" ,x+y)
    elif func == "-":
        print(x,"+",y ,"=" ,x-y)
    elif func == "/":
        print(x,"/",y,"=",x/y)
    elif func == "*":
        print(x,"*",y,"=",x*y)
    elif func == "**":
        print(x,"**",y,"=",x**y)
    else :
        print("function not available ")
elif prog ==2:
    print("welcome to no guessing hame ")
    x=rd.randrange(1,10)
    y=11
    while x!=y:
        y=int(input("guess the no : "))
        if x!=y:
            if x > y:
                print("your no is smaller ")
            else :
                print("your no is bigger ")
        else:
            print("congratulations you won \nthe no is " ,x)
elif prog ==3:
    print("welcome To Rock Paper Scissor game ")
    computer=[ "Rock ","paper ","Scissor " ]
    x=rd.choice(computer)
    print("1. rock\n2. paper\n3. scissors ")
    y=input("input your choice")
    if x=="Rock ":
        if y=="paper":
            print("you won the game")
            z=1
        elif y=="scissor":
                print("you lose the game")
        elif y=="rock":
            print("it's a tie ")
        else :
            print("wrong input ")
    elif x=="Paper ":
        if y=="scissor":
            print("you won the game")
            z=1
        elif y=="rock":
            print("you lose the game")
        elif y=="paper":
            print("it's a tie ")
        else :
            print("wrong input ")
    else:
        if y=="rock":
            print("you won the game")
            z=1
        elif y=="paper":
            print("you lose the game")
        elif y=="scissor":
            print("it's a tie ")
        else :
            print("wrong input ")
elif prog ==4:
    x=int(input("enter the length of the password to be generated : "))
    if x<6:
        print("password should be of at least 6 charactes")
    else :
        characters=st.ascii_letters + st.digits + st.punctuation
        password=""
        for i in range(x+1):
            password+=rd.choice(characters)
        print("your password is : " , password)
else:
    print("wrong input ")














