#!/bin/bash

read -p "Enter your search term: " searchterm

searchterm=$(echo $searchterm | sed -e 's/\ /+/g')

lynx -dump http://google.com/search?q=$searchterm | less 
