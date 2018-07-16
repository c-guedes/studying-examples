import csv

with open('teste.csv', 'rb') as f:
    reader = csv.read(f)
for row in reader:
print (row)