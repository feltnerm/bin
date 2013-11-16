#!/usr/bin/env python

# Lil' python script to download other scripts and useful things.

# @TODO:
# * github urls

import os
import stat
import sys
import urlparse
import urllib2

DEPENDENCIES = (
    ('git-wtf', 'https://raw.github.com/michaelklishin/git-wtf/master/git-wtf')
  , ('leiningen', 'https://raw.github.com/technomancy/leiningen/stable/bin/lein')
  , ('prettyping', 'https://bitbucket.org/denilsonsa/small_scripts/raw/0c59d14ca5f1aac01447e28d81f5d5c433976348/prettyping.sh')
  , ('bash_colors', 'https://raw.github.com/maxtsepkov/bash_colors/master/bash_colors.sh')
  , ('z', 'https://raw.github.com/rupa/z/master/z.sh')
)

def chmod(file, mode):
    st = os.stat(name)
    os.chmod(name, st.st_mode | mode)

chmod_x = lambda file: chmod(file, stat.S_IEXEC)

def parse_url(url):
    u = urlparse.urlparse(url)

    if not u.scheme:
        if url.count('/') == 1 and len(url.split('/')) == 2:
            url = url.strip()
            url = "https://raw.github.com/" + url
            u = urlparse.urlparse(u)
    return urlparse.urlunparse(u)

def main(argv=None):

    for name, url in DEPENDENCIES:
        print("""> %s
                %s""" % (name, url))
        content = urllib2.urlopen(parse_url(url)).readlines()
        with open(name, 'w') as fil:
            fil.writelines(content)
        chmod_x(name)

    return 0 # success

if __name__ == '__main__':
    status = main()
    sys.exit(status)


