__author__ = 'ethan'

import glob
import os.path
import sys
from . import indexShare


if len(sys.argv) > 1:
    target_dir = os.path.normpath(os.path.expanduser(os.path.expandvars(sys.argv[1])))
    use_unicode = bool(len(sys.argv) > 2 and sys.argv[2] == "unicode=True")

    glob_pat = os.path.join(target_dir, "*.html")
    html_files = glob.glob(glob_pat)
    index_fp = os.path.join(target_dir, "index.html")
    try:
        html_files.remove(index_fp)
        my_template = indexShare.GlobalHTML(index_fp, u=use_unicode)

        for f in html_files:
            result = my_template.apply(f)
            print "Updated", str(len(result)), "parts of", os.path.basename(f), ":"
            for i, v in enumerate(result):
                print str(i), "\t", v

    except ValueError:
        sys.exit(str(index_fp + " not found. Aborting."))

else:
    print "Usage:  ", sys.argv[0], "\"[SITE ROOT FOLDER]\"[ unicode=True]\n"