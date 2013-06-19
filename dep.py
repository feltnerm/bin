#!/usr/bin/env python

import sys
import urllib2
urllib2.urlopen("http://example.com/foo/bar").read()

# url
# @TODO (mark): github urls
DEPENDENCIES = (
    ('git-wtf', 'https://raw.github.com/michaelklishin/git-wtf/master/git-wtf'),
    )

def parse_url(url):
    return url

def main(argv=None):
    
    for name, url in DEPENDENCIES:
        print("""
        > %s 
        %s""" % (name, url))
        content = urllib2.urlopen(url).readlines()
        with open(name, 'w') as fil:
            fil.writelines(content)


    return 0 # success

if __name__ == '__main__':
    status = main()
    sys.exit(status)


