__author__ = 'Captain_Ron'

from fuzzywuzzy import process
from fuzzywuzzy import fuzz
import csv

save_file = open('FuzzyResults3.csv', 'wt')
writer = csv.writer(save_file, lineterminator = '\n')

def parse_csv(path):

    with open(path,'r') as f:
        for row in f:
            row = row.split(',')
            yield row


if __name__ == "__main__":
    ## Create lookup dictionary by parsing the products csv
    data = {}
    for row in parse_csv('Prod.csv'):
        data[row[0]] = row[1]

    ## For each row in the lookup compute the partial ratio
    for row in parse_csv("LookUp.csv"):
        for found, score in process.extract(row, data[row[0]], limit=100):
            if score >= 60:
                print('%d%% partial match: "%s" with "%s" ' % (score, row, found))
                Digi_Results = [score, row, found]
                writer.writerow(Digi_Results)


save_file.close()