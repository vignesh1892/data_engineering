import csv
columns_to_keep = ["custid", "fullname"]
with open("custs.csv","r") as f:
    custrec= f.readlines()
    custs=[ cust.strip().split(",") for cust in custrec]
    print(custs)
    for cust in custs[1:]:
        print(cust[1])



# Columns you want to keep
columns_to_keep = ["custid", "fullname"]

with open("custs.txt", "r") as infile, open("selected_columns.txt", "w", newline="") as outfile:
    reader = csv.DictReader(infile)  # Read as dict
    writer = csv.DictWriter(outfile, fieldnames=columns_to_keep)

    writer.writeheader()  # Write header first
    for row in reader:
        writer.writerow({col: row[col] for col in columns_to_keep})
