from pymongo import MongoClient
import csv

client = MongoClient()
db = client.dowjones_sa

csv_dict = { 'date':0,'open':1, 'high':2, 'low':3, 'close':4, 'volume':5,'adj_close':6 }

def get_row_json(row,company):
    return {
            'company':company,
            'date':row[csv_dict['date']],
            'open':row[csv_dict['open']],
            'high':row[csv_dict['high']],
            'low':row[csv_dict['low']],
            'close':row[csv_dict['close']],
            'volume':row[csv_dict['volume']],
            'adj_close':row[csv_dict['adj_close']]
            }

def store_data(csv_path, company):
    csvfile = open(csv_path, 'r')
    csvfile.readline()
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        db.dowjones.insert(get_row_json(row,company))
