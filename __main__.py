__author__ = 'ethan'

import glob
import os.path
import sys
from . import indexShare


if len(sys.argv) > 1:
    target_dir = os.path.normpath(os.path.expanduser(os.path.expandvars(sys.argv[1])))
    use_unicode = False
    if len(sys.argv) > 2:
        if sys.argv[2] == "unicode=True":
            use_unicode = True

    glob_pat = os.path.join(target_dir, "*.html")
    html_files = glob.glob(glob_pat)
    my_template = None
    for f in html_files:
        if os.path.basename(f) == "index.html":
            my_template = indexShare.GlobalHTML(f, u=use_unicode)
            html_files.remove(f)
            break
    if my_template:
        for f in html_files:
            result = my_template.apply(f)
            print "Updated", str(len(result)), "parts of", os.path.basename(f), ":"
            for i, v in enumerate(result):
                print str(i), "\t", v
else:
    print "Usage:  ", sys.argv[0], "\"[SITE ROOT FOLDER]\"[ unicode=True]\n"