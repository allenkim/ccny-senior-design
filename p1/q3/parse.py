from search import *
import json
import ast
import statistics


with open('links_with_query.txt', 'r') as infile:
	lines = infile.readlines()

count = 0
enum = 0

# A B and C
res = {'A': {'title':[], 'summ':[], 'keywords':[] }, 
       'B':  {'title':[], 'summ':[], 'keywords':[] },
	'C':  {'title':[], 'summ':[], 'keywords':[] } };

# Enum Values
arr = [0,1,2] 
key = randomize(arr)

for idx, line in enumerate(lines[:10]):
	if (line.isspace()) :
		continue;
	print( "At line: " + str(idx) )
	if (idx % 5 == 0):
		real_url = line
		#print(real_url)
	elif (idx % 5 == 1):
		#print(getLinks(key['A'], line) )
		res['A']['title'].append(score(getLinks(key['A'], line), real_url))
		res['B']['title'].append(score(getLinks(key['B'], line), real_url))
		res['C']['title'].append(score(getLinks(key['C'], line), real_url))
	elif (idx % 5 == 2):
		res['A']['summ'].append(score(getLinks(key['A'], line), real_url))
		res['B']['summ'].append(score(getLinks(key['B'], line), real_url))
		res['C']['summ'].append(score(getLinks(key['C'], line), real_url))
	elif (idx % 5 == 3):
		query = " ".join(ast.literal_eval(line))
		#print( query )
		res['A']['keywords'].append(score(getLinks(key['A'], query), real_url))
		res['B']['keywords'].append(score(getLinks(key['B'], query), real_url))
		res['C']['keywords'].append(score(getLinks(key['C'], query), real_url))		

with open('results.txt', 'a') as results:
	results.write(json.dumps(res['A']) + "\n");
	results.write(json.dumps(res['B']) + "\n");
	results.write(json.dumps(res['C']) + "\n");

with open('key.txt', 'a') as keyfile:
	keyfile.write(json.dumps(key))

#print(len(res['A']['summ']))
	
titlestat = [statistics.mean(res['A']['title']), statistics.mean(res['B']['title']), statistics.mean(res['C']['title']) ]

summstat = [statistics.mean(res['A']['summ']), statistics.mean(res['B']['summ']), statistics.mean(res['C']['summ']) ]

keywordstat = [statistics.mean(res['A']['keywords']), statistics.mean(res['B']['keywords']), statistics.mean(res['C']['keywords']) ]

g = statistics.mean([titlestat[0], summstat[0], keywordstat[0]])
b = statistics.mean([titlestat[1], summstat[1], keywordstat[1]])
y = statistics.mean([titlestat[2], summstat[2], keywordstat[2]])

print(titlestat);
#print(summstat);
#print(keywordstat);
#print( g, b, y);
