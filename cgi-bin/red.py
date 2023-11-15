#!/usr/bin/env python

import codecs
from db import Db
from process_json import loader
import sys

# How to do glob('reddit_.mp4') on the F drive?



def render(postings, files):
    """
    Render the page.
    postings - list of postings
    files - list of already processed files
    """
    print(
    """\
Content-Type: text/html

<!DOCTYPE html>
<html lang="en">
<body>
""")
    for posting in postings:
        title = codecs.encode(posting['title'], errors='ignore').decode('utf-8', errors='ignore')
        title = ''.join([char for char in title if ord(char)<128])
        url = posting['url']
        if '3bvyb1' in url:
            sys.stderr.write(f'{url=}\n')
        file = extract_name(url).lower()
        if file in files:
            sys.stderr.write(f'found {file}\n')
        print(f"""
<p>
  <a href="{url}"
     target="_blank">
     {title}
  </a>
</p>
""")
    print("""
</body>
</html>""")

def main():
    """
    Top level fuction
    """
    postings = loader('../../../../tmp/fb.txt')
    code_db = Db('F:/N/O/SPELLSNO/IMAGES/xxxbunker/CODE/example.db')

    sql = "SELECT lower(filename) FROM videos WHERE filename LIKE 'reddit_%' ORDER BY 1"
    files = [extract_name(row[0])
             for row in code_db.execute(sql)]
    render(postings, files)
    sys.stderr.write('Done\n')


def extract_name(url):
    """
    Extract a name from a URL like this:
    https://i.redd.it/2gw5n9u3bvyb1.gif
    """
    try:
        if url.startswith('reddit_'):
            url = url[7:]
        if '/' in url:
            ret = url.rsplit('/', maxsplit=1)[1].rsplit('.', maxsplit=1)[0]
        else:
            ret = url.rsplit('.', maxsplit=1)[0]
        if '3bvyb1' in url:
            sys.stderr.write(f'{url=}, {ret=}\n')
        return ret
    except:
        sys.stderr.write(f'Got an error with {url=}\n')
        raise

main()
