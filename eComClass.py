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
        self.__transactions = []
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
    
    def viewTransactions(self):
        if len(self.__transactions) == 0:
            print("No transaction records.")
        for i in self.__transactions:
            i.printTransactionDetails()
    
    def addTransaction(self, tr):
        self.__transactions.append(tr)
        

    def AddProduct(self):
        productName = input("Product: ")
        productDescription = input("Description: ")
        productPrice = float(input("Price: "))
        productQuantity = int(input("Quantity: "))
        product = Product(productName, productDescription, productPrice, productQuantity)
        product.seller = self
        self.products.append(product)
    
    def addStocks(self):
        self.printProducts()
        if len(self.products) == 0:
            return
        try:    
            product = int(input("Change price\nProduct ID: "))
            for i in range(0, len(self.products)):
                if product == self.products[i].productID:
                    addedStock = float(input("Add stocks: "))
                    self.products[i].stockQuantity += addedStock
                    return
                
            addedStock += True
        except:
            print("Invalid product ID.")
    
    def printProducts(self):
        if len(self.products) == 0:
            print("No product")
        for i in self.products:
            i.printDetails()
            
    
    def removeProduct(self):
        self.printProducts()
        if len(self.products) == 0:
            return
        try:    
            product = int(input("Product ID: "))
            for i in range(0, len(self.products)):
                if product == self.products[i].productID:
                    self.products.remove(self.products[i])
                    return
            newPrice += True
        except:
            print("Invalid product ID.")

    
    def setPrice(self):
        self.printProducts()
        if len(self.products) == 0:
            return
        try:    
            product = int(input("Change price\nProduct ID: "))
            for i in range(0, len(self.products)):
                if product == self.products[i].productID:
                    newPrice = float(input("New price: "))
                    self.products[i].price = newPrice
                    return
            newPrice += True
        except:
            print("Invalid product ID.")
        
    def Deposit(self):
        money = float(input("Deposit amount: "))
        self.addProfit(money)

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
            i.seller.addTransaction(record)
            print(f"Bought {i.name}")
        self.emptyCart()
    
    def viewTransactions(self):
        if len(self.__transactions) == 0:
            print("No transaction records.")
        for i in self.__transactions:
            i.printTransactionDetails()

class Transaction:
    TransactionNum = 0
    def __init__(self, product, buyer, productQuantity):
        self.TransactionID = Transaction.TransactionNum
        self.product = product
        self.buyer = buyer
        self.productQuantity = productQuantity
        Transaction.TransactionNum += 1
    
    def printTransactionDetails(self):
        print(self.TransactionID, " | ", self.product.name, " | Quantity: ", self.productQuantity, " | ", "S: ", self.product.seller.name, "| B: ", self.buyer.name, " |")

class Shop:
    def __init__(self):
        self.buyers = []
        self.sellers = []
        self.products = []
        self.currentAccount = None


    def checkStocks(self):
        for i in self.sellers:
            for j in i.products:
                if j.stockQuantity == 0:
                    i.products.remove(j)

    def viewProducts(self):
        for i in self.sellers:
            for j in i.products:
                j.printDetails()


    def updateProducts(self):
        for i in self.sellers:
            for j in i.products:
                self.products = list(self.products)
                self.products.append(j)
                self.products = set(self.products)
        self.checkStocks()

    def createBuyerAccount(self):

        name = input("Name: ")
        password = input("Password: ")
        while len(password) < 8:
            print("Password should be at least 8 characters.")
            password = input("Password: ")
        account = Buyer(name)
        account.setPassword(password)
        self.buyers.append(account)
        self.currentAccount = account

    def createSellerAccount(self):

        name = input("Name: ")
        password = input("Password: ")
        while len(password) < 8:
            print("Password should be at least 8 characters.")
            password = input("Password: ")
        account = Seller(name)
        account.setPassword(password)
        self.sellers.append(account)
        print("Account Succesfully Created!")
        self.currentAccount = account

    def loginBuyer(self):
        while(True):
            name = input("Name: ")
            password = input("Password: ")
            for i in self.buyers:
                if name == i.name:
                    if i.getPassword() == password:
                        self.currentAccount = i
                        return True
            print("Incorrect information.")
            tr = input("Exit? Y/N: ").upper()
            if tr == 'Y':
                break

    def loginSeller(self):
        while(True):
            name = input("Name: ")
            password = input("Password: ")
            for i in self.sellers:
                if name == i.name:
                    if i.getPassword() == password:
                        self.currentAccount = i
                        return True
            print("Incorrect information.")
            tr = input("Exit? Y/N: ").upper()
            if tr == 'Y':
                break

    def mainMenu(self):
        Login_SignUp = input("1 Create an account\n2 Login\n3 Quit\n>>")
        while Login_SignUp not in ('1', '2', '3'):
            Login_SignUp = input("1 Create an account\n2 Login\n3 Quit\n>>")
        if Login_SignUp == '3':
            exit()
        
        Buyer_Seller = input("1 Buyer\n2 Seller\n3 Back\n>>")
        while Buyer_Seller != '1' and Buyer_Seller != '2' and Buyer_Seller != '3':
            Buyer_Seller = input("1 Buyer\n2 Seller\n3 Back\n>>")
        if Buyer_Seller == '3':
            return
        
        if Login_SignUp == '1' and Buyer_Seller == '1':
            self.createBuyerAccount()
        elif Login_SignUp == '1' and Buyer_Seller == '2':
            self.createSellerAccount()
        elif Login_SignUp == '2' and Buyer_Seller == '1':
            self.loginBuyer()
        

        elif Login_SignUp == '2' and Buyer_Seller == '2':
            self.loginSeller()

    def sellerMenu(self):
        while(True):
            self.updateProducts()
            print(f"\nName: {self.currentAccount.name}\nCredits: Php{self.currentAccount.getCredits()}")
            action = input("1 View your products\n2 Add Product\n3 Add Stocks\n4 Remove Product\n5 Set product price\n6 Deposit\n7 View transactions\n8 Logout\n>>")
            while action not in ('1', '2', '3', '4', '5', '6', '7', '8'):
                action = input("1 View your products\n2 Add Product\n3 Add Stocks\n4 Remove Product\n5 Set product price\n6 Deposit\n7 View transactions\n8 Logout\n>>")
            
            if action == '1':
                self.currentAccount.printProducts()
            
            elif action == '2':
                self.currentAccount.AddProduct()
            
            elif action == '3':
                self.currentAccount.addStocks()
                
            elif action == '4':
                self.currentAccount.removeProduct()
            
            elif action == '5':
                self.currentAccount.setPrice()
            
            elif action == '6':
                self.currentAccount.Deposit()
                
            elif action == '7':
                self.currentAccount.viewTransactions()

            elif action == '8':
                self.currentAccount = None
                break


    def buyerMenu(self):
        while(True):
            self.updateProducts()
            print(f"Name: {self.currentAccount.name}\nCredits: Php{self.currentAccount.getCredits()}")
            action = input("1 View products\n2 Add to Cart\n3 Remove from Cart\n4 View Cart\n5 Deposit\n6 Checkout\n7 View Transactions\n8 Logout\n>>")
            while action not in ('1', '2', '3', '4', '5', '6', '7', '8'):
                action = input("1 View products\n2 Add to Cart\n3 Remove from Cart\n4 View Cart\n5 Deposit\n6 Checkout\n7 View Transactions\n8 Logout\n>>")
            
            if action == '1':
                self.viewProducts()
            
            elif action == '2':
                try:
                    id = int(input("Product ID: "))
                    for i in self.products:
                        if i.productID == id:
                            print(i.name)
                            self.currentAccount.addToCart(i)       
                except:
                    print("Invalid product ID.")
            elif action == '3':
                self.currentAccount.removeFromCart()
            elif action == '4':
                self.currentAccount.printCart()
            
            elif action == '5':
                self.currentAccount.Deposit()
            
            elif action == '6':
                self.currentAccount.checkOut()
            
            elif action == '7':
                self.currentAccount.viewTransactions()
            
            else:
                self.currentAccount = None
                break

    def run(self):
        while(True):
            self.updateProducts()
            if self.currentAccount == None:
                self.mainMenu()
            
            if type(self.currentAccount) == Seller:
                self.sellerMenu()
            
            elif type(self.currentAccount) == Buyer:
                self.buyerMenu()

