age=int(input("please enter the age: "))
if not 0<=age<=120:
    print("invalid")
elif 0<=age<=12:
    print("child")
elif 13<=age<=17:
    print("teen")
else:
    print("adult")


single_character=input("please enter a single character: ")
vowels={"a","A","e","E","i","I","o","O","u","U"}
if not "z">=single_character>="A":
    print("Invalid")
elif single_character in vowels:
    print("Vowel")
else:
    print("Consonant")


age=int(input("please enter your age: "))
if age < 16:
    print("your age is too low")
else:
    is_vip=input("have yoe VIP? (answer yes or nothing) ")
    if is_vip and age >= 18:
        print("allow entry")
    elif 19<=age<=21:
        print("allow entry")


the_correct_password="emas1234"
user_password=input("please enter the correct password: ")
if the_correct_password == user_password:
    print("Access Granted")
elif len(user_password) < 8:
    print("Too short")
else:
    print("Wrong password")


x=int(input("enter point x: "))
y=int(input("enter point y: "))
if 10<=x<=50 and 20<=y<=80:
    if x==10 or x==50 or y==20 or y==80:
        print("On the edge")
    else:
        print("Inside the rectangle")
else:
    print("Outside the rectangle")


user_name=input("please enter your name: ")
print(f"welcome {user_name or "Anonymous"}")


number1=int(input("enter a number: "))
number2=int(input("enter a number: "))
number3=int(input("enter a number: "))
print((number1>0)+(number2>0)+(number3>0))


score=int(input("enter a grade: "))
print("A" if 90<=score<=100 else "B" if 80<=score<90 else "C" if 70<=score<80 else "F")
