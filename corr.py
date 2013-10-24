#! /bin/python

from util import loadjson
utag_freq = loadjson("tag-freq")
utag_freq = dict(map(lambda i: (i["name"], i["freq"]), utag_freq))

from counttag import tag_freq

qtag_freq = tag_freq(loadjson("hxiao/merged"))

shared_tags = set(utag_freq.keys()).intersection(set(qtag_freq.keys()))

pairs = [(utag_freq[tag], qtag_freq[tag]) for tag in shared_tags]

print pairs

from numpy import corrcoef

x,y = zip(*pairs)

print corrcoef(x,y)
