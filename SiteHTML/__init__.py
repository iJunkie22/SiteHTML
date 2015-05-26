__author__ = 'ethan'
"""
######################################## SiteHTML ########################################
############################### USING FROM A PYTHON SCRIPT ###############################

To call SiteHTML from python instead of command line, follow the format:

import SiteHTML

SiteHTML.run(['DIRECTORY_PATH', '-q'])

###########################################################################################
###################################### VALID OPTIONS ######################################

-u, unicode=True        Stores text as unicode (rarely needed, slower)
-q, quiet=True          Disable printing of the result stats in command line

###########################################################################################
"""

from . import __main__


def run(args):
    __main__.run(args)

