from product import Product
from menu import Menu
from order import Order


def clear_screen():
  import os
  os.system('clear')


def build_menu():
  menu = Menu()
  menu.add_product(Product(1, 'Hamburger', 5.99))
  menu.add_product(Product(2, 'Cheeseburger', 6.99))
  menu.add_product(Product(4, 'Fries', 1.99))
  menu.add_product(Product(3, 'Double Cheeseburger', 7.99))
  return menu
  
  
def take_order(menu):
  divider = '=' * 60
  order = Order()
  last_item = None
  while True:
    clear_screen()
    print divider
    if last_item:
      print 'Added %s to your order!' % last_item
    print 'Order total: $%3.2f' % order.get_total()
    print divider
    print 'Below is our menu.  Enter an item number to order it,'
    print 'or just hit enter to complete your order.'
    print divider
    menu.print_menu()
    product_number = raw_input('Product number: ')
    if product_number == '':
      break
    product = menu.find_product(int(product_number))
    if not product:
      continue
    quantity = int(raw_input('Quantity: '))
    order.add_item(product, quantity)
    last_item = product.name
  return order
  
  
def finish_order(order):
  clear_screen()
  print 'Order complete! Thank you for your business!\n'
  print 'Here is your receipt...\n'
  order.print_receipt()
    
    
menu = build_menu()
order = take_order(menu)
finish_order(order)