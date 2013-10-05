#!/bin/sh
while read line; do
  args="$args -H  '$line' ";
done

curl $args http://stackoverflow.com | grep python | wc -l
#echo "curl  $args http://stackoverflow.com" 
