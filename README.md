# red
Reddit viewer

Stored already view in sqlite database.

Notes:

Start the server with:
  python -m http.server --cgi

Run hello.py in cgi-bin with this in a browser:
  http://localhost:8000/cgi-bin/hello.py
it displays 'Hello, World!'
  http://localhost:8000/cgi-bin/red.py


TODO::
use glob('reddit_*.mp4') to generate a list of reddit files, convered to lower case, removing 'reddit_' and file extensions
When setting up a file for display, convert the last part of the url to lower case.
Use last part in file_list to see if I already have downloaded it, and don't display.

 os.chdir('F:/N/O/SPELLSNO/IMAGES/xxxbunker')
 
