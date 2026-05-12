# for num in range(1,11):
#     if num % 2 == 0:
#         continue
#     elif num == 7:
#         break
#     else:
#         print(num)
#
#
# while True:
#     password=input("enter the password: ")
#     if password == "1234":
#         print("Welcome")
#         break
#     else:
#         print("Try again")

# list_of_products=[]
# while True:
#     product_name=input("enter a product name or 'done' to break: ")
#     if product_name == "done":
#         for product in list_of_products:
#             print(product)
#         break
#     list_of_products.append(product_name)


# for i in range(1,4):
#     for j in range(1,4):
#         if j == 2:
#             break
#         print(i,j)


# counter=0
# vowels=["A","a","E","e","I","i","O","o","U","u"]
# user_string=input("enter a string: ")
# for i in user_string:
#     if i in vowels:
#         counter+=1
# print(counter)


# for i in range(1,6):
#     for j in range(1,6):
#         result=i*j
#         print(f"{i} x {j} = {result}")


# user_string1=input("enter a string: ")
# reverse_string=""
# n=len(user_string1)-1
# for i in range(n,-1,-1):
#     reverse_string+=user_string1[i]
# print(reverse_string)


# positive_integer=int(input("enter a positive integer: "))
# counter1=0
# while positive_integer:
#     if positive_integer%2 == 0:
#         counter1+=1
#     positive_integer=positive_integer // 10
# print(counter1)


# string1=input("enter a string: ")
# new_string=""
# for i in string1:
#     i+=i
#     new_string+=i
# print(new_string)


# highest_number=0
# while True:
#     positive_integers=int(input("enter a positive number or '0' to stop: "))
#     if positive_integers == 0:
#         print(f"The highest number is: {highest_number}")
#         break
#     elif highest_number < positive_integers:
#         highest_number=positive_integers


# string2=input("enter a string: ")
# booli=True
# for i in string2:
#     if not "z" >= i >= "A" and not "0"<=i<="9":
#         booli=False
#         break
# print(booli)


# integer=int(input("enter a number: "))
# if integer >= 0:
#     list_of_reversed_numbers = []
#     multi = 1
#     while integer:
#         list_of_reversed_numbers.append(integer % 10)
#         integer=integer//10
#     while list_of_reversed_numbers:
#         integer+= list_of_reversed_numbers.pop() * multi
#         multi= multi * 10
#     print(integer)
# else:
#     print("Invalid")
