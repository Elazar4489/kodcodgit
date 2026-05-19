

# 1

def return_list_of_active_names(general_list_of_people):
    list_of_active_names = []
    for each in general_list_of_people:
        if each[1] >= 18 and each[2] == "active":
            list_of_active_names.append(each[0])
    return list_of_active_names

general_list = [["Dan", 25, "active"],
                ["Noa", 16, "active"],
                ["Yael", 30, "inactive"]]

# print(return_list_of_active_names(general_list))

def check_if_user_email_exist(user_email):
    if not user_email:
        print("Invalid user")
        return True
    return None

def check_quantity(quantity,stock):
    if quantity <= 0 or quantity > stock:
        print("Invalid quantity")
        return True
    return None

def return_price(product_price,quantity):
    price=product_price * quantity
    if quantity >= 10:
        price *= 0.9
    if quantity >= 50:
        price *= 0.85
    return price

def print_order(email,name,quantity,price):
    print(f"Order confirmed: {email} bought {quantity}x{name} for ${price}")
    return email, name, quantity, price, "confirmed"

def handle_purchase(user_email, product_name, product_price, stock, quantity):

    if check_if_user_email_exist(user_email):
        return None

    if check_quantity(quantity,stock):
        return None

    price = return_price(product_price,quantity)
    stock -= quantity
    return print_order(user_email,product_name,quantity,price)


    # list1=[v for v in dict1.values()]
    # most=0
    # the_value=None
    # for item in list1:
    #     if list1.count(item)>most:
    #         most=list1.count(item)
    #         the_value=item
    return the_value
