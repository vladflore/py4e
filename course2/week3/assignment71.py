# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
fcontent = fh.read()
print(fcontent.upper().rstrip())
