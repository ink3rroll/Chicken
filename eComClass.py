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

