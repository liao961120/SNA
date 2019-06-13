import csv

with open('name_lookup.csv', 'r') as f:
    lookups = csv.DictReader(f)
    lookups = list(lookups)

with open('transfer_netSE.csv', 'r') as f:
    rows = csv.reader(f)
    data2 = list(rows)


# replace first column of matrix
for row in data2:
    for row2 in lookups:
        if row2['transfer'] == row[0]:
            row[0] = row2['college104']

# Replace first row of matrix 
for i, ele in enumerate(data2[0]):
    for row in lookups:
        if ele == row['college104_id']:
            data2[0][i] = row['college104']



with open('../transfer_netSE2.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(data2)
