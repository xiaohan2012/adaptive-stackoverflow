#! /bin/python

from util import merge_qs
if __name__ == '__main__':
    import sys, os
    src = sys.argv[1]
    dest = sys.argv[2]

    from simplejson import load, dump
    from codecs import open
    
    src_lst = load(open(src, "r", "utf8"))
    
    if not os.path.exists(dest):
        dest_lst = []
    else:
        dest_lst = load(open(dest, "r", "utf8"))


    dump(merge_qs(src_lst, dest_lst), open(dest, "w", 'utf8'))
    