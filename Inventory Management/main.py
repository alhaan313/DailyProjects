# Inventory stock management
import sqlite3

class Item:
    def __init__(self, name, quantity, low_stock_threshold):
        self.name = name
        self.quantity = quantity   
        self.low_stock_threshold = low_stock_threshold

    def is_low_stock(self):
        return self.quantity < self.low_stock_threshold
    
    def __str__(self):
        status = "Low Stock!" if self.is_low_stock() else "In Stock"
        return f"{self.name}: {self.quantity} units ({status})"

class InventoryManager:
    def __init__(self):
        self.db = sqlite3.connect('inventory.db')
        self.create_tables()
    
    def create_tables(self):
        with self.db:
            self.db.execute('''CREATE TABLE IF NOT EXISTS inventory
                            (name TEXT, quantity INTEGER, low_stock_threshold INTEGER)''')
            
    def add_item(self, name, quantity, low_stock_threshold):
        with self.db:
            self.db.execute('INSERT INTO inventory(name, quantity, low_stock_threshold) VALUES (?, ?, ?)',
                            (name, quantity, low_stock_threshold))
        print(f"Item '{name}' added to inventory.")

    def update_stock(self, name, quantity_change):
        with self.db:
            self.db.execute('UPDATE inventory SET quantity=quantity + ? WHERE name = ? ',
                            (quantity_change, name))
        print(f"Stock updated for '{name}' with this much change in the stocks {quantity_change}")
    
    def view_inventory(self):
        with self.db:
            items = self.db.execute('SELECT name, quantity, low_stock_threshold FROM inventory').fetchall()
        print("\nInventory: ")
        for item in items:
            name, quantity, threshold = item
            status = "Low Stock" if quantity<threshold else "Sufficient Stock"
            print(f"{name}: {quantity} units ({status})")
        
    def low_stock_alerts(self):
        with self.db:
            items = self.db.execute('SELECT name, quantity, low_stock_threshold FROM inventory WHERE quantity < low_stock_threshold').fetchall()
        print("\nLow-Stock Alerts:")
        if not items:
            print("No items are running low on stock.")
        else:
            for item in items:
                name, quantity, _ = item
                print(f"'{name}' is running low with only {quantity} units left!")

# Testing out the code
# Sample items
Soap = Item("Soap", 20, 10)
Pen = Item("Pen", 50, 5)
Jam = Item("Jam", 5, 10)

# Inventory Manager
inventory_manager = InventoryManager()

# Adding items to the inventory
inventory_manager.add_item(Soap.name, Soap.quantity, Soap.low_stock_threshold)
inventory_manager.add_item(Pen.name, Pen.quantity, Pen.low_stock_threshold)
inventory_manager.add_item(Jam.name, Jam.quantity, Jam.low_stock_threshold)


print("\n--- Inventory ---")
inventory_manager.view_inventory()

print("\n--- Updating Stock ---")
inventory_manager.update_stock("Soap", -40)
inventory_manager.update_stock("Jam", 10)
