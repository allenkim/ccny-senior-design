#!/bin/bash

read -p "Enter your search term: " searchterm

searchterm=$(echo $searchterm | sed -e 's/\ /+/g')

lynx -dump https://search.yahoo.com/search?p=$searchterm&ei=UTF-8&fp=1&nojs=1 | less 
