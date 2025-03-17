from product import Product
from order import Order
from store_management import StoreManagement

if __name__ == "__main__":
    magasin = StoreManagement()
    
    # Création de plusieurs produits et ajout au magasin
    produit1 = Product(1, 'Smartphone', 699.99, 50)
    produit2 = Product(2, 'Laptop', 1299.99, 30)
    produit3 = Product(3, 'Airpods', 129.99, 100)
    produit4 = Product(4, 'Tablette', 799.99, 40)
    produit5 = Product(5, 'Apple Watch', 349.99, 60)
    
    magasin.ajouter_produit(produit1)
    magasin.ajouter_produit(produit2)
    magasin.ajouter_produit(produit3)
    magasin.ajouter_produit(produit4)
    magasin.ajouter_produit(produit5)
    
    print("Liste des produits disponibles:")
    magasin.afficher_produits()
    
    # Simulation de commandes
    try:
        # Commande 1: Jour 5
        magasin.passer_commande("Martin Matin", "05/03/2025", {1: 2, 3: 1})
        
        # Commande 2: Jour 10
        magasin.passer_commande("Nessa", "10/03/2025", {2: 1, 5: 2})
        
        # Commande 3: Jour 15
        magasin.passer_commande("Imane", "15/03/2025", {4: 3, 3: 2})
        
        # Commande 4: Jour 15 (même jour)
        magasin.passer_commande("Angelo la debrouille", "15/03/2025", {1: 1, 2: 1, 5: 1})
        
        # Commande 5: Jour 20
        magasin.passer_commande("Lucas", "20/03/2025", {3: 5, 5: 1})
        
        # Commande 6: Jour 25
        magasin.passer_commande("Emma", "25/03/2025", {1: 3, 4: 2})
        
        print("\nListe des commandes:")
        magasin.afficher_commandes()
        
        # Annulation d'une commande (par exemple, la commande 3)
        print("\nAnnulation de la commande #3:")
        magasin.annuler_commande(3)
        
        print("\nListe des commandes après annulation:")
        magasin.afficher_commandes()
        
        # Affichage de l'histogramme des ventes quotidiennes
        print("\nHistogramme des ventes quotidiennes:")
        magasin.afficher_ventes_quotidiennes()
        
        # Calcul et affichage des statistiques des ventes quotidiennes
        stats = magasin.calculer_statistiques_ventes()
        print("\nStatistiques des ventes quotidiennes:", stats)
        print(f"- Moyenne: {stats['moyenne']:.2f} articles par jour")
        print(f"- Écart-type: {stats['ecart_type']:.2f}")
        print(f"- Minimum: {stats['minimum']} articles")
        print(f"- Maximum: {stats['maximum']} articles")
        
        # Affichage du stock restant
        print("\nStock restant après les commandes:")
        magasin.afficher_produits()
        
    except ValueError as e:
        print(f"Erreur: {e}")