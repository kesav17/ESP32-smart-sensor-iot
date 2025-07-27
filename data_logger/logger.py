# Logger script (optional use for data processing)
import csv

def read_csv(file='api_server/data.csv'):
    with open(file, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

if __name__ == "__main__":
    read_csv()
