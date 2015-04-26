from pymongo import MongoClient
import csv

client = MongoClient()
db = client.dowjones_sa

csv_dict = { 'company':0,'created_at':1, 'text':2, 'hashtags':3, 'symbols':4, 'urls':5,'mentions':6 }

def get_row_json(row):
    return {
            'company':row[csv_dict['company']],
            'created_at':row[csv_dict['created_at']],
            'text':row[csv_dict['text']].decode('utf-8', 'replace'),
            'hashtags':row[csv_dict['hashtags']].decode('utf-8','replace'),
            'symbols':row[csv_dict['symbols']],
            'urls':row[csv_dict['urls']],
            'mentions':row[csv_dict['mentions']].decode('utf-8', 'replace')

            }

def store_data(csv_path):
    csvfile = open(csv_path, 'r')
    csvfile.readline()
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        #try:
            db.tweets.insert(get_row_json(row))
        #except Exception:
            #print 'ignored'
