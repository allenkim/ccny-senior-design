import praw
import time
import requests
from random import randint

r = praw.Reddit(user_agent='Test Script')

start_date_time = '25.01.2008 00:00:00'
end_date_time = '30.12.2015 00:59:59'
pattern = '%d.%m.%Y %H:%M:%S'
start_epoch = int(time.mktime(time.strptime(start_date_time, pattern)))
end_epoch = int(time.mktime(time.strptime(end_date_time, pattern)))

link_file = "links.txt"

num_articles = 1000
limit_per_search = 10

articles_added = 0

with open(link_file, 'a') as out:
    while articles_added < num_articles:
        print(str(num_articles - articles_added) + " articles left to go")
        temp_epoch = randint(start_epoch+1,end_epoch)
        search_str = "timestamp:"+str(start_epoch)+".."+str(temp_epoch)
        submissions = r.search(search_str,subreddit='news',sort='new',limit=limit_per_search,syntax='cloudsearch')

        for link in submissions:
            try:
                req = requests.get(link.url)
            except Exception as e:
                continue
            if req.status_code == 200:
                out.write(link.url + '\n')
                articles_added += 1
