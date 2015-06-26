__author__ = 'ethan'
import re
import os.path
import sys
import glob

import indexShare


def list_eq(l1, l2):
    try:
        assert len(l1) == len(l2)
        for x1, x2 in zip(l1, l2):
            assert x1 == x2
    except AssertionError:
        return False
    return True


def int_neq(x1, x2):
    return int(x1 != x2)


def int_eq(x1, x2):
    return int(x1 == x2)


class OptionParser(object):
    _bool_pat = re.compile('^(?P<key>[a-zA-Z]+)=(?P<value>(True|False))$')
    _posix_pat = re.compile('^\-([a-z]+)$', re.I)

    def __init__(self):
        self._use_unicode = False
        self._override_index = False
        self._quiet = False
        self._site_path = None
        self._globals_file = 'index.html'
        self._parsed = False

    @classmethod
    def opt_test(cls, test_str_list):
        result_dict = {}
        for test_str in test_str_list:
            try:
                for pm in cls._posix_pat.match(test_str).group(0).strip('-'):
                    result_dict[pm] = True
            except AttributeError:
                pass
            try:
                m_d = cls._bool_pat.match(test_str).groupdict()
                result_dict[m_d['key']] = bool(m_d['value'] == 'True')
            except AttributeError:
                pass
        return result_dict

    def parse(self, in_list=sys.argv):
        if list_eq(sys.argv, in_list):
            del in_list[0]

        mat_dict = self.opt_test(in_list)
        self._use_unicode = bool(mat_dict.get('u') or mat_dict.get('unicode'))
        self._quiet = bool(mat_dict.get('q') or mat_dict.get('quiet'))
        self._site_path = os.path.normpath(os.path.expanduser(os.path.expandvars(in_list[0])))
        self._parsed = True


class SiteLocation(OptionParser, object):
    def build_site(self):

        glob_pat = os.path.join(self._site_path, "*.html")
        html_files = glob.glob(glob_pat)
        index_fp = os.path.join(self._site_path, self._globals_file)
        try:
            html_files.remove(index_fp)
            my_template = indexShare.GlobalHTML(index_fp, u=self._use_unicode)

            for f in html_files:
                result = my_template.apply(f)
                if self._quiet:
                    continue
                print "Updated %s parts of %s:" % (str(len(result)), os.path.basename(f))
                print "".join(["%s\t%s\n" % (i, v) for i, v in enumerate(result)])

        except ValueError:
            sys.exit(str(index_fp + " not found. Aborting."))
