import zipfile
import pandas
import csv

id = []
with open("Ponzi_label.csv", "r") as f:
    r = pandas.read_csv(f)
    id = list(r["Contract"])

files = [
    "0to999999_NormalTransaction",
    "1000000to1999999_NormalTransaction",
    "2000000to2999999_NormalTransaction",
    "3000000to3999999_NormalTransaction"
];

writer = csv.writer(open('labeled_contract_transactions_from.csv', 'w', newline=''))
writer.writerow(
    ['blockNumber', 'timestamp', 'transactionHash', 'from', 'to', 'creates',
     'value', 'gasLimit', 'gasPrice', 'gasUsed', 'status'])

for file in files:
    print(file);
    theZIP = zipfile.ZipFile(file + ".zip", 'r');
    theCSV = theZIP.open(file + ".csv", 'r');
    theCSV.readline()

    index=0
    for line in theCSV:
        if ((line.decode().split(",")[4]) in id):
            print(line)
            writer.writerow(line.decode().split(","))

theCSV.close();
theZIP.close();