from pymongo import MongoClient
import csv
import time 
import datetime

client = MongoClient()
db = client.dowjones_sa
prices = {"":""}
holidays =[datetime.datetime(2014,1,15),datetime.datetime(2014,2,16)]


def date_by_adding_business_days(from_date, add_days):
    business_days_to_add = add_days
    current_date = from_date
    while business_days_to_add > 0:
        current_date += datetime.timedelta(days=1)
        weekday = current_date.weekday()
        if weekday >= 5: # sunday = 6
            continue
        if current_date in holidays:
            continue
        business_days_to_add -= 1
    return current_date

if __name__ == '__main__':
	'''
	For chevron/coca cola: key = date_add_3.strftime("%d/%m/%Y")
	For exxon: key = date_add_3.strftime("%Y-%m-%d")
	'''

	for d in db.dowjones.find({"company" : "coca cola"}):
		prices[d['date']] = d['adj_close']

	for tweet in db.tweets.find({"company" : "coca cola"}):
		from_date=tweet['created_at']      
		struct=time.strptime(from_date,"%a %b %d %H:%M:%S +0000 %Y")
		date = datetime.datetime(*struct[:6])
		date_add_3 = date_by_adding_business_days(date, 3)
		key = date_add_3.strftime("%d/%m/%Y")
		if key in prices.keys():
			tweet['price'] = prices[key]
			db.tweetswithprices.insert(tweet)


		
