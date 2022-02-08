""" controller.py """

# Import external modules
import config
import model
import view

# Import libraries
import csv
import fileinput
from pathlib import Path
import os

datafile = config.datafile
fieldnames = config.fieldnames


# For the header of the csv file we want the dict keys -- Currently not used
# This could be useful if you were dealing with multiple data files with different column names
def get_fieldnames(rows):
  for key in rows[0].keys():
    fieldnames.append(key)


# Create one row in datafile
def create_one(name, price, quantity):
  model.create_one(name, price, quantity)


# Create list of rows in datafile
def create_all(rows):
  with open(datafile, 'a', newline='', encoding='UTF8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)


# Read one row
def read_one(needle):
  return model.read_one(needle)


# Read all rows
def read_all():
  return model.read_all()


# Update one row in datafile
def update_one(name, price, quantity):
  model.update_one(name, price, quantity)


# Delete one row in datafile
def delete_one(name):
  model.delete_one(name)


# Search the datafile for item name
def search_one(needle):
  return model.search_one(needle)


# Create datafile if it does not exist
def create_datafile(csvfile):
  model.create_datafile(csvfile)


# Check to see if the datafile exists
def test_datafile_exists(csvfile):
  return model.test_datafile_exists(csvfile)
