#!/bin/bash

NOW=$(date +"%F--%T")
cookiejar="cookies/hxiao.cjar"
url="http://stackoverflow.com"

userpage=$(curl -b $cookiejar -c $cookiejar $url)
nobodypage=$(curl $url)

if [  "$1" == "test" ]; then
    echo "test tag python count"
    echo $userpage | ./page2json |  ./counttag python
    echo $nobodypage | ./page2json | ./counttag python
else
    echo $userpage | ./page2json > "data/hxiao/$NOW.json"
    echo $nobodypage | ./page2json > "data/nobody/$NOW.json"
fi


