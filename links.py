from simplejson import loads, load
from question import parse_question_page

def indexpage_links(qs):
    """
    >>> lks = indexpage_links(load(open("data/testqs.json")))
    >>> print lks[0]
    /questions/19198839/how-to-add-text-link-inside-a-div-using-jquery
    >>> print len(lks)
    90
    """
    return map(lambda q: q["url"], qs)
    
def indexpage_links_shell():
    import sys
    content = sys.stdin.read()
    return getlinks(loads(content))
        
def test():
    import doctest
    doctest.testmod()
    
if __name__ == '__main__':
    test()