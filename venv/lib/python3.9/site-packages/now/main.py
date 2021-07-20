import os
import sys
import argparse
from datetime import datetime
from now import config, exceptions


CONFIG_PATH = os.path.join("~", ".nowrc")
OUTPUT_PATH = os.path.join("~", ".now.txt")


def make_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('message', nargs='*')
    return parser


def parse_arguments(args):
    parser = make_parser()
    parsed, extra = parser.parse_known_args(args)
    normal = " ".join(parsed.message) if parsed.message else ""
    dashed = " ".join(extra) if extra else ""
    if normal and dashed:
        message = "{0} {1}".format(normal, dashed)
    else:
        message = normal + dashed
    del parsed.message
    return message, parsed


def get_output_file(env):
    path = env.get('NOWFILE', None)
    if path:
        path = os.path.expanduser(path)
        abspath = os.path.abspath(path)
        if path != abspath:
            raise exceptions.BadConfig(
                "if specified, NOW_FILE env variable must be "
                "an absolute path.")
    else:
        nowrc = config.Nowrc.from_file(os.path.expanduser(CONFIG_PATH))
        path = nowrc['write_to']
        if path:
            path = os.path.expanduser(path)
            abspath = os.path.abspath(path)
            if path != abspath:
                raise exceptions.BadConfig(
                    "if specified, write_to parameter in .nowrc must be "
                    "an absolute path.")
    if not path:
        path = os.path.expanduser(OUTPUT_PATH)
    output = open(path, 'a+b')
    return output


def get_timestamp(utcnow=datetime.utcnow):
    return utcnow().strftime("%Y-%m-%d %H:%M:%S")


def _main(args, env, utcnow=datetime.utcnow):
    message, _ = parse_arguments(args)
    if not message:
        raise exceptions.NoMessage("you forgot to say what you're doing.")
    output = get_output_file(env)
    if output is None:
        raise exceptions.NoOutputFile("could not find an output file.")
    timestamp = get_timestamp(utcnow=utcnow)
    line = "{0} {1}".format(timestamp, message)
    with output:
        output.write(line.encode("utf-8"))
        output.write(b'\n')


def main():
    args = sys.argv[1:]
    env = os.environ.copy()
    try:
        _main(args, env)
        result = 0
    except exceptions.Error as error:
        formatted = "Error: {0}\n".format(error.message)
        sys.stderr.write(formatted)
        result = 1
    sys.exit(result)
