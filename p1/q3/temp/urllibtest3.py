import re;
import urllib.request;

headers={};
headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)';

request = urllib.request.Request('https://www.google.com/search?q=python', headers=headers);
response = urllib.request.urlopen( request );
target = open('google.html', 'w');
targetstring = response.read().decode("latin-1");

target.write(targetstring);

li = [];
count = 0;

link_index = targetstring.find("<div class=\"g\">");
newtarget = targetstring[link_index:];
while ( link_index != -1):
	#print( newtarget );
	prebegin = newtarget.find("<a");
	#print( prebegin );
	begin =	newtarget.find( "\"", prebegin);
	#print( begin );
	end = newtarget.find("&", begin+1);
	#print( end );
	li.append( newtarget[begin+8:end] );
	count = count + 1;
	newtarget = newtarget[end:];
	link_index = newtarget.find("<div class=\"g\">");
	newtarget = newtarget[link_index:];
# Print out lists
print( li ); 
