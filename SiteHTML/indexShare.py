__author__ = 'ethan'

import re
import cStringIO
import StringIO
import sys


class UndefinedGlobalError(KeyError):
    def __init__(self, target_fp, line_number, global_key):
        sys.stderr.write('<%s> Line %s :: \'%s\' not defined in index.html\n' % (target_fp, line_number, global_key))
        pass


class NestedGlobalError(Exception):
    def __init__(self, target_fp, line_number, key1, key2):
        args = (target_fp, line_number, key1, key2)
        self.file_path = args[0]
        self.message = '<%s> Line %s :: \'%s\' overlaps \'%s\'\n' % args
        sys.stderr.write(self.message)
        pass


class GlobalHTML(object):
    globals_pat = re.compile('^\s*<!--\s(?P<status>Begin|End)\sGlobal\s(?P<key>[A-Za-z ]+)\s-->$')

    def __init__(self, index_fp, u=False):
        self.globals_dict = {}
        self._requires_unicode = u

        index_fd = open(index_fp, 'r')

        capturing = None
        for line in index_fd:
            mat = self.globals_pat.match(line)
            if mat:
                assert mat.groupdict()['status'] in ["Begin", "End"]
                if mat.groupdict()['status'] == "Begin":
                    capturing = LineBuffer(mat.groupdict()['key'], u=self._requires_unicode)
                else:
                    # Probably End
                    assert mat.groupdict()['status'] == "End"
                    k, v = capturing.yield_value()
                    self.globals_dict[k] = v
                    del capturing
                    capturing = None
            elif capturing:
                capturing.capture(line)

        index_fd.close()

    def apply(self, target_fp):
        new_file_buf = cStringIO.StringIO() if not self._requires_unicode else StringIO.StringIO()
        should_yield = True
        target_fd = open(target_fp, 'r+w')
        applied_keys = []
        g_key = None

        try:
            for i, line in enumerate(target_fd):
                mat = self.globals_pat.match(line)
                if mat:
                    mat_dict = mat.groupdict()
                    # Is either the Begin or End
                    new_file_buf.write(line)
                    assert mat_dict['status'] in ["Begin", "End"]

                    if mat_dict['status'] == "Begin":
                        g_key = mat_dict['key']
                        should_yield = False

                        try:
                            new_file_buf.write(self.globals_dict[g_key])
                            applied_keys.append(g_key)

                        except KeyError, e:
                            UndefinedGlobalError(target_fp, i, e)
                            # Global not defined in index.html
                            pass

                    else:
                        # Probably matches End Global
                        if g_key != mat_dict['key']:
                            raise NestedGlobalError(target_fp, i, mat_dict['key'], g_key)
                        # Exiting the lines owned by global
                        should_yield = True

                elif should_yield:
                    # Line does not wrap or contain global lines
                    new_file_buf.write(line)

            target_fd.seek(0)
            target_fd.write(new_file_buf.getvalue())
            target_fd.truncate()

        except NestedGlobalError, e:
            sys.stderr.write('Reverting \'%s\'\n\n' % e.file_path)
            applied_keys = []

        finally:
            target_fd.close()
            new_file_buf.close()

        return applied_keys


class LineBuffer:
    def __init__(self, key_name, u=False):
        self.key_name = key_name
        self.line_buf = cStringIO.StringIO() if not u else StringIO.StringIO()

    def capture(self, line):
        self.line_buf.write(line)

    def yield_value(self):
        new_str = self.line_buf.getvalue()
        self.line_buf.close()
        return self.key_name, new_str
