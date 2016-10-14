import praw
import time

r = praw.Reddit(user_agent='Test Script')

start_date_time = '25.01.2008 00:00:00'
end_date_time = '30.12.2015 00:59:59'
pattern = '%d.%m.%Y %H:%M:%S'
start_epoch = int(time.mktime(time.strptime(start_date_time, pattern)))
end_epoch = int(time.mktime(time.strptime(end_date_time, pattern)))

search_str = "timestamp:"+str(start_epoch)+".."+str(end_epoch)

submissions = r.search(search_str,subreddit='news',sort='new',limit=1,syntax='cloudsearch')
for item in submissions:
    print(item.url)
