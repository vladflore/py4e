# write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py. The program will prompt for a URL,
# read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data,
# compute the sum of the numbers in the file.
#
# We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the
# other is the actual data you need to process for the assignment.
#
# Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_330795.xml (Sum ends with 62)

import ssl
import urllib.request
import xml.etree.ElementTree as ET

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
if len(url) < 1: url = "http://py4e-data.dr-chuck.net/comments_330795.xml"

data = urllib.request.urlopen(url, context=ctx).read()

# print('Retrieved', len(data), 'characters')
# print(data.decode())
tree = ET.fromstring(data)

counts = tree.findall('.//count')
s = 0
for tag in counts:
    s = s + int(tag.text)
print(s)
