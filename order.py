class Order(object):
    def __init__(self):
        self.order_items = list()
    
    def get_total(self):
        total = 0
        for product, quantity in self.order_items:
            total = total + product.price * quantity
        return total
        
    def add_item(self, product, quantity):
        self.order_items.append((product, quantity))
        
    def print_receipt(self):
        print 'Item                       Price  Qty  Sub  Ttl'
        print '=========================  =====  ===  ========'
        for p, q, in self.order_items:
            print '%-20s $%2.2f %3s $%5.2f' % (p.name, p.price, q, p.price * q)
        print '\nGrand total: $%2.2f' % self.get_total()