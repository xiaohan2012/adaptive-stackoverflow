from util import loadjson
from qtag import tagfreq, tagset

if __name__ == '__main__':
    hx_lst = loadjson("qlist.hxiao")
    nb_lst = loadjson("qlist.nobody")

    hx_freq, nb_freq = tagfreq(hx_lst), tagfreq(nb_lst)
    hx_set, nb_set = tagset(hx_lst), tagset(nb_lst)

    print sorted(list(hx_set))
    print sorted(list(nb_set))
    print hx_set.intersection(nb_set)