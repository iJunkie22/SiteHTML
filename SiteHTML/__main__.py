__author__ = 'ethan'

import sys

import runners


def run(arg_list):
    if len(arg_list) > 1 or __name__ != "__main__":
        parser = runners.SiteLocation()
        parser.parse(arg_list)
        parser.build_site()

    else:
        print "Usage:  ", arg_list[0], "\"[SITE ROOT FOLDER]\"[options]\n"

if __name__ == "__main__":
    run(sys.argv)
