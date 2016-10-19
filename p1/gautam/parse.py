from search import *
import json
import statistics

with open('links_with_query.txt', 'r') as infile:
	lines = infile.readlines()

count = 0
enum = 0

Google = {'title':[], 'summ':[], 'keywords':[] }
Bing = {'title':[], 'summ':[], 'keywords':[] }
Yahoo = {'title':[], 'summ':[], 'keywords':[] }

#arr = [('Google', Google), ('Bing', Bing), ('Yahoo', Yahoo)];
#key = randomize(arr)

for idx, line in enumerate(lines):
	if (line.isspace()) :
		continue;
	print( "At line: " + str(idx) )
	if (idx % 5 == 0):
		real_url = line
	elif (idx % 5 == 1):
		Google['title'].append(score(getLinks(0, line), real_url))
		Bing['title'].append(score(getLinks(1, line), real_url))
		Yahoo['title'].append(score(getLinks(2, line), real_url))
	elif (idx % 5 == 2):
		Google['summ'].append(score(getLinks(0, line), real_url))
		Bing['summ'].append(score(getLinks(1, line), real_url))
		Yahoo['summ'].append(score(getLinks(2, line), real_url))
	elif (idx % 5 == 3):
		query = " ".join(json.loads(line))
		Google['summ'].append(score(getLinks(0,query), real_url))
		Bing['summ'].append(score(getLinks(1, query), real_url))
		Yahoo['summ'].append(score(getLinks(2, query), real_url))		

with open('results.txt', 'a') as results:
	results.write(json.dumps(Google) + "\n");
	results.write(json.dumps(Bing) + "\n");
	results.write(json.dumps(Yahoo) + "\n");
	
titlestat = [statistics.mean(Google['title']), statistics.mean(Bing['title']), statistics.mean(Yahoo['title']) ]

summstat = [statistics.mean(Google['summ']), statistics.mean(Bing['summ']), statistics.mean(Yahoo['summ']) ]

keywordsstat = [statistics.mean(Google['keywords']), statistics.mean(Bing['keywords']), statistics.mean(Yahoo['keywords']) ]

g = statistics.mean([titlestat[0], summstat[0], keywordstat[0]])
b = statistics.mean([titlestat[1], summstat[1], keywordstat[1]])
y = statistics.mean([titlestat[2], summstat[2], keywordstat[2]])

print(titlestat);
print(summstat);
print(keywordstat);
print( g, b, y);
