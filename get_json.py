#!/usr/bin/env python
"""
Read JSON data from a specific subreddit.
Writes the formatted JSON to stdout.
"""


import argparse
import json
import sys
import urllib.request


def build_parser():
    """
    Collect command line arguments.
    """
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('subreddit',
                        help='The name of the subreddit. ')
    parser.add_argument('-t', '--timeframe',
                        choices=['hour', 'day', 'week', 'month', 'year', 'all'],
                        default='day',
                        help='Amount of time to look at. '
                        ' Default: %(default)s.')
    parser.add_argument('--limit',
                        default=100,
                        help='Limit on the number of postings to retrieve. '
                        ' Default: %(default)s.')

    parser.add_argument('-l', '--listing',
                        choices=['controversial', 'best', 'hot', 'new',
                                 'random', 'rising', 'top'],
                        default='new',
                        help='Sort articles according to this. '
                        ' Default: %(default)s.')

    return parser


def main(args):
    """
    Retrieve JSON data.
    """
    url = f'https://www.reddit.com/r/{args.subreddit}/' \
          f'{args.listing}.json?limit={args.limit}&t={args.timeframe}'
    fp = urllib.request.urlopen(url)
    json_bytes = fp.read()
    json_data = json.loads(json_bytes.decode("utf8", errors='ignore'))
    fp.close()
    sys.stdout.reconfigure(errors='ignore')
    print(json.dumps(json_data, sort_keys=True,
                     indent=4, separators=(',', ': ')))


if __name__ == '__main__':
    sys.exit(main(build_parser().parse_args()))
