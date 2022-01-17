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



class location():
    codeoflocation = 300000
    def __init__(self,name):
        self.name = name
        self.code = location.codeoflocation + 1
        location.codeoflocation += 1

    def display1(self):
        print("Location is: ", self.name, "         ", "Code of location is: ", self.code)

class movement():
    def __init__(self, from_location, to_location, product, quantity):
        self.from_location = from_location
        self.to_location = to_location
        self.product = product
        self.quantity = quantity
        self.display = ''
        try:
            if self.product.stock_at_location[self.from_location] >= self.quantity:  #for checking
                qun = self.product.stock_at_location[self.from_location] - self.quantity  #decreasing value from starting location
                self.product.stock_at_location.update({self.from_location: qun})  #update
                if self.to_location in self.product.stock_at_location:  #increasing with value which move from the from location
                    qun1 = self.product.stock_at_location[self.to_location] + self.quantity
                    self.product.stock_at_location.update({self.to_location: qun1})  #update to location(end location after movement)
                    # print(self.product.name,"stock added")
                else:
                    # if not available location it adds both location and quantity
                    self.product.stock_at_location.update({self.to_location: self.quantity})
                # print(self.product.name,"done movement")
                self.display = f'product quantity :{self.quantity} from {self.from_location.name} to {self.to_location.name}'

            else:
                print(f"quantity no: {self.quantity} of {self.product.name} not available {self.from_location.name}")
        except Exception:
            print("no location for that product\n")
            # print("no stock available")

    @staticmethod
    def movements_by_product(product):
        flag = 0
        for item in movement1:
            if item.product.name == product.name:
                flag = 1
                print(item.display)

        if flag == 0:
            print("No movements yet.....")

if __name__ == "__main__":
    rajkot = location("Rajkot")
    ahmedabad = location("Ahmedabad")
    mumbai = location("Mumbai")
    pune = location("Pune")
    delhi = location("Delhi")
    listoflocation = [rajkot, ahmedabad, mumbai, pune]

    for i in listoflocation:
        i.display1()
        Mobile = Category("Mobile")

    prodct = [product("samsung", Mobile, 1790000, {rajkot:500, ahmedabad:700, delhi:1000}),
              product("apple", Mobile, 2190000, {rajkot:2000, mumbai:2200, pune:800}),
              product("blackberry", Mobile, 2890000, {rajkot:800, pune: 1200, delhi: 1100}),
              product("sony", Mobile, 3990000, {mumbai:900, delhi:1200}),
              product("nokia", Mobile, 4890000, {ahmedabad:870, rajkot:930, mumbai:670, delhi: 560})]

    print(" \nlist of all products : ")
    for x in prodct:
        print(x.name) #print name of product
        for key in x.stock_at_location:
            print(f'{key.name} - {x.stock_at_location[key]}')
        print()

    movement1 = [movement(rajkot, pune, prodct[0], 200),
                 movement(pune, rajkot, prodct[1], 300),
                 movement(delhi, ahmedabad, prodct[2], 800),
                 movement(delhi, rajkot, prodct[3], 870),
                 movement(rajkot, delhi, prodct[4], 670)]

    print ("which products are movements from one city to another city : ")
    for i in prodct:
        print(i.name)  # product name
        movement.movements_by_product(i)  # movement of product
        print()
    print("\n")

    print("************************************************************************************************")

    print("updated stock details : ")
    for i in prodct:
        i.display()
        print('Location: ', end='')
        for key in i.stock_at_location:
            print(f'{key.name} - {i.stock_at_location[key]}', end='  ')
        print('\n')
    print()
    print("***********************************************************************************")

    print("Updated location wise product stock")
    for i in listoflocation:
        print(i.name)
        for p in prodct:
            if i in p.stock_at_location:
                print(f'{p.name}- {p.stock_at_location[i]}')
        print()
    '''
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


    print("ascending based sorting : ")
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
