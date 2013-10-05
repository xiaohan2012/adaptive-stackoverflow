#!/bin/bash

while read line
do
    echo $line
    args+=" -H  \"$line\"";
done < headers/hxiao

cookie=$(cat cookies/hxiao)

cmd="curl $args -b '$cookie' http://stackoverflow.com"

echo $(eval "$cmd")

