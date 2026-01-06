#1.adatok betoltese fajlbol
#2.uj rendeles felvetel
#3.rendesles modositasa
#4.rendelesek megtekintese
#5.rendelesek mentese
#6. statisztika
#7. rendelés törlése
import csv
import json
from collections import Counter
from datetime import datetime

MENU_FILE = 'menu.csv'
ORDERS_FILE = 'order.json'

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name}: {self.price} Ft'

    def to_dict(self):
        return {'name': self.name, 'price': self.price}

class Order:
    def __init__(self, customer_name: str, table_number:int, items:list[MenuItem]):
        self.customer_name = customer_name
        self.table_number = table_number
        self.items = items
        self.timestamp =datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def total_price(self):
        return sum(int(item.price) for item in self.items)

    def __str__(self):
        item_names = ', '.join(item.name for item in self.items)
        return (f'Vendeg: {self.customer_name}, Asztal:{self.table_number},'
                f'Tetelek: {item_names}, Total: {self.total_price()} Ft'
                f'Time: {self.timestamp}')

    def to_dict(self):
        return {
            'customer_name': self.customer_name,
            'table_number': str(self.table_number),
            'items': [item.to_dict() for item in self.items],
            'timestamp': self.timestamp
        }

def load_menu():
    menu = []
    try:
        with open(MENU_FILE, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                menu.append(MenuItem(row['name'], row['price']))
    except FileNotFoundError:
        print('Menu fájl nem található! Ellenőrizd le, hogy a mnu.csv megtalalhato e program mellett.')
    except:
        print('Kritikus hiba a menu betoltese kozben')
    return menu

def save_orders(orders):
    try:
        with open(ORDERS_FILE, mode='w', encoding='utf-8') as file:
            json.dump([order.to_dict() for order in orders], file)
    except TypeError as err:
        print('Kritikus hiba!')
        print(err)

def load_orders():
    orders = []
    try:
        with open(ORDERS_FILE, mode='r', encoding='utf-8') as file:
            orders_dict = json.load(file)
            for order_item in orders_dict:
                items = [MenuItem(item['name'], item['price']) for item in order_item['items']]
                order = Order(order_item['customer_name'], int(order_item['table_number']), items)
                order.timestamp = order_item['timestamp']
                orders.append(order)
    except FileNotFoundError:
        print('rendelés fájl nem található, ellenőrizd le, hogy létezik e rendeles json file!')
    except:
        print('Kritikus hiba!')
    return orders

def list_menu(menu):
    print("===MENU===")
    for index , item in enumerate(menu, start = 1):
        print(f'{index}. {item}')

def take_order(menu: list[MenuItem]):
    print("=== Uj Rendeles ===")
    customer_name = input('Vendeg neve: ')
    table_number = input('Asztal szama: ')
    list_menu(menu)
    items = []
    while True:
        choice = input('Kerem adjon meg egy elemet szam alapja. '
                       'Ha nem akar mar semmit rendelni, nyomjon entert')
        if not choice:
            break
        elif choice.isdigit() and  1 <= int(choice) <= len(menu):
            items.append(menu[int(choice) - 1])
        else:
            print('rossz volt a valasztas, probald meg ujra!')
    return Order(customer_name, int(table_number), items)

def list_orders(orders):
    print("===Jelenlegi rendelesek===")
    for index, order in enumerate(orders, start=1):
        print(f'{index}. {order}')

def delete_order(orders):
    list_orders(orders)
    choice = input('Valasszon ke egy rendelest a torleshez: ')
    if choice.isdigit() and 1 <= int(choice) <= len(orders):
        del orders[int(choice) - 1]
        print('A rendeles torolve...')
    else:
        print('Rosszat opciot valasztott!')

def generate_statistics(orders):
    if not orders:
        print('Nincs megredneles a statisztika generálásához')
        return
    total_income = sum(order.total_price() for order in orders)
    all_items = [item.name for order in orders for item in order.items]
    most_popular = Counter(all_items).most_common(1)[0][0]
    print(f'Teljes Bevétel: {total_income} Ft')
    print(f'A legnepszerubb etel: {most_popular}')

def main():
    menu = load_menu()
    orders = load_orders()

    while True:
        print('== Ettermi alkalmazas ==')
        print('1. Menu listazasa')
        print('2. Uj rendeles felvetele')
        print('3. Rendeles listazasa')
        print('4. Rendeles torlese')
        print('5. Statisztika')
        print('6. Mentes es kilepes')

        choice = input('Valasszon egy elemet:')
        if choice == '1':
            list_menu(menu)
        elif choice == '2':
            order = take_order(menu)
            orders.append(order)
        elif choice == '3':
            list_orders(orders)
        elif choice == '4':
            delete_order(orders)
        elif choice == '5':
            generate_statistics(orders)
        elif choice == '6':
            save_orders(orders)
            print('Rendeles sikeresen elmentve. Kilepes...')
            break
        else:
            print('ilyen opcio nincs!')

if __name__ == '__main__':
    main()






