import csv

def csvtodict(file):
    with open(file,'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            print row

csvtodict("userdetails.csv")


