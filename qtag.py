
from collections import Counter

def tagfreq(lst):
    """
    >>> f = tagfreq([{"tags": ["a", "b", "c"]}, {"tags": ["a","b"]}, {"tags": ["a"]}])
    >>> f["a"]
    3
    >>> f["b"]
    2
    >>> f["c"]
    1
    """
    return Counter([tag for tags in map(lambda q: q["tags"], lst) for tag in tags])

def tagset(lst):
    """
    >>> f = tagset([{"tags": ["a", "b", "c"]}, {"tags": ["a","b"]}, {"tags": ["a"]}])
    >>> sorted(list(f))
    ['a', 'b', 'c']
    """
    return set([tag for tags in map(lambda q: q["tags"], lst) for tag in tags])

def test():
    import doctest
    doctest.testmod()

def main():
    pass
    
if __name__ == '__main__':
    test()