#!/bin/bash

# while read line
# do
#     echo $line
#     args+=" -H  \"$line\"";
# done < headers/hxiao

# cookie=$(cat cookies/hxiao)

# cmd="curl -c cookie/hxiao.cjar http://stackoverflow.com"

# echo $(eval "$cmd")

curl -v -b cookies/hxiao.cjar -c cookies/hxiao.cjar http://stackoverflow.com | grep python | wc -l
curl -v http://stackoverflow.com | grep python | wc -l


