

##################################################################################################
# description:  python uniq sort
# raw_url:      https://gist.githubusercontent.com/mrkafk/a936f8e02c5c701ede283b322e86b96a/raw/af555a5892f285e0ffb075b57d3c108fa579d3d1/find_dissimilar_packages.py
# filename:     find_dissimilar_packages.py


def uniq_sort(lst):
    lst = list(set(lst))
    lst.sort()
    return lst

                