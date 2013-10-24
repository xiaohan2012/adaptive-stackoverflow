from simplejson import load, dumps

from codecs import open

def loadjson(path):
    """
    >>> lst = loadjson("qlist.hxiao")
    >>> print len(lst)
    90
    """
    return load(open("data/" + path + ".json", "r", "utf8"))

def getqs(string):
    """
    >>> qs = getqs(open("data/testpage.html", "r").read())
    >>> print len(qs)
    90
    >>> q = qs[0]
    >>> print q["title"]
    how to add text link inside a div using jquery?
    >>> print q["url"]
    /questions/19198839/how-to-add-text-link-inside-a-div-using-jquery
    >>> print q["tags"]
    ['javascript', 'jquery', 'div', 'href']
    >>> print q["ctime"]
    2013-10-05 14:32:24Z
    """

    from pyquery import PyQuery as pq
    
    def aux(q):
        q = pq(q)
        return {
            "url": q.find("a.question-hyperlink").eq(0).attr("href"),
            "title": q.find("a.question-hyperlink").eq(0).text(),
            "tags" : map(lambda t: pq(t).text(), q.find(".tags a.post-tag")),
            "ctime": q.find(".started span.relativetime").eq(0).attr("title"),
        }

    return map(aux, pq(string).find(".question-summary"))

def dump_qs():
    import sys
    
    content = sys.stdin.read()
    qs = getqs(content)

    print dumps(qs)

def test():
    import doctest
    doctest.testmod()
    
if __name__ == '__main__':
    test()
