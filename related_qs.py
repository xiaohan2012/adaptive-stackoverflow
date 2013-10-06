#! /bin/python
from question import parse_question_page

prefix = "http://stackoverflow.com"

def question_related_links(q):
    """
    >>> q = parse_question_page(open("data/testquestion.html").read(), "a")
    >>> lks = question_related_links(q)
    >>> lks[0]
    'http://stackoverflow.com/questions/151945/how-do-i-control-how-emacs-makes-backup-files'
    """
    return map(lambda l: prefix + l, q['related-links'])
    
def question_related_links_shell():
    import sys
    content = sys.stdin.read()
    url = sys.argv[1]
    q = parse_question_page(content, url)
    for l in question_related_links(q):
        print l

if __name__ == '__main__':
    question_related_links_shell()