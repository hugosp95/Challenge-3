import os
import csv

with open(budget_data, 'r') as csvfilee:
  csvreader = csv.reader(csvfile, delimiter=',')
  header = next(csvreader)
  
