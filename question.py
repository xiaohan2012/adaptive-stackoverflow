#! /bin/python

from pyquery import PyQuery as pq

def parse_question_page(doc, url):
    """
    >>> q = parse_question_page(open("data/testquestion.html").read(), \
    "http://stackoverflow.com/questions/384284/how-do-i-rename-an-open-file-in-emacs")
    >>> q["title"]
    'How do I rename an open file in Emacs?'
    >>> q["url"]
    'http://stackoverflow.com/questions/384284/how-do-i-rename-an-open-file-in-emacs'
    >>> q["tags"]
    ['emacs']
    >>> len(q["related-links"])
    10
    >>> q["related-links"][0]
    '/questions/151945/how-do-i-control-how-emacs-makes-backup-files'
    """
    doc = pq(doc)
    return {
        "title": doc.find("#question-header h1 a").text(),
        "url": url,
        "body": doc.find(".question .post-text").html(),
        "tags": map(lambda a: pq(a).text(), doc.find(".post-taglist a")),
        "related-links": map(lambda s: pq(s).find("a.question-hyperlink").attr("href"), doc.find(".sidebar-related .spacer"))
    }

def test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    test()
    print parse_question_page(open("data/testquestion.html").read(), "fe")