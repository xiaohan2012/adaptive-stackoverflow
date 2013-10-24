#! /bin/bash
path="$1"
merge_fp=$path/merged.json

files=$(ls $path/*)

for f in $files; do
    ./merge_qs.py $f $merge_fp
done

python -c "from simplejson import load; from codecs import open; print len(load(open('$merge_fp', 'r', 'utf8')))"
