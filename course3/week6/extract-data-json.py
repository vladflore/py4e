# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py. The
# program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment
# counts from the JSON data, compute the sum of the numbers in the file and enter the sum below: We provide two files
# for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual
# data you need to process for the assignment.
#
# Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553) Actual data:
# http://py4e-data.dr-chuck.net/comments_330796.json (Sum ends with 66) The closest sample code that shows how to
# parse JSON and extract a list is json2.py. You might also want to look at geoxml.py to see how to prompt for a URL
# and retrieve data from a URL.

import json
import ssl
import urllib.request

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
if len(url) < 1: url = "http://py4e-data.dr-chuck.net/comments_330796.json"
# context is not needed because the data source link is NOT https
data = urllib.request.urlopen(url, context=ctx).read()
json_data = json.loads(data)
comments = json_data['comments']
s = 0
for comment in comments:
    s = s + int(comment['count'])
print(s)
