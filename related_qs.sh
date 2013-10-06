#! /bin/bash

url=$1

curl $url | ./related_qs.py $url
