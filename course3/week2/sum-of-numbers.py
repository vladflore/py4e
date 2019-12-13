# assignment-sum-of-numbers.pdf
import re

file_name = input('Enter file name:')
if len(file_name) < 1:
    file_name = "sample-data.txt"
data_file = open(file_name)
numbers = list()
for line in data_file:
    numbers.extend(re.findall("[0-9]+", line))
print(sum(list(map(int, numbers))))
