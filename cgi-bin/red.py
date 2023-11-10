#!/usr/bin/env python

import codecs
from process_json import loader

# How to do glob('reddit_.mp4') on the F drive?

whole_list = loader('../../../../tmp/fb.txt')
posting = whole_list[0]
print(
    """\
Content-Type: text/html

<!DOCTYPE html>
<html lang="en">
<body>
""")
for posting in whole_list:
    title = codecs.encode(posting['title'], errors='ignore').decode('utf-8', errors='ignore')
    title = ''.join([char for char in title if ord(char)<128])
    url = posting['url']
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

