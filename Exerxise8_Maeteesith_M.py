username = input("Username :")
password = input("Password :")
if username == "Benz" and password == "111":
    print("Login Success")
    print("======= Welcome to Shop4Real =======")
    print("Please Choose Product")
    iphone = 25000
    mac = 55000
    ap = 6500
    print("Iphone11           25000 THB")
    print("MacBook            55000 THB")
    print("AirPods            6500  THB")
    select = input("Please Choose Product : ")
    if select == "iphone11":
        qty = int(input("Please Enter qty :"))
        total = iphone * qty
        print("Product : iphone11")
        print("Qty :", qty)
        print("Total Price:", total)
    elif select == "macbook":
        qty = int(input("Please Enter qty :"))
        total = mac * qty
        print("Product : MacBook")
        print("Qty :", qty)
        print("Total Price:", total)
    elif select == "airpods":
        qty = int(input("Please Enter qty :"))
        total = ap * qty
        print("Product : MacBook")
        print("Qty :", qty)
        print("Total Price:", total)
    else:
        print("โปรดทำรายการอีกครั้ง")
else:
    print("Login Failed")