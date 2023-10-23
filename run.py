from eComClass import Product, Buyer, Seller, Transaction

Buyers = []
Sellers = []
Products = []
CurrentAccount = None

def checkStocks():
    for i in Sellers:
        for j in i.products:
            if j.stockQuantity == 0:
                i.products.remove(j)

def viewProducts():
    for i in Sellers:
        for j in i.products:
            j.printDetails()


def updateProducts():
    global Products
    for i in Sellers:
        for j in i.products:
            Products = list(Products)
            Products.append(j)
            Products = set(Products)
    checkStocks()

def createBuyerAccount():
    global CurrentAccount
    name = input("Name: ")
    password = input("Password: ")
    while len(password) < 8:
        print("Password should be at least 8 characters.")
        password = input("Password: ")
    account = Buyer(name)
    account.setPassword(password)
    Buyers.append(account)
    CurrentAccount = account

def createSellerAccount():
    global CurrentAccount
    name = input("Name: ")
    password = input("Password: ")
    while len(password) < 8:
        print("Password should be at least 8 characters.")
        password = input("Password: ")
    account = Seller(name)
    account.setPassword(password)
    Sellers.append(account)
    print("Account Succesfully Created!")
    CurrentAccount = account

def loginBuyer():
    global CurrentAccount
    while(True):
        name = input("Name: ")
        password = input("Password: ")
        for i in Buyers:
            if name == i.name:
                if i.getPassword() == password:
                    CurrentAccount = i
                    return True
        print("Incorrect information.")
        tr = input("Exit? Y/N: ").upper()
        if tr == 'Y':
            break

def loginSeller():
    global CurrentAccount
    while(True):
        name = input("Name: ")
        password = input("Password: ")
        for i in Sellers:
            if name == i.name:
                if i.getPassword() == password:
                    CurrentAccount = i
                    return True
        print("Incorrect information.")
        tr = input("Exit? Y/N: ").upper()
        if tr == 'Y':
            break

def mainMenu():
    Login_SignUp = input("1 Create an account\n2 Login\n>>")
    while Login_SignUp != '1' and Login_SignUp != '2':
        Login_SignUp = input("1 Create an account\n2 Login\n>>")
    
    Buyer_Seller = input("1 Buyer\n2 Seller\n3 Back\n>>")
    while Buyer_Seller != '1' and Buyer_Seller != '2' and Buyer_Seller != '3':
        Buyer_Seller = input("1 Buyer\n2 Seller\n3 Back\n>>")
    if Buyer_Seller == '3':
        return
    
    if Login_SignUp == '1' and Buyer_Seller == '1':
        createBuyerAccount()
    elif Login_SignUp == '1' and Buyer_Seller == '2':
        createSellerAccount()
    elif Login_SignUp == '2' and Buyer_Seller == '1':
        loginBuyer()
    else:
        loginSeller()

def sellerMenu():
    while(True):
        updateProducts()
        global CurrentAccount
        print(f"\nName: {CurrentAccount.name}\nCredits: Php{CurrentAccount.getCredits()}")
        action = input("1 View your products\n2 Add Product\n3 Set Product Price\n4 Remove Product\n5 Deposit\n6 Logout\n>>")
        while action not in ('1', '2', '3', '4', '5', '6', '7'):
            action = input("1 View your products\n2 Add Product\n3 Set Product Price\n4 Remove Product\n5 Deposit\n6 Logout\n>>")
        
        if action == '1':
            CurrentAccount.printProducts()
        
        elif action == '2':
            CurrentAccount.AddProduct()
        
        elif action == '3':
            CurrentAccount.setPrice()
        
        elif action == '4':
            CurrentAccount.removeProduct()
        
        elif action == '5':
            CurrentAccount.Deposit()
        
        else:
            CurrentAccount = None
            break

def buyerMenu():
    while(True):
        updateProducts()
        global CurrentAccount
        print(f"Name: {CurrentAccount.name}\nCredits: Php{CurrentAccount.getCredits()}")
        action = input("1 View products\n2 Add to Cart\n3 Remove from Cart\n4 View Cart\n5 Deposit\n6 Checkout\n7 View Transactions\n8 Logout\n>>")
        while action not in ('1', '2', '3', '4', '5', '6', '7', '8'):
            action = input("1 View products\n2 Add to Cart\n3 Remove from Cart\n4 View Cart\n5 Deposit\n6 Checkout\n7 View Transactions\n8 Logout\n>>")
        
        if action == '1':
            viewProducts()
        
        elif action == '2':
            print("|||||||||")
            id = int(input("Product ID: "))
            for i in Products:
                if i.productID == id:
                    print(i.name)
                    CurrentAccount.addToCart(i)       

        elif action == '3':
            CurrentAccount.removeFromCart()
        elif action == '4':
            CurrentAccount.printCart()
        
        elif action == '5':
            CurrentAccount.Deposit()
        
        elif action == '6':
            CurrentAccount.checkOut()
        
        elif action == '7':
            CurrentAccount.viewTransactions()
        
        else:
            CurrentAccount = None
            break

def Run():
    while(True):
        updateProducts()
        global CurrentAccount
        if CurrentAccount == None:
            mainMenu()
        
        if type(CurrentAccount) == Seller:
            sellerMenu()
        
        elif type(CurrentAccount) == Buyer:
            buyerMenu()
Run()