class Category:
    code = 1001
    def __init__(self,name):
        self.name = name
        self.code = Category.code+10
        self.no_of_products = 0
        Category.code+=1
    def disp(self):
        print("Category : ",self.name,",Main Code:",self.code)
        print("Total no of product :->",self.no_of_products)

class product:
    codepro = 0
    def __init__(self,name,Category,price):
        self.name = name
        self.code = product.codepro+1
        product.codepro+=1
        self.category = Category.name
        self.price = int(price)
        self.no_of_products=self.code+1
        Category.no_of_products+=1
    def display(self):
        print("product :",self.name,"     code :",self.code,"     Category :", self.category,"     Price :", self.price)

apple = Category("apple")
samsung = Category("samsung")
oppo = Category("oppo")

try:
    prodct = [product("a31",samsung,17900),
              product("a32",samsung,21900),
              product("a72",samsung,28900),
              product("XR",apple,39900),
              product("12mini",apple,48900),
              product("13mini",apple,58900),
              product("13pro",apple,98900),
              product("a02",oppo,8900),
              product("f17",oppo,17900),
              product("f19",oppo,19990)]
    for i in prodct:
        i.display()
    apple.disp()
    samsung.disp()
    oppo.disp()

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


except Exception as e:
    print(e)