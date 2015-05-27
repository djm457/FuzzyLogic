__author__ = 'Captain_Ron'

from fuzzywuzzy import process

def parse_csv(path):

    with open(path,'r') as f:
        for row in f:
            print(row)
            yield row

if __name__ == "__main__":
    ## Create lookup dictionary by parsing the products csv
    data = dict((row[0], row[1]) for row in parse_csv("Prod.csv"))

    ## For each row in the lookup compute the partial ratio
    for row in parse_csv("LookUp.csv"):
        for found, score in process.extract(row[0], data.keys(), limit=100):
            if score >= 60:
                print('%d%% partial match: "%s" with "%s" ' % (score, row[0], found))


