import csv
with open('deneme.csv', 'r') as file:
    data = file.read()

data = data.replace('\n', ' ')

with open('deneme2', 'w') as file:
    file.write(data)
