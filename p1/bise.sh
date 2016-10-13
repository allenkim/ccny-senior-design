#!/bin/bash

read -p "Enter your search term: " searchterm

searchterm=$(echo $searchterm | sed -e 's/\ /+/g')

lynx -dump http://www.bing.com/search?q=$searchterm&qs=n&form=QBLH&pq=python&sc=0-0&sp=-1&sk=&cvid=4D48C02756CF4F0CB02ECE88E7AF3924 | less 
