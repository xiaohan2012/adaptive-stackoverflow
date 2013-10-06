#!/bin/bash

NOW=$(date +"%F--%T")

./crawl.sh | ./page2json > "data/hxiao/$NOW.json"

curl http://stackoverflow.com | ./page2json > "data/nobody/$NOW.json"

