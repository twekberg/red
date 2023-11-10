#!/usr/bin/env python
"""
Process a JSON file from reddit.

Example with file in /tmp:
  ./process_json.py ../../../../tmp/fb.txt
"""


import argparse
from datetime import datetime
import json
import sys
import re


def build_parser():
    """
    Collect command line arguments.
    """
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('json_filename',
                        help='The filename of the JSON file to process.')
    return parser


def main(args):
    """
    """
    return loader(args.json_filename)

def loader(json_filename):
    """
    Loads the JSON file
    Return a list of dicts by extracting key data from the JSON file.
    """
    with open(json_filename) as json_file:
        data = json.load(json_file)
    
    media_list = []
    for chunk in data['data']['children']:
        media = {}
        child = chunk['data']
        url = child['url']
        title = child['title']
        created_utc = datetime.utcfromtimestamp(int(child['created_utc']))
        score = child['score']
        subreddit = child['subreddit']
        media = dict(url=url,
                     title=title,
                     created_utc=created_utc,
                     score=score,
                     subreddit=subreddit)
        media_list.append(media)
    return sorted(media_list, key=lambda x: x['created_utc'], reverse=True)

if __name__ == '__main__':
    sys.exit(main(build_parser().parse_args()))
