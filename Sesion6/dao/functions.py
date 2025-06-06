#Data Acces Object
"""Agregar productos"""
class ProductDao:
    def __init__(self):
        self.products = []
        
    def add(self, product):
        self.products.append(product)
            
    def show(self):
        for product in self.products:
            print(product)