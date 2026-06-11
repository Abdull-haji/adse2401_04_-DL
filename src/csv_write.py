import csv

rows = [
    ["order_id","customer","amount","country"],
    [1,"john doe",100,"usa"],
    [2,"jane doe",150,"canada"],
    [3,"bob smith",200,"uk"]
]

with open("orders.csv", "w",newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)

