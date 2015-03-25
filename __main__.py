__author__ = 'ethan'

import glob
import os.path
import sys
from . import indexShare


if len(sys.argv) > 1:
    target_dir = os.path.normpath(os.path.expanduser(os.path.expandvars(sys.argv[1])))
    glob_pat = os.path.join(target_dir, "*.html")
    html_files = glob.glob(glob_pat)
    my_template = None
    for f in html_files:
        if os.path.basename(f) == "index.html":
            my_template = indexShare.GlobalHTML(f)
            html_files.remove(f)
    if my_template:
        for f in html_files:
            result = my_template.apply(f)
            print "Updated", str(len(result)), "parts of", os.path.basename(f), ":"
            for i, v in enumerate(result):
                print str(i), "\t", v
else:
    print "Usage:  ", sys.argv[0], "[SITE ROOT FOLDER]\n"