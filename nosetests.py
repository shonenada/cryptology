from __future__ import print_function
import os
import re


def _find(path, pattern, use_full_path=False):
    """Same as GNU find tool."""
    files = []
    if use_full_path:
        path = os.path.abspath(path)
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if re.match(pattern, filename):
                match_file_path = os.path.join(dirpath, filename)
                match_file_path = match_file_path.replace('\\', '/')
                files.append(match_file_path)
    return files


def tests():
    modules = " ".join(_find('./', r"^test[a-zA-Z0-9_]+\.(py)$"))
    os.system('nosetests %s' % modules)


tests()
