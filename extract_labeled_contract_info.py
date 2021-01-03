import zipfile
import pandas
import csv


id = []
with open("Ponzi_label.csv", "r") as f:
    r = pandas.read_csv(f)
    id = list(r["Contract"])

print(id)
files = [
    "0to999999_ContractInfo",
    "1000000to1999999_ContractInfo",
    "2000000to2999999_ContractInfo",
    "3000000to3999999_ContractInfo",
    "4000000to4999999_ContractInfo",
    "5000000to5999999_ContractInfo",
    "6000000to6999999_ContractInfo",
    "7000000to7999999_ContractInfo",
    "8000000to8999999_ContractInfo",
    "9000000to9999999_ContractInfo",
    "10000000to10999999_ContractInfo"
];

writer = csv.writer(open('labeled_contract_info.csv', 'w', newline=''))
writer.writerow(
    ['address', 'createdBlockNumber', 'createdTimestamp', 'createdTransactionHash', 'creator', 'creatorIsContract',
     'createValue', 'creationCode', 'contractCode'])

for file in files:
    print(file);
    theZIP = zipfile.ZipFile(file + ".zip", 'r');
    theCSV = theZIP.open(file + "_Created.csv", 'r');
    theCSV.readline()

    index=0
    for line in theCSV:
        if (line.decode().split(",")[0]) in id:
            writer.writerow(line.decode().split(","))

    theCSV.close();
    theZIP.close();
