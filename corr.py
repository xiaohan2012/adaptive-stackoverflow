#! /bin/python
from util import loadjson
from numpy import corrcoef
from counttag import tag_freq

utag_freq = loadjson("tag-freq")
utag_freq = dict(map(lambda i: (i["name"], i["freq"]), utag_freq))

uqtag_freq = tag_freq(loadjson("hxiao/merged"))
nqtag_freq = tag_freq(loadjson("nobody/merged"))


ushared_tags = set(utag_freq.keys()).intersection(set(uqtag_freq.keys()))
nshared_tags = set(utag_freq.keys()).intersection(set(nqtag_freq.keys()))

upairs = [(utag_freq[tag], uqtag_freq[tag]) for tag in ushared_tags]
npairs = [(utag_freq[tag], nqtag_freq[tag]) for tag in nshared_tags]

x,uy = zip(*upairs)
print corrcoef(x,uy)

x,ny = zip(*npairs)
print corrcoef(x,ny)

#recent tags
rtag_freq = loadjson("recent-tag-freq")
rtag_freq = dict(map(lambda i: (i["name"], i["freq"]), rtag_freq))

shared_tags = set(rtag_freq.keys()).intersection(set(uqtag_freq.keys()))

pairs = [(rtag_freq[tag], uqtag_freq[tag]) for tag in shared_tags]

x,y = zip(*pairs)

print corrcoef(x,y)