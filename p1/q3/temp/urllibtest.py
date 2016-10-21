import re;
import urllib.request;

response = urllib.request.urlopen('https://www.bing.com?q=python');
target = open('google.html', 'w');
targetstring = response.read().decode("latin-1");

target.write(targetstring);

li = [];
count = 0;

# Isolate Search Queries
start = targetstring.find("<ol id=\"b_results\" role=\"main\" aria-label=\"Search Results\">");
#print( start );
end = targetstring.find("</ol>");
#print( end );

# Cut out rest
newtarget = targetstring[start:end+4];
link_index = newtarget.find("<li class=\"b_algo\">");
newtarget = newtarget[link_index:];
while ( link_index != -1):
	#print( newtarget );
	prebegin = newtarget.find("<a");
	#print( prebegin );
	begin =	newtarget.find( "\"", prebegin);
	#print( begin );
	end = newtarget.find("\"", begin+1);
	#print( end );
	li.append( newtarget[begin+1:end] );
	count = count + 1;
	newtarget = newtarget[end:];
	link_index = newtarget.find("<li class=\"b_algo\">");
	newtarget = newtarget[link_index:];
# Print out lists
print( li ); 
