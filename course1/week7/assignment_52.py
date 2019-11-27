largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" :
        break
    try :
        inum = int(num)
    except :
        print('Invalid input')
        continue
    if smallest is None or largest is None:
        smallest = largest = inum
    if inum < smallest :
        smallest = inum
    if inum > largest :
        largest = inum

print('Maximum is', largest)
print('Minimum is', smallest)
