from simplejson import load
from codecs import open

def loadjson(path):
    """
    >>> lst = loadjson("qlist.hxiao")
    >>> print len(lst)
    90
    """
    return load(open("data/" + path + ".json", "r", "utf8"))
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()