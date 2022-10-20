
numbers = [     [99, 11, 66, 86, 55],
               [44, 21, 65, 88, 24],
               [33, 77, 32, 33, 34]]


rnum = len(numbers)
cnum = len(numbers[0])

print ('Sum of rows: ', end=' ')
for i in range(rnum):
	rsum = sum(numbers[i])
	print (rsum, end=' ')
print()

# ******************************
# Make your Code
# ******************************
rmax = 0
maxnum = 0
checked = False
print('Sum of columns: ', end = ' ')
for i in range(cnum):
    csum = 0
    for j in range(rnum):
        csum += numbers[j][i]
        if maxnum < numbers[j][i]:
            maxnum = numbers[j][i]
        if not checked:
            rsum = sum(numbers[j])
            if rmax < rsum:
                rmax = rsum
                maxr = j
    checked = True

    print (csum, end = ' ')
print()

print(f"The row that has the greatest sum: {maxr}")
print(f"The greatest number: {maxnum}")