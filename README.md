# red
Reddit viewer

Stored already view in sqlite database.

Notes:

Start the server with:
  cd ~/src/red
  python -m http.server --cgi

Run hello.py in cgi-bin with this in a browser:
  http://localhost:8000/cgi-bin/hello.py
it displays 'Hello, World!'

Run red.lpy in cgi-bin with this in a browser:
  http://localhost:8000/cgi-bin/red.py
It will display a list of titles as links. Click on the link to see an
  image or video.


TODO::
identifies duplicates. Need another DB or table to record those we have already viewed.
columns: id, file, ts, table name: viewed
--done--
use glob('reddit_*.mp4') to generate a list of reddit files, converted to lower case, removing 'reddit_' and file extensions
When setting up a file for display, convert the last part of the url to lower case.
Use last part in file_list to see if I already have downloaded it, and don't display.

 os.chdir('F:/N/O/SPELLSNO/IMAGES/xxxbunker')
-------------------------------------------------------------------------------
Load simple.html in a browser. Click the reddit link. After a few
seconds the image will appear.
-------------------------------------------------------------------------------
This is a useful guide to extracting reddit postings in JSON format

https://www.jcchouinard.com/documentation-on-reddit-apis-json/

This link:

https://www.reddit.com/r/python/top.json?limit=100&t=month

in a browser will display the JSON file in a raw or formatted manner.
Use this URL to display JSON data for FromBelowView

https://www.reddit.com/r/FromBelowView/top.json?limit=100&t=month

listing = 'top' # controversial, best, hot, new, random, rising, top
timeframe = 'month' #hour, day, week, month, year, all

The above URL uses a listing of top and a timeframe of month.
