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
    Starting point.
    """
    with open(args.json_filename) as json_file:
        data = json.load(json_file)
    
    medias = []
    for chunk in data['data']['children']:
        media = {}
        child = chunk['data']
        if child['media']:
            html = child['media']['oembed']['html']
            url = html.split('"')[1]
        else:
            url = f'https://www.reddit.com{child["permalink"]}'
        title = child['title']
        created_utc = datetime.utcfromtimestamp(int(child['created_utc']))
        score = child['score']
        subreddit = child['subreddit']
        #print(f'{url=}, {title=}, {created_utc=}, {score=}, {subreddit=}')
        media['url'] = url
        media['title'] = title
        media['created_utc'] = created_utc
        media['score'] = score
        media['subreddit'] = subreddit
        medias.append(media)
    return sorted(medias, key=lambda x: x['created_utc'], reverse=True)

if __name__ == '__main__':
    sys.exit(main(build_parser().parse_args()))
