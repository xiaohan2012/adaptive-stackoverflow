#!/bin/bash

NOW=$(date +"%F--%T")

./crawl.sh | python page2json.py > "data/hxiao/$NOW.json"

curl http://stackoverflow.com | python page2json.py > "data/nobody/$NOW.json"

