import urllib.request
from random import shuffle

# enum -> 0: google, 1: bing, 2: yahoo

def queryforHTML(enum, query):
	if (enum == 0):
		headers={};
		headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2)';
		querystring = urllib.parse.urlencode({'q': query})
		request = urllib.request.Request('https://www.google.com/search?'+querystring, headers=headers);
		response = urllib.request.urlopen( request );
		targetstring = response.read().decode("latin-1");
	elif (enum == 1):
		querystring = urllib.parse.urlencode({'q': query})
		response = urllib.request.urlopen('https://www.bing.com?' + querystring);
		targetstring = response.read().decode("latin-1");
	else:
		querystring = urllib.parse.urlencode({'p': query})
		response = urllib.request.urlopen('https://search.yahoo.com/search?' + querystring);
		target = open('yahoo.html', 'w');
		targetstring = response.read().decode("latin-1");
	return targetstring

def HTML2Links(enum, targetstring):
	li = [];
	count = 0;
	
	if (enum == 0):
		link_index = targetstring.find("<div class=\"g\">");
		newtarget = targetstring[link_index:];
		while ( link_index != -1):
			prebegin = newtarget.find("<a");
			begin =	newtarget.find( "\"", prebegin);
			end = newtarget.find("&", begin+1);
			li.append( newtarget[begin+8:end] );
			count = count + 1;
			newtarget = newtarget[end:];
			link_index = newtarget.find("<div class=\"g\">");
			newtarget = newtarget[link_index:];
	elif (enum == 1):
		start = targetstring.find("<ol id=\"b_results\" role=\"main\" aria-label=\"Search Results\">");
		end = targetstring.find("</ol>");
		newtarget = targetstring[start:end+4];
		link_index = newtarget.find("<li class=\"b_algo\">");
		newtarget = newtarget[link_index:];
		while ( link_index != -1):
			prebegin = newtarget.find("<a");
			begin =	newtarget.find( "\"", prebegin);
			end = newtarget.find("\"", begin+1);
			li.append( newtarget[begin+1:end] );
			count = count + 1;
			newtarget = newtarget[end:];
			link_index = newtarget.find("<li class=\"b_algo\">");
			newtarget = newtarget[link_index:];
	else:
		start = targetstring.find("<ol class=\"mb-15 reg searchCenterMiddle\">");
		end = targetstring.find("</ol>", start);

		newtarget = targetstring[start:end+4];
		link_index = newtarget.find("<li id");
		newtarget = newtarget[link_index:];
		while ( link_index != -1):
			divcheck = newtarget.find("<div class=\"dd");
			first = newtarget.find("\"", divcheck);
			last = newtarget.find("\"", first+1);
			condition = newtarget.find("Sr", first, last);
			newtarget = newtarget[first:];
			if (condition != -1):	
				prebegin = newtarget.find("<a");
				begin =	newtarget.find( "href=\"", prebegin);
				end = newtarget.find("\"", begin+6);
				li.append( newtarget[begin+6:end] );
				count = count + 1;
				newtarget = newtarget[end:];
			link_index = newtarget.find("<li id");
			newtarget = newtarget[link_index:];
	return li;
		

def getLinks(enum, query):
	return HTML2Links(enum, queryforHTML(enum, query));


def randomize(array):
	#shuffle(array)
	arr = {}
	arr['A'] = array[0]
	arr['B'] = array[1]
	arr['C'] = array[2]
	return arr	

def score(links, real_link):
	
	for link in links[:7]:
		found = link.find(real_link)
		found2 = real_link.find(link)
		if found != -1 or found2 != -1:
			return found
		else:	
			return 7;
