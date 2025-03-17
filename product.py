class Product:
    def __init__(self, product_id, name,price,stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock
    # TODO: Compléter l'affichage des détails du produit
    def afficher_details_produit(self):
        print(f"Product ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Price: {self.price}")
        print(f"Stock: {self.stock}")