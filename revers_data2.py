import csv

with open("Td-modified.csv") as fr, open("out.csv","w", newline="") as fw:
    cr = csv.reader(fr,delimiter=",")
    cw = csv.writer(fw,delimiter=",")
    cw.writerow(next(cr))  # write title as-is
    cw.writerows(reversed(list(cr)))
