class Product:
    productNum = 0
    def __init__(self, name, description, price, stockQuantity):
        self.name = name
        self.description = description
        self.price = price
        self.stockQuantity = stockQuantity
        self.seller = None
        self.productID = Product.productNum
        Product.productNum += 1
    

    def printDetails(self):
        print(self.productID, " ", self.name, " - Php ", self.price, " | Stocks: ", self.stockQuantity, " |")
    
    def printDescription(self):
        print(self.name, ": ", self.description)

class Seller:
    numSeller = 0
    def __init__(self, name):
        self.name = name
        self.__password = None
        self.__SellerID = f"#S{Seller.numSeller}"
        self.products = []
        self.__profits = 0
        Seller.numSeller += 1

    def setPassword(self, password):
        self.__password = password
    
    def getPassword(self):
        return self.__password
    
    def getCredits(self):
        return self.__profits
    
    def getSellerID(self):
        return self.__SellerID
    
    def addProfit(self, val):
        self.__profits += val

    def AddProduct(self):
        productName = input("Product: ")
        productDescription = input("Description: ")
        productPrice = float(input("Price: "))
        productQuantity = int(input("Quantity: "))
        product = Product(productName, productDescription, productPrice, productQuantity)
        product.seller = self
        self.products.append(product)
    
    def printProducts(self):
        if len(self.products) == 0:
            print("No product")
        for i in self.products:
            i.printDetails()
            
    
    def removeProduct(self):
        self.printProducts()
        if len(self.products) == 0:
            return
        product = input("Remove: ")
        for i in range(0, len(self.products)):
            if product == self.products[i].name:
                self.products.remove(self.products[i])
    
    def setPrice(self):
        self.printProducts()
        if len(self.products) == 0:
            return
        product = input("Change price\nProduct Name: ")
        newPrice = float(input("New price: "))
        for i in range(0, len(self.products)):
            if product == self.products[i].name:
                self.products[i].price = newPrice
    
    def Deposit(self):
        money = float(input("Deposit amount: "))
        self.__profits = money

class Buyer:
    numBuyers = 0
    def __init__(self, name):
        self.name = name
        self.__password = None
        self.__BuyerID = f"#B{Buyer.numBuyers}"
        self.__credits = 0
        self.__cart = {}
        self.__transactions = []
        Buyer.numBuyers += 1
    
    def setPassword(self, password):
        self.__password = password
    
    def getPassword(self):
        return self.__password
    
    def getCredits(self):
        return self.__credits
    
    def addToCart(self, product):
        quant = int(input("Quantity: "))
        while product.stockQuantity < quant:
            print("Insufficient stocks.")
            quant = int(input("Quantity: "))
        self.__cart[product] = quant
    
    def removeFromCart(self):
        if len(self.__cart) == 0:
            print("Cart is empty.")
            return
        for i in self.__cart:
            print(i.name, " | Quantity: ", self.__cart[i])
        productName = input("Remove product: ")
        for i in self.__cart:
            if productName == i.name:
                self.__cart[i] = 0
    
    def emptyCart(self):
        self.__cart = []
    
    def printCart(self):
        if len(self.__cart) == 0:
            print("Cart is empty.")
            return
        for i in self.__cart:
            print(i.name, " - ", i.price, " | Quantity: ", self.__cart[i])
    
    def Deposit(self):
        money = float(input("Deposit amount: "))
        self.__credits += money
    
    def checkOut(self):
        total = 0
        for i in self.__cart:
            total += (i.price * self.__cart[i])
        
        if total > self.__credits:
            print("Insufficient credit.")
            return
        
        self.__credits -= total
        
        print("Successfully bought: ")
        self.printCart()
        print("Total: Php", total)

        for i in self.__cart:
            i.stockQuantity -= self.__cart[i]
            i.seller.addProfit(i.price * self.__cart[i])
            record = Transaction(i, self, self.__cart[i])
            self.__transactions.append(record)
            print(f"Bought {i.name}")
        self.emptyCart()
    
    def viewTransactions(self):
        if len(self.__transactions) == 0:
            print("No transaction records.")
        for i in self.__transactions:
            i.printTransactionDetails()

