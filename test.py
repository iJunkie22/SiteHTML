import SiteHTML
from SiteHTML.tests import tempsite


__author__ = 'ethan'

test1 = tempsite.TestSite()
print(test1.t_d)
# test1.cleanup()
SiteHTML.run([test1.t_d])
test1.cleanup(delete=True)
