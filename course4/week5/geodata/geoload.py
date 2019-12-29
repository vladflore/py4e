# Retrieving GEOData Download the code from http://www.py4e.com/code3/geodata.zip - then unzip the file and edit
# where.data to add an address nearby where you live - don't reveal where you live. Then run the geoload.py to lookup
# all of the entries in where.data (including the new one) and produce the geodata.sqlite. Then run geodump.py to
# read the database and produce where.js. You can run the programs and then scroll back to take your screen shots
# when the program finishes. Then open where.html to visualize the map. Take screen shots as described below. Make
# sure that your added location shows in all three of your screen shots.
#
# This is a relatively simple assignment. Don't take off points for little mistakes. If they seem to have done the
# assignment give them full credit. Feel free to make suggestions if there are small mistakes. Please keep your
# comments positive and useful. If you do not take grading seriously, the instructors may delete your response and
# you will lose points.


import json
import sqlite3
import ssl
import time
import urllib.parse
import urllib.request

# api_key = False
# If you have a Google Places API key, enter it here
api_key = 'AIzaSyDgc55HcAuYiURG_gFhWnBGMVORT2uJTIM'

if api_key is False:
    api_key = 42
    serviceurl = "http://py4e-data.dr-chuck.net/json?"
else:
    serviceurl = "https://maps.googleapis.com/maps/api/geocode/json?"

# Additional detail for urllib
# http.client.HTTPConnection.debuglevel = 1

conn = sqlite3.connect('geodata_assignment.sqlite')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)''')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

fh = open("where.data")
count = 0
for line in fh:
    # if count > 200:
    #     print('Retrieved 200 locations, restart to retrieve more')
    #     break

    address = line.strip()
    print('')
    cur.execute("SELECT geodata FROM Locations WHERE address= ?",
                (memoryview(address.encode()),))

    try:
        data = cur.fetchone()[0]
        print("Found in database ", address)
        continue
    except:
        pass

    parms = dict()
    parms["address"] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))
    count = count + 1

    try:
        js = json.loads(data)
    except:
        print(data)  # We print in case unicode causes an error
        continue

    if 'status' not in js or (js['status'] != 'OK' and js['status'] != 'ZERO_RESULTS'):
        print('==== Failure To Retrieve ====')
        print(data)
        break

    cur.execute('''INSERT INTO Locations (address, geodata)
            VALUES ( ?, ? )''', (memoryview(address.encode()), memoryview(data.encode())))
    conn.commit()
    if count % 10 == 0:
        print('Pausing for a bit...')
        time.sleep(5)

print("Run geodump.py to read the data from the database so you can vizualize it on a map.")
