__author__ = 'ethan'

import re
import cStringIO
import StringIO


class GlobalHTML(object):
    def __init__(self, index_fp, u=False):
        self.globals_pat = re.compile('^\s*<!--\s(?P<status>Begin|End)\sGlobal\s(?P<key>[A-Za-z ]+)\s-->$')
        self.globals_dict = dict()
        self._requires_unicode = u

        index_fd = open(index_fp, 'r')

        capturing = None
        for line in index_fd:
            mat = self.globals_pat.match(line)
            if mat:
                if mat.groupdict()['status'] == "Begin":
                    capturing = LineBuffer(mat.groupdict()['key'], u=self._requires_unicode)
                else:
                    # Probably End
                    k, v = capturing.yield_value()
                    self.globals_dict[k] = v
                    del capturing
                    capturing = None
            elif capturing:
                capturing.capture(line)

        index_fd.close()

    def apply(self, target_fp):
        if not self._requires_unicode:
            new_file_buf = cStringIO.StringIO()
        else:
            new_file_buf = StringIO.StringIO()

        should_yield = True
        target_fd = open(target_fp, 'r+w')
        applied_keys = []

        try:
            for line in target_fd:
                mat = self.globals_pat.match(line)
                if mat:
                    if mat.groupdict()['status'] == "Begin":
                        should_yield = False
                        new_file_buf.write(line)
                        new_file_buf.write(self.globals_dict[mat.groupdict()['key']])
                        applied_keys.append(mat.groupdict()['key'])

                    else:
                        # Probably End
                        should_yield = True

                if should_yield:
                    new_file_buf.write(line)
        finally:
            target_fd.seek(0)
            target_fd.write(new_file_buf.getvalue())
            target_fd.truncate()
            target_fd.close()
            new_file_buf.close()

        return applied_keys


class LineBuffer:
    def __init__(self, key_name, u=False):
        self.key_name = key_name
        if not u:
            self.line_buf = cStringIO.StringIO()
        else:
            self.line_buf = StringIO.StringIO()

    def capture(self, line):
        self.line_buf.write(line)

    def yield_value(self):
        new_str = self.line_buf.getvalue()
        self.line_buf.close()
        return self.key_name, new_str
