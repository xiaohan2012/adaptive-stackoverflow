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
    html to json
    
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
    """stdin string to json"""
    import sys
    
    content = sys.stdin.read()
    qs = getqs(content)

    print dumps(qs)

def merge_qs(l1, l2):
    """
    merge two question lists
    
    >>> src_list = [{"url": "/questions/19559333/apply-non-standard-css-style-properties-at-run-time-using-javascript", "tags": ["javascript"], "ctime": "2013-10-24 07:14:38Z", "title": "Apply non-standard css style properties at run time using JavaScript"}, {"url": "/questions/19558567/ganglia-web-hosts-up-and-hosts-down-issue", "tags": ["ganglia"], "ctime": "2013-10-24 07:14:24Z", "title": "Ganglia Web - Hosts Up and Hosts Down Issue"}]
    >>> dest_list =  [{"url": "/questions/19558567/ganglia-web-hosts-up-and-hosts-down-issue", "tags": ["ganglia"], "ctime": "2013-10-24 07:14:24Z", "title": "Ganglia Web - Hosts Up and Hosts Down Issue"}, {"url": "/questions/19559191/getting-tag-names-with-beautifulsoup", "tags": ["python", "beautifulsoup"], "ctime": "2013-10-24 07:14:07Z", "title": "Getting Tag Names with BeautifulSoup"}]
    >>> lst = merge_qs(src_list, dest_list)
    >>> len(lst)
    3
    """
    import re
    ext_id = lambda q: re.findall(r"/.*/(\d+)/.*", q["url"])[0]
    ids1 = set(map(ext_id, l1))
    ids2 = set(map(ext_id, l2))
    ids = ids1.union(ids2)
    qlist = []
    for l in l1+l2:
        id = ext_id(l)
        if id in ids:
            qlist.append(l)
            ids = ids - {id}
    return qlist
    
def test():
    import doctest
    doctest.testmod()
    
if __name__ == '__main__':
    test()
