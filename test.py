__author__ = 'ethan'

import SiteHTML
from SiteHTML.tests import tempsite

test1 = tempsite.TestSite()
print test1.t_d
# test1.cleanup()
SiteHTML.run([test1.t_d])
test1.cleanup(delete=True)
