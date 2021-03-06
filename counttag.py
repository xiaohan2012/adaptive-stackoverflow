#! /usr/bin/python2.7

from simplejson import loads, dumps

def count_tag(qs, tag):
    """
    >>> qs = [{"tags": ['a', 'b']}, {"tags": ['a']}]
    >>> print count_tag(qs, 'a')
    2
    >>> print count_tag(qs, 'b')
    1
    """
    return len( [q for q in qs if tag in q["tags"]] )

def count_tag_shell():
    import sys
    content = sys.stdin.read()
    tag = sys.argv[1]

    from simplejson import loads
    print count_tag(loads(content), tag)

def tag_freq(qs):
    """
    >>> from util import loadjson
    >>> qs = loadjson("qlist.hxiao")
    >>> freq = tag_freq(qs)
    >>> freq['python']
    22
    """
    from collections import Counter
    return Counter([tag for q in qs for tag in q["tags"]])

def test():
    import doctest
    doctest.testmod()
    
if __name__ == '__main__':
    test()

if __name__ == '__main__':
    count_tag_shell()
    #test()
