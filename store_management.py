import numpy as np
import matplotlib.pyplot as plt
from order import Order  # Assurez vous que le module order est accessible
from datetime import datetime

class StoreManagement:
    def __init__(self):
        self.produits = []  # dictionnaire {product_id: Product}
        self.commandes = []  # liste des commandes
        self.ventes_quotidiennes = np.zeros(31, dtype=int)  # ventes pour chaque jour du mois
    
    def ajouter_produit(self, product):
        # TODO: Ajouter un produit à la liste des produits
        self.produits.append(product)
    
    def passer_commande(self, customer_name, order_date, produits_commande):
        # produits_commande: dictionnaire (product_id:quantité)
        # 1. Vérifier que chaque produit existe et que le stock est suffisant
        for product_id, quantite in produits_commande.items():
            produit_trouve = False
            for produit in self.produits:
                if produit.product_id == product_id:
                    produit_trouve = True
                    if produit.stock < quantite:
                        raise ValueError(f"Stock insuffisant pour le produit {produit.name} (ID: {product_id})")
                    break
            if not produit_trouve:
                raise ValueError(f"Produit avec ID {product_id} non trouvé")
        
        # 2. Décrémenter le stock de chaque produit commandé
        for product_id, quantite in produits_commande.items():
            for produit in self.produits:
                if produit.product_id == product_id:
                    produit.stock -= quantite
                    break
        
        # 3. Créer un objet Order et l'ajouter à la liste des commandes
        order_id = len(self.commandes) + 1  # ID simple basé sur le nombre de commandes
        nouvelle_commande = Order(order_id, customer_name, order_date, produits_commande)
        self.commandes.append(nouvelle_commande)
        
        # 4. Mettre à jour les ventes quotidiennes en fonction de la date de la commande
        try:
            date_obj = datetime.strptime(order_date, "%d/%m/%Y")
            jour = date_obj.day
            # Calculer le total d'articles vendus dans cette commande
            total_articles = sum(produits_commande.values())
            self.ventes_quotidiennes[jour-1] += total_articles  # jour-1 car les indices commencent à 0
        except ValueError:
            raise ValueError("Format de date incorrect. Utilisez DD/MM/YYYY")
            
        return nouvelle_commande
    
    def annuler_commande(self, order_id):
        # 1. Trouver la commande avec l'ID donné
        commande_trouvee = None
        index_commande = -1
        
        for i, commande in enumerate(self.commandes):
            if commande.order_id == order_id:
                commande_trouvee = commande
                index_commande = i
                break
                
        if commande_trouvee is None:
            raise ValueError(f"Commande avec ID {order_id} non trouvée")
        
        # 2. Rétablir le stock pour chaque produit de la commande
        for product_id, quantite in commande_trouvee.produits.items():
            for produit in self.produits:
                if produit.product_id == product_id:
                    produit.stock += quantite
                    break
        
        # 3. Ajuster self.ventes_quotidiennes
        try:
            date_obj = datetime.strptime(commande_trouvee.order_date, "%d/%m/%Y")
            jour = date_obj.day
            total_articles = sum(commande_trouvee.produits.values())
            self.ventes_quotidiennes[jour-1] -= total_articles
        except ValueError:
            pass  # Si la date était invalide, nous ne pouvons pas ajuster correctement
        
        # 4. Supprimer la commande de la liste des commandes
        self.commandes.pop(index_commande)
        
        return True
    
    def afficher_produits(self):
        # Afficher le détail de tous les produits présents dans le dictionnaire self.produits
        if not self.produits:
            print("Aucun produit disponible")
            return
            
        print("=== LISTE DES PRODUITS ===")
        for produit in self.produits:
            produit.afficher_details_produit()
            print("-" * 30)
    
    def afficher_commandes(self):
        # Afficher la liste de toutes les commandes enregistrées
        if not self.commandes:
            print("Aucune commande enregistrée")
            return
            
        print("=== LISTE DES COMMANDES ===")
        for commande in self.commandes:
            commande.afficher_details_commande()
            print("-" * 30)
    
    def afficher_ventes_quotidiennes(self):
        jours =[str(i+1) for i in range(31)]
        ventes = self.ventes_quotidiennes.tolist()
        plt.figure(figsize=(10,6))
        plt.bar(jours,ventes)
        plt.title("Ventes Quotidiennes")
        plt.xlabel("Jour")
        plt.ylabel("Nombre d'articles vendus")
        plt.show()
    
    def calculer_statistiques_ventes(self):
        # Utiliser numpy pour calculer la moyenne, l'écart type, le minimum et le maximum des ventes quotidiennes
        stats = {
            'moyenne': np.mean(self.ventes_quotidiennes),
            'ecart_type': np.std(self.ventes_quotidiennes),
            'minimum': np.min(self.ventes_quotidiennes),
            'maximum': np.max(self.ventes_quotidiennes)
        }
        return stats