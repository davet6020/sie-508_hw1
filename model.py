""" model.py """

# Import external modules
import config
import view

# Import libraries
import csv
import fileinput
from pathlib import Path
import os

datafile = config.datafile
fieldnames = config.fieldnames


# Create one row in datafile
def create_one(name, price, quantity):
  # Make sure the item is not already in the datafile
  if search_one(name):
    msg = 'Item {} already exists in {}'.format(name, datafile)
    view.print_message(msg)
  else:
    # Fail if null values are passed in, otherwise convert to list
    if len(name) == 0 or len(str(price)) == 0 or len(str(quantity)) == 0:
      return "Must specify a value for name, price and quantity"
    else:
      row = [{'name': name, 'price': price, 'quantity': quantity}]

    # With functions like a try catch
    with open(datafile, 'a', newline='', encoding='UTF8') as csvfile:
      writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
      try:
        writer.writerows(row)
      except Exception as e:
        view.print_error(e)


# Read one row
def read_one(needle):
  with open(datafile, encoding='UTF8') as csvfile:
    one_item = {}
    reader = csv.DictReader(csvfile, fieldnames)
    next(reader)
    for row in reader:
      if row['name'] == needle:
        one_item = {'name': row['name'], 'price': row['price'], 'quantity': row['quantity']}
        return one_item
      else:
        one_item = '"{}" not found'.format(needle)

  return one_item


# read all items
def read_all():
  if os.path.getsize(datafile) == 0:
    return {'no data'}

  all_items = []
  with open(datafile, encoding='UTF8') as csvfile:
    reader = csv.DictReader(csvfile, fieldnames)
    next(reader)
    for row in reader:
      ai = {'name': row['name'], 'price': row['price'], 'quantity': row['quantity']}
      all_items.append(ai)

  return all_items


# Update one row in datafile
def update_one(name, price, quantity):
  if not search_one(name):
    msg = '"{}" not found'.format(name)
    view.print_message(msg)
    return

  with fileinput.input(datafile, inplace=True, mode='r') as csvfile:
    msg = 'Updating {}'.format(name)
    view.print_message(msg)

    reader = csv.DictReader(csvfile)
    print(",".join(reader.fieldnames))  # print back the headers
    for row in reader:
      if row["name"] == name:
        row["price"] = price
        row["quantity"] = quantity
      print(",".join([row["name"], str(row["price"]), str(row["quantity"])]))


# Delete one row in datafile
def delete_one(name):
  if not search_one(name):
    msg = '"{}" not found'.format(name)
    view.print_message(msg)
    return

  with fileinput.input(datafile, inplace=True, mode='r') as csvfile:
    msg = 'Deleting {}'.format(name)
    view.print_message(msg)

    reader = csv.DictReader(csvfile)
    print(",".join(reader.fieldnames))  # print back the headers

    for row in reader:
      if not row["name"] == name:
        print(",".join([row["name"], str(row["price"]), str(row["quantity"])]))


# Search the datafile for item name
def search_one(needle):
  with open(datafile, encoding='UTF8') as csvfile:
    reader = csv.DictReader(csvfile, fieldnames)
    next(reader)
    for row in reader:
      if row['name'] == needle:
        return True
  return False


# Create datafile if it does not exist
def create_datafile(csvfile):
  with open(datafile, 'w+', encoding='UTF8') as csvfile:
    pass


# Check to see if datafile exists
def test_datafile_exists(csvfile):
  path = Path(csvfile)
  return path.is_file()
