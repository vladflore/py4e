# 7.2 Write a program that prompts for a file name, then opens that file and reads through the file,
# looking for lines of the form:
#     X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values
# and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
# when you are testing below enter mbox-short.txt as the file name.
# Use the file name mbox-short.txt as the file name

fname = input("Enter file name: ")
fh = open(fname)
search_str = "X-DSPAM-Confidence:"
val_count = 0
val_s = 0
for line in fh:
    if not line.startswith(search_str): continue
    val_start_pos = line.index(search_str) + len(search_str)
    val = line[val_start_pos:len(line)].rstrip()
    val_count = val_count + 1
    val_s = val_s + float(val)
print("Average spam confidence:", val_s / val_count)
