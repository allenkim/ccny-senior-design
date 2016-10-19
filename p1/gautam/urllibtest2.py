import re;
import urllib.request;

response = urllib.request.urlopen('https://search.yahoo.com/search?p=python');
target = open('yahoo.html', 'w');
targetstring = response.read().decode("latin-1");

target.write(targetstring);

li = [];
count = 0;

# Isolate Search Queries
start = targetstring.find("<ol class=\"mb-15 reg searchCenterMiddle\">");
#print( start );
end = targetstring.find("</ol>", start);
#print( end );

# Cut out rest
newtarget = targetstring[start:end+4];
link_index = newtarget.find("<li id");
newtarget = newtarget[link_index:];
#print( link_index );
while ( link_index != -1):
	#print( newtarget ); 
	divcheck = newtarget.find("<div class=\"dd");
	first = newtarget.find("\"", divcheck);
	last = newtarget.find("\"", first+1);
	condition = newtarget.find("Sr", first, last);
	newtarget = newtarget[first:];
	#print( condition );
	if (condition != -1):	
		#print( newtarget );
		prebegin = newtarget.find("<a");
		#print( prebegin );
		begin =	newtarget.find( "href=\"", prebegin);
		#print( begin );
		end = newtarget.find("\"", begin+6);
		#print( end );
		li.append( newtarget[begin+6:end] );
		count = count + 1;
		newtarget = newtarget[end:];
	link_index = newtarget.find("<li id");
	newtarget = newtarget[link_index:];
# Print out lists
print( li );

