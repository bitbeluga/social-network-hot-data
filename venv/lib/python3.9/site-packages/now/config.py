"""Config file processing (for ~/.nowrc).
"""
import os
import sys
from collections import OrderedDict


if sys.version_info < (3, 3):
    FileNotFoundError = IOError


class InvalidConfigError(Exception):
    """Raised when there is an error during a .nowrc file parse.
    """
    def __init__(self, filename, errors):
        Exception.__init__(self)
        self.filename = filename
        self.errors = errors

    def __str__(self):
        return "errors in {0!r}, lines {1!r}".format(
            self.filename,
            list(tup[0] for tup in self.errors)
        )


class Nowrc(object):
    """Parsed representation of a .nowrc config file.
    """
    default_encoding = "utf-8"

    def __init__(self):
        self.encoding = self.default_encoding
        self.data = OrderedDict()

    def __getitem__(self, key):
        return self.data.get(key)

    @classmethod
    def from_file(cls, path):
        """Make a Nowrc instance from given file.
        """
        instance = cls()
        instance.read(path)
        return instance

    def read(self, path):
        """Read data from file into this Nowrc instance.
        """
        try:
            inp = open(path, 'rb')
        except FileNotFoundError as error:
            if error.errno != 2:
                raise
            return None
        parsing = parse_nowrc(inp)
        for key, value in parsing:
            if key in self.data:
                raise InvalidConfigError(
                    path, "duplicate declaration for {0}: {1!r} vs. {2!r}"
                    .format(key, self.data[key], value))
            self.data[key] = value
        parsing.close()

    def validate(self):
        write_to = self['write_to']
        if write_to:
            expanded = os.path.expanduser(write_to)
            if not expanded == os.path.abspath(expanded):
                pass

        pass


def extract_key_value(line):
    """Return key, value from given line if present, else return None.
    """
    segments = line.split("=", 1)
    if len(segments) < 2:
        return None
    key, value = segments
    value = value.strip()
    key = key.strip()
    value = value.strip()
    return key, value


def parse_nowrc(inp):
    """Iterator yielding key/value pairs from given stream.

    yields tuples of key, value.
    """
    errors = []
    with inp:
        for line_number, line in enumerate(inp):
            line = line.decode("utf-8")
            if not line.strip():
                continue
            kv_tuple = extract_key_value(line)
            if kv_tuple is None:
                errors.append((line_number, line))
                continue
            try:
                yield kv_tuple
            except GeneratorExit:
                break
    if errors:
        raise InvalidConfigError(inp.name, errors)
