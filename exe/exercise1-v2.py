import pandas as pd
from treelib import Node, Tree

class Category:
    code = 1001
    def __init__(self,name,parent=None):
        self.name = name
        self.code = Category.code+10
        self.no_of_products = 0
        Category.code+=1
        self.parent = parent
        self.product = []
        self.display_name = self.name
        self.display_name1()

    def disp(self):
        print("Category : ", self.name,", Code:", self.code)
        print("Total no of product :->", self.no_of_products)
        print(self.display_name)
        if self.no_of_products != 0:
            print("All Products Name : ")
            for i in self.product:
                print(i.name)
        print()
    def display_name1(self):
        count = self
        while(count.parent!=None):
            self.display_name = f'{count.parent.name} > {self.display_name}'
            count=count.parent

class product:
    codepro = 0
    def __init__(self,name,Category,price,stock_at_location ={}):
        self.name = name
        self.code = product.codepro+1
        product.codepro+=1
        self.category = Category
        self.price = int(price)
        Category.no_of_products +=1
        Category.product.append(self)
        self.stock_at_location = stock_at_location
        #self.no_of_products=self.code+1
        #Category.no_of_products+=1
    def display(self):
        print("product :",self.name, "     code :",self.code, "     Category :", self.category.name, "     Price :",self.price)

def main():

    #Parent objects
    vehicle = Category("vehicle")
    device = Category("device")

    #child objects
    cars = Category("cars", vehicle)
    bike = Category("bike", vehicle)
    mobile = Category("mobile", device)
    laptop = Category("laptop", device)

    #child of child objects
    petrol = Category("petrol", cars)
    apple = Category("apple", mobile)
    samsung = Category("samsung", mobile)

    listofcategory = [vehicle, device , cars, bike, mobile, laptop, petrol, apple, samsung]


    prodct = [product("samsunga31", mobile, 17900),
              product("samsunga32", mobile, 21900),
              product("samsunga72", mobile, 28900),
              product("iphoneXR", mobile, 39900),
              product("iphone12mini", mobile, 48900),
              product("iphone13mini", mobile, 58900),
              product("iphone13pro", mobile, 98900),
              product("Macbook Air", laptop, 140000),
              product("Macbook", laptop, 89000),
              product("Activa5g", bike, 19990),
              product("Access", bike, 890000),
              product("Maruti celerio", cars, 693000),
              product("Tata tiago", cars, 700000),
              product("walkswagen Tiguan", cars, 3100000),
              product("hyundai Nexo", cars, 6500000),
              product("Creta", cars, 1500000),
              product("Maruti Ertiga", cars, 1100000),
              product("Tata altroz", cars, 1000000),
              product("Tata punch", cars, 900000),
              product("maruti Baleno", cars, 700000)]

    print("Category list : ")
    for x in listofcategory:
        x.disp()


    print ("list of product : ")
    for x in prodct:
        x.display()

    print("category and product in tree format")

    tree = Tree()

    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_column', 500)
    pd.set_option('display.width', 1000)

    tree.create_node("Product Category", 0)

    for i in listofcategory:
        tree.create_node(i.name, i.name, parent=0)
        if i.parent is not None:
            tree.move_node(i.name, i.parent.name)
        for c in i.product:
            tree.create_node(c.name, c.name, parent=i.name)
    tree.show()


'''    print("ascending based sorting : ")
    asort = (sorted(prodct, key=lambda asort: asort.price))
    for k in asort:
        k.display()

    print("descending based sorting :")
    desort = (sorted(prodct, key= lambda desort:desort.price, reverse=True))
    for k in desort:
        k.display()

    search = int(input("search based on product code :- "))
    y = [i for i in prodct if i.code == search]
    for i in y :
        i.display()
'''
if __name__=="__main__":
    main()