#!/usr/bin/env python
"""
Get a field from the reddit JSON file.
"""


import argparse
import sys
import json


def build_parser():
    """
    Collect command line arguments.
    """
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    # j['data']['children'][0]['data']['title']
    parser.add_argument('-i', '--iterator',
                        default='data.children',
                        help='The field in the JSON to iterate on. '
                        ' Default: %(default)s.')
    parser.add_argument('-f', '--field',
                        default='data.title',
                        help='The field to extract the required data. '
                        ' Default: %(default)s.')
    parser.add_argument('filename',
                        help='The filename of the JSON file.')
    return parser


def main(args):
    """
    main
    """
    with open(args.filename) as jin:
        json_data = json.load(jin)
    for field in args.iterator.split('.'):
        json_data = json_data[field]
    for data in json_data:
        value = data
        for field in args.field.split('.'):
            value = value[field]
        print(value)

if __name__ == '__main__':
    sys.exit(main(build_parser().parse_args()))
