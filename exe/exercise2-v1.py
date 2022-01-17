from datetime import datetime
from exercise1_v3 import product,Category
import re
from validation import Validator
validate = Validator()

import pandas as pd

from past.builtins import raw_input

class Customer:
    def __init__(self, name, email, phone, street, city, state, country, company, type):
        self.name = validate.name(name)
        self.email = validate.mail(email)
        self.phone = validate.phono(phone)
        self.street = validate.name(street)
        self.city = validate.name(city)
        self.state = validate.name(state)
        self.country = validate.name(country)
        self.company = company

        if type == 'company' or type == 'billing' or type == 'shipping' or type == 'contact':
            self.type = type
        else:
            print("Invalid Type!")

    def display(self):
        print("name : ", self.name)
        print("email : ", self.email)
        print("phone : ", self.phone)
        print(f"Address :{self.street}, {self.city}, {self.state},{self.country}")
        print("type : ", self.type)


class Order:
    order_number = 1201

    def __init__(self, date, company, billing, shipping):
        self.number = f"{Order.order_number}"
        Order.order_number += 1
        self.date = date
        self.company = company
        if billing.type == 'billing' and shipping.type == 'shipping':
            self.billing = billing
            self.shipping = shipping
        else:
            print("wrong information")
        self.order_lines = []
        self.total_amount = 0

    def totalamount(self):
        for i in self.order_lines:
            self.total_amount = self.total_amount + i.subtotal
        return self.total_amount

    def display(self):
        print("\nOrder Number: ", self.number)
        print("Date: ", self.date)
        print("Company: ", self.company.name)
        print()
        print("Billing information")
        print("------------------------------")
        self.billing.display()
        print()
        print("Shipping information: ")
        print("------------------------------")
        self.shipping.display()
        print()
        print("Order List:")
        print("------------------------------")
        temp = pd.DataFrame(i.__dict__ for i in self.order_lines)
        temp['order'] = temp['order'].apply(lambda x: x.number)
        temp['product'] = temp['product'].apply(lambda x: x.name)
        print(temp)
        print("Total amount: ", self.totalamount())


class OrderLine:
    def __init__(self,order,product,quantity,selling_price):
        self.order = order
        self.order.order_lines.append(self)
        self.product = product
        self.quantity = int(quantity)
        self.mrp = product.price
        self.selling_price = float(selling_price)
        self.subtotal = (self.quantity * self.selling_price)

    def display(self):
        print("product : ", self.product.name)
        print("quantity : ", self.quantity)
        print("mrp : ", self.mrp)
        print("selling price : ", self.selling_price)
        print("subtotal : ", self.subtotal)

if __name__ == '__main__':
    #objects of category :
    device = Category("device")
    laptop = Category("laptop")
    stationary = Category("stationary")

    #ojbects of products :
    AC = product("Air conditioner", device, 26990)
    fridge = product("side by side refridgerator", device, 55900)
    laptop = product("laptop", device,49900)
    bag = product("laptop bag",stationary,950)

    #objects of customer

    samsung = Customer("Samsung", "samsungcare@gmail.com", "8000090000", "kalawad road", "rajkot", "gujarat", "india", "", "company")

    lenovo = Customer("lenovo", "lenovocare@gmail.com", "9800994059", "mahila college chawk", "rajkot", "gujarat", "india", "", "company")

    jack = Customer("Jack", "jack@gmail.com", "9903020302", "yagnik road", "rajkot", "gujarat", "india", "", "billing")

    jo = Customer("jo", "jo12@gmail.com", "8000099909", "university road", "rajkot", "gujarat", "india", "", "shipping")

    #order and orderline objects

    order1 = Order('20 feb 2022', samsung, jack, jo)
    order1_line1 = OrderLine(order1, AC, 1, 25999)
    order1_line2 = OrderLine(order1, fridge, 1, 54490)

    order2 = Order('22 jan 2022', lenovo, jack, jo)
    order2_line1 = OrderLine(order2, laptop, 1, laptop.price)

    order3 = Order('30 jan 2022', lenovo, jack, jo)
    order3_line1 = OrderLine(order3, bag, 2, bag.price)


    listofallproduct = [AC,fridge,laptop,bag]
    #lists of all orders
    orders_list = [order1, order2, order3]
    #sorting orders by date
    sorted_list = list(sorted(orders_list, key=lambda item: datetime.strptime(item.date, "%d %b %Y")))

    #displaying sorted orders
    count = 1
    for i in sorted_list:
        print("\n")
        print(f"[Order {count}]")
        count += 1
        i.display()

    #filter current month order :-
    print("----------------------------------------------------------------------------------------------------")
    user = input("do you want to print current month order - write yes or no : ")

    if user == 'yes':
        print()
        print("order of current month")
        count = 1
        for i in orders_list:
            date_obj = datetime.strptime(i.date, '%d %b %Y')
            if date_obj.month == datetime.today().month:
                print("\n")
                print("------------------------")
                print(f"|Order {count} |")
                print("------------------------")
                count += 1
                i.display()
    elif user == 'no':
        pass
    else:
        print("Invalid input!!")

    #search order from it's number :
    search_no = input("search products with order number : ")
    flag = 0
    for i in orders_list:
        if i.number == search_no:
            i.display()
            flag = 1
    if flag == 0:
        print("No order found!")

    #search order with it's name :
    user = input("Do you want to search prodcut with it's name - yes or no : ")
    if user == "yes":
        product_name = input("Enter product name do you want to search : ")
        flg = 0
        for i in listofallproduct:
            if i.name == product_name:
                flg = 2
                for o in orders_list:
                    for u in o.order_lines:
                        if u.product == i:
                            print("order number : ", o.number)
                            u.display()
                            flg = 1
        if flag == 2:
            print()
            print(f"No orders for {product_name}!!")
        elif flag == 0:
            print()
            print("No such product!!")