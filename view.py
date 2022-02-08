""" view.py """

# Import external modules
import config
import controller

datafile = config.datafile
fieldnames = config.fieldnames

# Print all rows
def print_all(rows):
  print('All rows in {}'.format(datafile))
  for row in rows:
    print(row)


# Print a single requested row
def print_one(row):
  if 'not found' in row:
    print(row)
  else:
    print('Found item {}'.format(row['name']))
    print(row)


# Print error message
def print_error(msg):
  print('Error: {}'.format(msg))


# Print error message
def print_message(msg):
  print('{}'.format(msg))

