class Menu(object):
    def __init__(self):
        self.products = dict()
    
    def add_product(self, product):
        self.products[product.product_id] = product
    
    def print_menu(self):
        for product_id, product in sorted(self.products.items()):
            print '%2s %-20s $%2.2f' % (product.product_id, product.name, product.price)
    
    def find_product(self, product_id):
        product = self.products.get(product_id)
        return product 
    