class Product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=float(price)
        self.quantity=int(quantity)
class Warehouse:
    def __init__(self):
        self.products=[]
    def add_product(self,product):
        self.products.append(product)
    def remove_product(self,product_name):
        for product in self.products:
            if product.name==product_name:
                self.products.remove(product)
                return True
        return False
    def get_product(self,product_name):
        for product in self.products:
            if product.name==product_name:
                return product
        return None
    def get_total_value(self):
        total_value=0
        for product in self.products:
            total_value+=product.price*product.quantity
        return total_value
    def list_products(self):
        for product in self.products:
            print(f"{product.name} - {product.quantity} units - ${product.price}")
warehouse=Warehouse()
while True:
    print("\n-- Warehouse Management System ---")
    print("1. Add Product")
    print("2. Remove Product")
    print("3. List Products")
    print("4. Calculate Total Value")
    print("0. Exit")
    choice=input("Enter your choice: ")
    if choice=="1":
        name=input("Enter the product name: ")
        price=input("Enter the product price: ")
        quantity=input("Enter the product quantity: ")
        product=Product(name,price,quantity)
        warehouse.add_product(product)
        print("Product added successfully.")
    elif choice=="2":
        name=input("Enter the product name: ")
        if warehouse.remove_product(name):
            print("Product removed successfully.")
        else:
            print("Product not found.")
    elif choice=="3":
        print("\nWarehouse products:")
        warehouse.list_products()
    elif choice=="4":
        total_value=warehouse.get_total_value()
        print(f"\nTotal value of products: ${total_value}")
    elif choice=="0":
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please try again.")
