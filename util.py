from simplejson import load
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
    """

    from pyquery import PyQuery as pq
    
    def aux(q):
        q = pq(q)
        return {
            "url": q.find("a.question-hyperlink").eq(0).attr("href"),
            "title": q.find("a.question-hyperlink").eq(0).text(),
            "tags" : map(lambda t: pq(t).text(), q.find(".tags a.post-tag"))
        }

    return map(aux, pq(string).find(".question-summary"))

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
    path = sys.argv[1]
    tag = sys.argv[2]

    from simplejson import loads
    print count_tag(load(open(path, "r")), tag)
    
def dump_qs():
    import sys
    from simplejson import dumps
    
    content = sys.stdin.read()
    qs = getqs(content)

    print dumps(qs)

def test():
    import doctest
    doctest.testmod()
    
if __name__ == '__main__':
    #test()
    count_tag_shell()