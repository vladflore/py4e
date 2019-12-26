# The program will use urllib to read the HTML from the data files below, and parse the data, extracting numbers and
# compute the sum of the numbers in the file. Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_330793.html (Sum ends with 50)

import ssl
from urllib.request import urlopen

from bs4 import BeautifulSoup

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
if len(url) < 1: url = "http://py4e-data.dr-chuck.net/comments_330793.html"
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the span tags
tags = soup('span')
s = 0
for tag in tags:
    s = s + int(tag.contents[0])
print(s)
