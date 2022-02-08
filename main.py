""" main.py is the main thing
that runs on my main laptop in
the state of Maine """

__author__      = "Silvia Nittel"
__copyright__   = "Copyright 2022, SIE508, University of Maine"
__credits__     = ["Silvia Nittel", "Richard Twiggs"]

# Import external modules
import config
import controller
import view

# Import libraries
import csv
from pathlib import Path

# # Datafile Verification
datafile = config.datafile

# If the datafile does not exist, create it
if not controller.test_datafile_exists(datafile):
  controller.create_datafile(datafile)

# # Bulk Data Insertion
my_items = [
  {'name': 'bread', 'price': 2.51, 'quantity': 20},
  {'name': 'milk', 'price': 4.02, 'quantity': 10},
  {'name': 'eggs', 'price': 4.03, 'quantity': 5},
  {'name': 'vodka', 'price': 19.99, 'quantity': 2},
  {'name': 'blackberries', 'price': 6.99, 'quantity': 4},
]

# CREATE
# Insert all rows from my_items into datafile
controller.create_all(my_items)
view.print_all(controller.read_all())
input("Press Enter to continue...")

# Insert a single row into datafile
controller.create_one('bacon', price=4.46, quantity=10)
view.print_all(controller.read_all())
input("Press Enter to continue...")

# Insert a single row that already exists
controller.create_one('bread', price=8.88, quantity=888)
view.print_all(controller.read_all())
input("Press Enter to continue...")

# READ
# all_items = controller.read_all()
# view.print_all(all_items)

one_item = controller.read_one('bacon')
view.print_one(one_item)
input("Press Enter to continue...")

# If the item is not found, return message saying so
one_item = controller.read_one('cookies')
view.print_one(one_item)
input("Press Enter to continue...")

# UPDATE
controller.update_one('bacon', price=4.48, quantity=30)
one_item = controller.read_one('bacon')
view.print_one(one_item)
input("Press Enter to continue...")
# Update an item that does not exist
controller.update_one('cookies', price=8.88, quantity=888)
input("Press Enter to continue...")

# DELETE
# Delete an item that does exist
controller.delete_one('bread')
view.print_all(controller.read_all())
input("Press Enter to continue...")

# Delete an item that does not exist
controller.delete_one('cookies')
view.print_all(controller.read_all())
input("Press Enter to continue...")

# Read them all one last time
# all_items = controller.read_all()
# view.print_all(all_items)
