class Order:
    def __init__(self, order_id, customer_name, order_date, produits):
        # produits est un dictionnaire (product_id:quantité)
        # 'order_date' est en format DD/MM/YYYY
        #TODO : Initialiser les attributs de la commande
        self.order_id = order_id
        self.customer_name = customer_name
        self.order_date = order_date
        self.produits = produits
    def afficher_details_commande(self):
        #TODO : Afficher les détails de la commande
        #Exemple : afficher l'ID, le nom du client, la date , et les produits commandés
        print(f"Order ID: {self.order_id}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Order Date: {self.order_date}")
        print("Products:")
        for product_id, quantity in self.produits.items():
            print(f"Product ID: {product_id}, Quantity: {quantity}")
