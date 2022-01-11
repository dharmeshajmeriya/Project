
from exercise1_v3 import product,Category
import re

from past.builtins import raw_input

remail = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
rphone = r"(0|91)?[7-9][0-9]{9}"


def check(email):
    if (re.fullmatch(remail, email)):
        print(email)
    else:
        print("Enter valid Email")


def check(phone):
    if (re.fullmatch(rphone, phone)):
        print(phone)
    else:
        print("Enter valid phone number")

class Customer:
    def __init__(self):
        name = input("enter your name : ")
        email = input("enter valid email : ")
        check(email)
        phone = int(input("Enter phone number : "))
        check(phone)
        street = input("Enter your street : ")
        city = input("Enter city name : ")
        state = input("Enter your state : ")
        country = input("Enter country name : ")
        compnay = input("Enter company name : ")

        if type == 'company' or type == 'billing' or type == 'shipping' or type == 'contact':
            self.type = type
        else:
            print("Invalid Type!")

        print("your name is : ", name," email is : ", email, " phone number is : ", phone, "\n street name is : ", street, "city name is : ", city, "state name is : ", state, "\n country name is : ", country)

class order:
    def __init__(self,number, date, company, billing, shipping, total_amount, order_lines):
        self.number = number
        self.date = date
        self.company = company
        self.billing = billing
        self.shipping = shipping
        self.total_amount = total_amount
        self.order_lines = order_lines


if __name__ == '__main__':
    #objects of category :
    mobiles = Category("mobiles")
    laptop = Category("laptop")
    stationary = Category("stationary")

    #ojbects of products :
    samsung = product("samsung S21 FE", mobiles, 49990)
    apple = product("iphone 13", mobiles, 59900)
    lenovo = product("ideapad530s", laptop,49900)
    bag = product("laptop bag",stationary,990)

    #objects of customer
    john = Customer("john", "john@gmail.com","7890223909","Kalawad road","rajkot","gujarat","india","","company")

